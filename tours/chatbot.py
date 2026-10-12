"""Google Gemini chatbot that answers using live tour, hotel and transport data."""

import logging

from django.conf import settings

from .models import Hotel, TourPackage, TransportOption

logger = logging.getLogger(__name__)


def _catalog_text():
    packages = TourPackage.objects.filter(is_published=True)
    hotels = Hotel.objects.filter(is_published=True)
    transport = TransportOption.objects.filter(is_published=True)

    lines = ["TOUR PACKAGES (rates in Indian Rupees / INR):"]
    for pkg in packages:
        lines.append(
            f"- {pkg.title} | {pkg.destination} | {pkg.duration_days} days / "
            f"{pkg.duration_nights} nights | Rs {pkg.per_person_rate_inr} per person | "
            f"example total for {pkg.typical_group_size} people: Rs {pkg.total_rate_inr}. "
            f"{pkg.short_description}"
        )
        hotel_names = ", ".join(h.name for h in pkg.hotels.filter(is_published=True)[:4])
        if hotel_names:
            lines.append(f"  Hotels: {hotel_names}")

    lines.append("\nHOTELS (price per night in INR):")
    for hotel in hotels:
        lines.append(
            f"- {hotel.name}, {hotel.city}, {hotel.star_rating} star, "
            f"Rs {hotel.price_per_night_inr}/night. {hotel.description[:180]}"
        )

    lines.append("\nTRANSPORT (car and bus, rates in INR):")
    for item in transport:
        lines.append(
            f"- {item.get_transport_type_display()} {item.name}: "
            f"{item.capacity} seats, Rs {item.rate_per_day_inr}/day, "
            f"Rs {item.rate_per_person_inr}/person. {item.description[:160]}"
        )
    return "\n".join(lines)


def ask_gemini(user_message):
    api_key = settings.GEMINI_API_KEY
    if not api_key:
        return (
            "The travel assistant is not configured yet. "
            "Add GEMINI_API_KEY to your .env file and restart the server."
        )

    try:
        from google import genai
        from google.genai import types
    except ImportError:
        return "The Gemini library is not installed. Run: pip install google-generativeai"

    system = (
        "You are Mahin, a friendly travel advisor for Mahin Travels, an India tour company. "
        "Answer only using the catalog below. Prices are in Indian Rupees (INR). "
        "When quoting a package, always mention per-person rate and an example total. "
        "If the traveller wants to book or get a quote, direct them to the enquiry form at "
        "/contact/ and mention they can select a tour package, hotel, and car or bus. "
        "If asked about something not in the catalog, say you will connect them via the "
        "enquiry form. Keep answers short (under 120 words). Do not invent prices.\n\n"
        + _catalog_text()
    )

    try:
        client = genai.Client(api_key=api_key)
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=user_message,
            config=types.GenerateContentConfig(system_instruction=system),
        )
        text = (response.text or "").strip()
        return text or "I could not form a reply. Please try again."
    except Exception as exc:
        logger.error("Gemini request failed (%s)", type(exc).__name__)
        return "Sorry, I could not reach the travel assistant right now. Please try again shortly or send us an enquiry."
