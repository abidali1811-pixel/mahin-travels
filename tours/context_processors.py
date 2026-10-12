from django.conf import settings
from .models import Enquiry, GalleryImage, Hotel, SiteTheme, TourPackage


def site_defaults(request):
    theme = SiteTheme.objects.first()
    return {
        "SITE_NAME": settings.SITE_NAME,
        "SITE_TAGLINE": settings.SITE_TAGLINE,
        "SITE_PHONE": settings.SITE_PHONE,
        "SITE_EMAIL": settings.SITE_EMAIL,
        "SITE_ADDRESS": settings.SITE_ADDRESS,
        "site_theme": theme,
    }


def admin_dashboard(request):
    """Counts for the custom admin overview, only queried on the dashboard."""
    if request.path != "/admin/" or not getattr(request.user, "is_staff", False):
        return {}

    return {
        "dashboard_counts": {
            "new_enquiries": Enquiry.objects.filter(is_read=False).count(),
            "tours": TourPackage.objects.count(),
            "hotels": Hotel.objects.count(),
            "gallery": GalleryImage.objects.count(),
        },
        "recent_enquiries": Enquiry.objects.select_related("package").order_by(
            "-created_at"
        )[:5],
    }
