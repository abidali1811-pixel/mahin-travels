"""Load sample India tour, hotel, transport and gallery records."""

from django.core.management.base import BaseCommand

from tours.models import GalleryImage, Hotel, TourPackage, TransportOption

PACKAGES = [
    {
        "title": "Golden Triangle Classic",
        "slug": "golden-triangle-classic",
        "destination": "Delhi · Agra · Jaipur",
        "duration_days": 6,
        "duration_nights": 5,
        "short_description": "Delhi, Agra and Jaipur in one iconic North India circuit.",
        "description": (
            "Walk through Old Delhi, watch sunrise at the Taj Mahal, and explore the "
            "pink palaces of Jaipur. Ideal first trip to North India with comfortable "
            "hotels and private car transfers between cities."
        ),
        "itinerary": (
            "Day 1: Arrive Delhi, Old Delhi rickshaw ride and India Gate.\n"
            "Day 2: Qutub Minar, Humayun's Tomb, drive to Agra.\n"
            "Day 3: Taj Mahal sunrise, Agra Fort, drive to Jaipur.\n"
            "Day 4: Amber Fort, City Palace, Jantar Mantar.\n"
            "Day 5: Local bazaars and optional balloon ride.\n"
            "Day 6: Return to Delhi and departure."
        ),
        "highlights": "Taj Mahal sunrise\nAmber Fort elephant / jeep ride\nOld Delhi food walk",
        "cover_image_url": "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=1200",
        "per_person_rate_inr": 28500,
        "typical_group_size": 2,
        "is_featured": True,
    },
    {
        "title": "Kerala Backwaters & Hills",
        "slug": "kerala-backwaters-hills",
        "destination": "Kochi · Munnar · Alleppey",
        "duration_days": 7,
        "duration_nights": 6,
        "short_description": "Tea estates of Munnar and a private houseboat on the backwaters.",
        "description": (
            "Start in historic Kochi, drive into the Western Ghats for tea gardens, "
            "then drift overnight on a traditional Kerala houseboat through Alleppey."
        ),
        "itinerary": (
            "Day 1: Arrive Kochi, Fort Kochi walk.\n"
            "Day 2: Drive to Munnar, tea museum.\n"
            "Day 3: Eravikulam National Park and spice gardens.\n"
            "Day 4: Drive to Alleppey, board houseboat.\n"
            "Day 5: Village cruise and stay in a lakeside resort.\n"
            "Day 6: Relaxation and Ayurveda massage.\n"
            "Day 7: Transfer to Kochi airport."
        ),
        "highlights": "Overnight houseboat\nMunnar tea trails\nKathakali performance",
        "cover_image_url": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=1200",
        "per_person_rate_inr": 34200,
        "typical_group_size": 2,
        "is_featured": True,
    },
    {
        "title": "Goa Beaches & Heritage",
        "slug": "goa-beaches-heritage",
        "destination": "North & South Goa",
        "duration_days": 5,
        "duration_nights": 4,
        "short_description": "Beach time, Portuguese churches and spice-scented village tours.",
        "description": (
            "A relaxed Goa holiday mixing North Goa nightlife, South Goa beaches, "
            "Old Goa churches and a river cruise. Car and bus options available."
        ),
        "itinerary": (
            "Day 1: Arrive Goa, Calangute / Baga beach.\n"
            "Day 2: Old Goa churches and Fontainhas.\n"
            "Day 3: South Goa beaches and spice plantation.\n"
            "Day 4: Free day or Dudhsagar day trip.\n"
            "Day 5: Departure."
        ),
        "highlights": "Basilica of Bom Jesus\nSpice plantation lunch\nSunset cruise",
        "cover_image_url": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1200",
        "per_person_rate_inr": 19800,
        "typical_group_size": 2,
        "is_featured": True,
    },
    {
        "title": "Rajasthan Royal Circuit",
        "slug": "rajasthan-royal-circuit",
        "destination": "Jaipur · Jodhpur · Udaipur",
        "duration_days": 8,
        "duration_nights": 7,
        "short_description": "Forts, lakes and desert palaces across royal Rajasthan.",
        "description": (
            "From Jaipur's Amber Fort to Jodhpur's Mehrangarh and the lakes of Udaipur. "
            "Heritage hotels and private AC car transfers throughout."
        ),
        "itinerary": (
            "Day 1: Arrive Jaipur.\n"
            "Day 2: Amber Fort and bazaars.\n"
            "Day 3: Drive to Jodhpur via Pushkar (optional).\n"
            "Day 4: Mehrangarh Fort and blue city walk.\n"
            "Day 5: Drive to Udaipur.\n"
            "Day 6: City Palace and Lake Pichola boat.\n"
            "Day 7: Fateh Sagar and local crafts.\n"
            "Day 8: Departure."
        ),
        "highlights": "Mehrangarh Fort\nLake Pichola sunset boat\nHeritage hotel stay",
        "cover_image_url": "https://images.unsplash.com/photo-1578999935853-4ec5fa6c1f60?w=1200",
        "per_person_rate_inr": 42500,
        "typical_group_size": 2,
        "is_featured": True,
    },
    {
        "title": "Himachal Hill Escape",
        "slug": "himachal-hill-escape",
        "destination": "Shimla · Manali",
        "duration_days": 6,
        "duration_nights": 5,
        "short_description": "Pine forests, mountain roads and snow views in Himachal Pradesh.",
        "description": (
            "A classic hill-station holiday covering Shimla's colonial mall and Manali's "
            "Solang Valley, with AC innova or tempo traveller options for families."
        ),
        "itinerary": (
            "Day 1: Chandigarh / Delhi pickup, drive to Shimla.\n"
            "Day 2: Mall Road, Jakhu, Kufri.\n"
            "Day 3: Drive to Manali via Kullu.\n"
            "Day 4: Solang Valley and Hadimba Temple.\n"
            "Day 5: Optional Rohtang / Atal Tunnel (seasonal).\n"
            "Day 6: Drive to Chandigarh / Delhi."
        ),
        "highlights": "Solang Valley\nShimla Mall Road\nKullu river views",
        "cover_image_url": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=1200",
        "per_person_rate_inr": 26800,
        "typical_group_size": 4,
        "is_featured": False,
    },
    {
        "title": "Kashmir Valley Delight",
        "slug": "kashmir-valley-delight",
        "destination": "Srinagar · Gulmarg · Pahalgam",
        "duration_days": 6,
        "duration_nights": 5,
        "short_description": "Houseboats, meadows and snow-capped peaks of Kashmir.",
        "description": (
            "Stay on a Dal Lake houseboat, ride the Gulmarg gondola and walk the "
            "Betaab Valley in Pahalgam. Rates include hotels and local taxis."
        ),
        "itinerary": (
            "Day 1: Arrive Srinagar, Shikara on Dal Lake.\n"
            "Day 2: Mughal gardens and houseboat stay.\n"
            "Day 3: Gulmarg gondola.\n"
            "Day 4: Drive to Pahalgam.\n"
            "Day 5: Aru / Betaab Valley.\n"
            "Day 6: Return Srinagar and fly out."
        ),
        "highlights": "Dal Lake shikara\nGulmarg gondola\nBetaab Valley",
        "cover_image_url": "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=1200",
        "per_person_rate_inr": 38900,
        "typical_group_size": 2,
        "is_featured": True,
    },
    {
        "title": "South India Temple Trail",
        "slug": "south-india-temple-trail",
        "destination": "Chennai · Madurai · Thanjavur",
        "duration_days": 7,
        "duration_nights": 6,
        "short_description": "Living temples, classical music towns and Chettinad flavours.",
        "description": (
            "A cultural circuit of Tamil Nadu covering Meenakshi Amman Temple, "
            "Brihadeeswara and Mahabalipuram shore temples, with AC bus or car."
        ),
        "itinerary": (
            "Day 1: Arrive Chennai, Marina Beach.\n"
            "Day 2: Mahabalipuram.\n"
            "Day 3: Drive to Thanjavur.\n"
            "Day 4: Brihadeeswara Temple.\n"
            "Day 5: Madurai Meenakshi Temple evening aarti.\n"
            "Day 6: Chettinad mansions.\n"
            "Day 7: Departure from Madurai / Chennai."
        ),
        "highlights": "Meenakshi Temple aarti\nUNESCO Brihadeeswara\nMahabalipuram shore temple",
        "cover_image_url": "https://images.unsplash.com/photo-1731268380735-4f7f0b128a0a?w=1200",
        "per_person_rate_inr": 31200,
        "typical_group_size": 2,
        "is_featured": False,
    },
    {
        "title": "Andaman Island Break",
        "slug": "andaman-island-break",
        "destination": "Port Blair · Havelock",
        "duration_days": 5,
        "duration_nights": 4,
        "short_description": "Turquoise water, Radhanagar Beach and a light island hopping plan.",
        "description": (
            "Fly into Port Blair, ferry to Havelock (Swaraj Dweep) for snorkelling "
            "and beach time. Hotel rates shown per night; package includes ferry."
        ),
        "itinerary": (
            "Day 1: Arrive Port Blair, Cellular Jail light show.\n"
            "Day 2: Ferry to Havelock, Radhanagar Beach.\n"
            "Day 3: Elephant Beach snorkel.\n"
            "Day 4: Return Port Blair, Corbyn's Cove.\n"
            "Day 5: Departure."
        ),
        "highlights": "Radhanagar Beach\nElephant Beach snorkel\nCellular Jail",
        "cover_image_url": "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?w=1200",
        "per_person_rate_inr": 36500,
        "typical_group_size": 2,
        "is_featured": False,
    },
]

HOTELS = [
    {
        "name": "Haveli Heritage Inn",
        "city": "Jaipur",
        "star_rating": 4,
        "description": "A restored haveli near the old city with courtyard breakfasts.",
        "amenities": "Wi-Fi, Breakfast, Airport transfer, AC",
        "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=1200",
        "price_per_night_inr": 6500,
        "packages": ["golden-triangle-classic", "rajasthan-royal-circuit"],
    },
    {
        "name": "Taj View Residency",
        "city": "Agra",
        "star_rating": 4,
        "description": "Comfortable rooms with easy access to the Taj Mahal east gate.",
        "amenities": "Wi-Fi, Breakfast, Restaurant, AC",
        "image_url": "https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=1200",
        "price_per_night_inr": 7200,
        "packages": ["golden-triangle-classic"],
    },
    {
        "name": "Connaught Stay",
        "city": "New Delhi",
        "star_rating": 4,
        "description": "Central Delhi hotel, walkable to Connaught Place.",
        "amenities": "Wi-Fi, Breakfast, Gym, AC",
        "image_url": "https://images.unsplash.com/photo-1551882547-ff40c63fe5fa?w=1200",
        "price_per_night_inr": 8000,
        "packages": ["golden-triangle-classic"],
    },
    {
        "name": "Lake Palace Boutique",
        "city": "Udaipur",
        "star_rating": 5,
        "description": "Lakeside rooms looking across Pichola with a rooftop restaurant.",
        "amenities": "Wi-Fi, Breakfast, Pool, Lake view",
        "image_url": "https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1200",
        "price_per_night_inr": 14500,
        "packages": ["rajasthan-royal-circuit"],
    },
    {
        "name": "Blue City Haveli",
        "city": "Jodhpur",
        "star_rating": 3,
        "description": "Family-run stay in the blue lanes below Mehrangarh Fort.",
        "amenities": "Wi-Fi, Breakfast, Rooftop, AC",
        "image_url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=1200",
        "price_per_night_inr": 4800,
        "packages": ["rajasthan-royal-circuit"],
    },
    {
        "name": "Tea Garden Resort",
        "city": "Munnar",
        "star_rating": 4,
        "description": "Cottages overlooking tea slopes, with bonfire evenings.",
        "amenities": "Wi-Fi, Breakfast, Mountain view, Restaurant",
        "image_url": "https://images.unsplash.com/photo-1571003123894-1f0594d2b5d9?w=1200",
        "price_per_night_inr": 7800,
        "packages": ["kerala-backwaters-hills"],
    },
    {
        "name": "Backwater Houseboat",
        "city": "Alleppey",
        "star_rating": 3,
        "description": "Private AC houseboat with chef, overnight cruise included.",
        "amenities": "Meals, AC cabin, Deck lounge",
        "image_url": "https://images.unsplash.com/photo-1593693411515-2b7aa477de24?w=1200",
        "price_per_night_inr": 12000,
        "packages": ["kerala-backwaters-hills"],
    },
    {
        "name": "Harbour Heritage",
        "city": "Kochi",
        "star_rating": 4,
        "description": "Fort Kochi boutique hotel in a spice-trade warehouse.",
        "amenities": "Wi-Fi, Breakfast, Courtyard, AC",
        "image_url": "https://images.unsplash.com/photo-1611892440504-42a792e24d32?w=1200",
        "price_per_night_inr": 6900,
        "packages": ["kerala-backwaters-hills"],
    },
    {
        "name": "Palm Breeze Goa",
        "city": "Calangute",
        "star_rating": 4,
        "description": "Resort 400 metres from the beach with a large pool.",
        "amenities": "Wi-Fi, Breakfast, Pool, Beach shuttle",
        "image_url": "https://images.unsplash.com/photo-1571896349842-33c89424de2d?w=1200",
        "price_per_night_inr": 8500,
        "packages": ["goa-beaches-heritage"],
    },
    {
        "name": "Pine View Shimla",
        "city": "Shimla",
        "star_rating": 3,
        "description": "Hill-facing rooms a short walk from Mall Road.",
        "amenities": "Wi-Fi, Breakfast, Heater, Restaurant",
        "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800",
        "price_per_night_inr": 5200,
        "packages": ["himachal-hill-escape"],
    },
    {
        "name": "Solang Valley Lodge",
        "city": "Manali",
        "star_rating": 3,
        "description": "Simple mountain lodge with packed-lunch picnic options.",
        "amenities": "Wi-Fi, Breakfast, Parking, Heater",
        "image_url": "https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=800",
        "price_per_night_inr": 4600,
        "packages": ["himachal-hill-escape"],
    },
    {
        "name": "Dal Lake Houseboat",
        "city": "Srinagar",
        "star_rating": 4,
        "description": "Cedar-wood houseboat with shikara pickup at the jetty.",
        "amenities": "Meals, Lake view, Heater",
        "image_url": "https://images.unsplash.com/photo-1566073771259-6a8506099945?w=900",
        "price_per_night_inr": 9800,
        "packages": ["kashmir-valley-delight"],
    },
    {
        "name": "Meadows Pahalgam",
        "city": "Pahalgam",
        "star_rating": 4,
        "description": "Riverside hotel with garden lawns and mountain views.",
        "amenities": "Wi-Fi, Breakfast, Garden, Heater",
        "image_url": "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=1200",
        "price_per_night_inr": 7600,
        "packages": ["kashmir-valley-delight"],
    },
    {
        "name": "Temple Town Stay",
        "city": "Madurai",
        "star_rating": 3,
        "description": "Clean AC rooms near Meenakshi Temple with rooftop dining.",
        "amenities": "Wi-Fi, Breakfast, AC, Restaurant",
        "image_url": "https://images.unsplash.com/photo-1631049307264-da0ec9d70304?w=1200",
        "price_per_night_inr": 3900,
        "packages": ["south-india-temple-trail"],
    },
    {
        "name": "Coral Sands Havelock",
        "city": "Havelock",
        "star_rating": 4,
        "description": "Beach cottages a short walk from Radhanagar Beach.",
        "amenities": "Wi-Fi, Breakfast, Beach access, AC",
        "image_url": "https://images.unsplash.com/photo-1573843981267-be1999ff37cd?w=1200",
        "price_per_night_inr": 11200,
        "packages": ["andaman-island-break"],
    },
]

TRANSPORT = [
    {
        "name": "Toyota Innova Crysta",
        "transport_type": "car",
        "description": "AC SUV for families. Ideal for Golden Triangle and hill drives.",
        "capacity": 6,
        "rate_per_day_inr": 4500,
        "rate_per_person_inr": 900,
        "image_url": "https://images.unsplash.com/photo-1549317661-bd32c8ce0db2?w=1200",
        "packages": [
            "golden-triangle-classic",
            "rajasthan-royal-circuit",
            "himachal-hill-escape",
            "kerala-backwaters-hills",
        ],
    },
    {
        "name": "Maruti Dzire / Etios",
        "transport_type": "car",
        "description": "Sedan for 2–3 travellers on city circuits and airport runs.",
        "capacity": 3,
        "rate_per_day_inr": 2800,
        "rate_per_person_inr": 950,
        "image_url": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=1200",
        "packages": [
            "golden-triangle-classic",
            "goa-beaches-heritage",
            "south-india-temple-trail",
        ],
    },
    {
        "name": "Tempo Traveller (12 seater)",
        "transport_type": "car",
        "description": "Force Traveller with push-back seats for small groups.",
        "capacity": 12,
        "rate_per_day_inr": 7500,
        "rate_per_person_inr": 650,
        "image_url": "https://images.unsplash.com/photo-1544620341-11cb2cd7c00b?w=1200",
        "packages": ["himachal-hill-escape", "rajasthan-royal-circuit", "south-india-temple-trail"],
    },
    {
        "name": "Volvo Multi-Axle AC Coach",
        "transport_type": "bus",
        "description": "Long-distance AC sleeper/seater coach for group departures.",
        "capacity": 40,
        "rate_per_day_inr": 28000,
        "rate_per_person_inr": 1200,
        "image_url": "https://images.unsplash.com/photo-1544620341-11cb2cd7c00b?w=1200",
        "packages": ["golden-triangle-classic", "south-india-temple-trail", "goa-beaches-heritage"],
    },
    {
        "name": "Mini Coach (27 seater AC)",
        "transport_type": "bus",
        "description": "Mid-size AC bus for school, family and corporate groups.",
        "capacity": 27,
        "rate_per_day_inr": 16000,
        "rate_per_person_inr": 850,
        "image_url": "https://images.unsplash.com/photo-1570125909232-eb263c188f7e?w=1200",
        "packages": ["kerala-backwaters-hills", "himachal-hill-escape"],
    },
    {
        "name": "Non-AC Pushback Bus",
        "transport_type": "bus",
        "description": "Budget group transport for short interstate runs.",
        "capacity": 45,
        "rate_per_day_inr": 11000,
        "rate_per_person_inr": 450,
        "image_url": "https://images.unsplash.com/photo-1544620341-11cb2cd7c00b?w=800",
        "packages": ["south-india-temple-trail"],
    },
]

GALLERY = [
    ("Taj Mahal, Agra", "Sunrise at India's most famous monument.", "https://images.unsplash.com/photo-1564507592333-c60657eea523?w=1000"),
    ("Jaipur palaces", "Pink City courtyards and carved facades.", "https://images.unsplash.com/photo-1578999935853-4ec5fa6c1f60?w=1000"),
    ("Kerala backwaters", "Canoes and coconut groves near Alleppey.", "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=1000"),
    ("Goa shoreline", "Arabian Sea beaches and palms.", "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1000"),
    ("Himalayan road", "Hill roads through Himachal Pradesh.", "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=1000"),
    ("Dal Lake", "Shikaras on the water in Srinagar.", "https://images.unsplash.com/photo-1595815771614-ade9d652a65d?w=1000"),
    ("South Indian temple", "Gopuram towers of Tamil Nadu.", "https://images.unsplash.com/photo-1731268380735-4f7f0b128a0a?w=1000"),
    ("Andaman waters", "Clear water around Havelock Island.", "https://images.unsplash.com/photo-1589308078059-be1415eab4c3?w=1000"),
    ("Udaipur lake", "Evening light on Lake Pichola.", "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=1000"),
    ("Tea gardens", "Munnar slopes after monsoon.", "https://images.unsplash.com/photo-1593693397690-362cb9666fc2?w=1000"),
]


class Command(BaseCommand):
    help = "Insert sample India travel packages, hotels, transport and gallery images."

    def handle(self, *args, **options):
        packages = {}
        for data in PACKAGES:
            obj, created = TourPackage.objects.update_or_create(
                slug=data["slug"], defaults=data
            )
            packages[obj.slug] = obj
            self.stdout.write(("Created " if created else "Updated ") + obj.title)

        for data in HOTELS:
            payload = {k: v for k, v in data.items() if k != "packages"}
            obj, _ = Hotel.objects.update_or_create(
                name=data["name"], city=data["city"], defaults=payload
            )
            obj.packages.set(
                [packages[s] for s in data["packages"] if s in packages]
            )

        for data in TRANSPORT:
            payload = {k: v for k, v in data.items() if k != "packages"}
            obj, _ = TransportOption.objects.update_or_create(
                name=data["name"], defaults=payload
            )
            obj.packages.set(
                [packages[s] for s in data["packages"] if s in packages]
            )

        for order, (title, caption, url) in enumerate(GALLERY, start=1):
            GalleryImage.objects.update_or_create(
                title=title,
                defaults={
                    "caption": caption,
                    "image_url": url,
                    "sort_order": order,
                    "is_published": True,
                },
            )

        self.stdout.write(self.style.SUCCESS("Sample India travel data is ready."))
