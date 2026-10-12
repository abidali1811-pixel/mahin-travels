from django.conf import settings
from .models import SiteTheme


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
