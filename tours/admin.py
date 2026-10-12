from django import forms
from django.contrib import admin

from .models import Enquiry, GalleryImage, Hotel, SiteTheme, TourPackage, TransportOption


@admin.register(SiteTheme)
class SiteThemeAdmin(admin.ModelAdmin):
    class ThemeForm(forms.ModelForm):
        class Meta:
            model = SiteTheme
            fields = "__all__"
            widgets = {
                field: forms.TextInput(attrs={"type": "color"})
                for field in (
                    "page_background", "section_background", "card_background",
                    "text_color", "muted_text_color", "primary_color",
                    "primary_dark_color", "accent_color", "border_color",
                )
            }

    form = ThemeForm
    fieldsets = (
        ("Backgrounds", {"fields": ("page_background", "section_background", "card_background")}),
        ("Text", {"fields": ("text_color", "muted_text_color")}),
        ("Brand colors", {"fields": ("primary_color", "primary_dark_color", "accent_color", "border_color")}),
    )

    def has_add_permission(self, request):
        return not SiteTheme.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "destination",
        "duration_days",
        "per_person_rate_inr",
        "is_featured",
        "is_published",
    )
    list_filter = ("is_featured", "is_published", "destination")
    search_fields = ("title", "destination", "short_description")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "star_rating", "price_per_night_inr", "is_published")
    list_filter = ("city", "star_rating", "is_published")
    search_fields = ("name", "city")
    filter_horizontal = ("packages",)


@admin.register(TransportOption)
class TransportOptionAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "transport_type",
        "capacity",
        "rate_per_day_inr",
        "rate_per_person_inr",
        "is_published",
    )
    list_filter = ("transport_type", "is_published")
    search_fields = ("name",)
    filter_horizontal = ("packages",)


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ("title", "sort_order", "is_published", "created_at")
    list_editable = ("sort_order", "is_published")
    search_fields = ("title", "caption")


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "package", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "phone", "message")
    readonly_fields = (
        "name", "email", "phone", "package", "hotel", "transport", "message", "created_at"
    )
    list_editable = ("is_read",)
