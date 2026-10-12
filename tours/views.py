from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .chatbot import ask_gemini
from .forms import EnquiryForm
from .models import GalleryImage, Hotel, TourPackage, TransportOption


def home(request):
    featured = TourPackage.objects.filter(is_published=True, is_featured=True)[:6]
    if not featured:
        featured = TourPackage.objects.filter(is_published=True)[:6]
    gallery = GalleryImage.objects.filter(is_published=True)[:8]
    return render(
        request,
        "tours/home.html",
        {"featured": featured, "gallery": gallery},
    )


def services(request):
    packages = TourPackage.objects.filter(is_published=True)
    query = request.GET.get("q", "").strip()
    if query:
        packages = packages.filter(
            Q(title__icontains=query)
            | Q(destination__icontains=query)
            | Q(short_description__icontains=query)
        )
    cars = TransportOption.objects.filter(is_published=True, transport_type="car")
    buses = TransportOption.objects.filter(is_published=True, transport_type="bus")
    return render(
        request,
        "tours/services.html",
        {"packages": packages, "cars": cars, "buses": buses, "query": query},
    )


def package_detail(request, slug):
    package = get_object_or_404(TourPackage, slug=slug, is_published=True)
    hotels = package.hotels.filter(is_published=True)
    transport = package.transport_options.filter(is_published=True)
    form = EnquiryForm(initial={"package": package})
    return render(
        request,
        "tours/package_detail.html",
        {
            "package": package,
            "hotels": hotels,
            "transport": transport,
            "form": form,
        },
    )


def hotels(request):
    hotel_list = Hotel.objects.filter(is_published=True).prefetch_related("packages")
    return render(request, "tours/hotels.html", {"hotels": hotel_list})


def gallery(request):
    images = GalleryImage.objects.filter(is_published=True)
    return render(request, "tours/gallery.html", {"images": images})


def contact(request):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you. Your enquiry has been saved. Our team will contact you soon.",
            )
            return redirect("contact")
    else:
        initial = {}
        package_id = request.GET.get("package")
        hotel_id = request.GET.get("hotel")
        transport_id = request.GET.get("transport")
        if package_id:
            initial["package"] = package_id
        if hotel_id:
            initial["hotel"] = hotel_id
        if transport_id:
            initial["transport"] = transport_id
        form = EnquiryForm(initial=initial)
    return render(request, "tours/contact.html", {"form": form})


@require_POST
def chat_api(request):
    message = (request.POST.get("message") or "").strip()
    if not message:
        return JsonResponse({"reply": "Please type a question about our tours."})
    if len(message) > 800:
        return JsonResponse({"reply": "Please keep your question a little shorter."})
    reply = ask_gemini(message)
    return JsonResponse({"reply": reply})
