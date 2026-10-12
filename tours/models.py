from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse


class TourPackage(models.Model):
    """A packaged India tour sold on the public website."""

    title = models.CharField(max_length=160)
    slug = models.SlugField(unique=True)
    destination = models.CharField(max_length=120, help_text="e.g. Rajasthan, Kerala")
    duration_days = models.PositiveIntegerField()
    duration_nights = models.PositiveIntegerField()
    short_description = models.CharField(max_length=280)
    description = models.TextField()
    itinerary = models.TextField(help_text="One day per line works well.")
    highlights = models.TextField(blank=True, help_text="One highlight per line.")
    cover_image = models.ImageField(upload_to="packages/", blank=True)
    cover_image_url = models.URLField(
        blank=True,
        help_text="Used when no uploaded file is set (handy for sample data).",
    )
    per_person_rate_inr = models.PositiveIntegerField(
        help_text="Base package rate per person in Indian Rupees."
    )
    typical_group_size = models.PositiveIntegerField(
        default=2,
        help_text="Used to show an example total price.",
    )
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("package_detail", args=[self.slug])

    @property
    def total_rate_inr(self):
        return self.per_person_rate_inr * self.typical_group_size

    def display_image(self):
        if self.cover_image:
            return self.cover_image.url
        return self.cover_image_url

    def highlight_list(self):
        return [line.strip() for line in self.highlights.splitlines() if line.strip()]

    def itinerary_days(self):
        return [line.strip() for line in self.itinerary.splitlines() if line.strip()]


class Hotel(models.Model):
    """Hotel that can be offered with one or more tour packages."""

    STAR_CHOICES = [(n, f"{n} Star") for n in range(2, 6)]

    name = models.CharField(max_length=160)
    city = models.CharField(max_length=80)
    star_rating = models.PositiveSmallIntegerField(choices=STAR_CHOICES, default=3)
    description = models.TextField()
    amenities = models.CharField(
        max_length=300,
        blank=True,
        help_text="Comma-separated, e.g. Wi-Fi, Breakfast, Pool",
    )
    image = models.ImageField(upload_to="hotels/", blank=True)
    image_url = models.URLField(blank=True)
    price_per_night_inr = models.PositiveIntegerField()
    packages = models.ManyToManyField(TourPackage, related_name="hotels", blank=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["city", "name"]

    def __str__(self):
        return f"{self.name} ({self.city})"

    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url

    def amenity_list(self):
        return [item.strip() for item in self.amenities.split(",") if item.strip()]


class TransportOption(models.Model):
    """Car or bus transport that can be added to a tour."""

    CAR = "car"
    BUS = "bus"
    TYPE_CHOICES = [(CAR, "Car"), (BUS, "Bus")]

    name = models.CharField(max_length=120)
    transport_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    description = models.TextField()
    capacity = models.PositiveIntegerField(help_text="Number of passengers")
    rate_per_day_inr = models.PositiveIntegerField(
        help_text="Vehicle hire rate per day in INR."
    )
    rate_per_person_inr = models.PositiveIntegerField(
        help_text="Share/seat rate per person in INR (useful for buses)."
    )
    image = models.ImageField(upload_to="transport/", blank=True)
    image_url = models.URLField(blank=True)
    packages = models.ManyToManyField(
        TourPackage, related_name="transport_options", blank=True
    )
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["transport_type", "name"]

    def __str__(self):
        return f"{self.get_transport_type_display()} — {self.name}"

    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url


class GalleryImage(models.Model):
    """Photos shown in the public gallery and homepage mosaic."""

    title = models.CharField(max_length=120)
    caption = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to="gallery/", blank=True)
    image_url = models.URLField(
        blank=True,
        help_text="Used when no uploaded file is set.",
    )
    sort_order = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title

    def display_image(self):
        if self.image:
            return self.image.url
        return self.image_url


class Enquiry(models.Model):
    """Contact form submissions from the public website."""

    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    package = models.ForeignKey(
        TourPackage,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="enquiries",
    )
    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="enquiries",
    )
    transport = models.ForeignKey(
        TransportOption,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="enquiries",
    )
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Enquiries"

    def __str__(self):
        return f"{self.name} — {self.created_at:%d %b %Y}"


class SiteTheme(models.Model):
    """Optional website color palette editable from the admin."""

    color_validator = RegexValidator(
        regex=r"^#[0-9A-Fa-f]{6}$",
        message="Enter a six-digit hex color, such as #0B4F6C.",
    )

    page_background = models.CharField(max_length=7, default="#f7f3eb", validators=[color_validator])
    section_background = models.CharField(max_length=7, default="#efe8db", validators=[color_validator])
    card_background = models.CharField(max_length=7, default="#fffdf8", validators=[color_validator])
    text_color = models.CharField(max_length=7, default="#1c1917", validators=[color_validator])
    muted_text_color = models.CharField(max_length=7, default="#57534e", validators=[color_validator])
    primary_color = models.CharField(max_length=7, default="#0b4f6c", validators=[color_validator])
    primary_dark_color = models.CharField(max_length=7, default="#083d54", validators=[color_validator])
    accent_color = models.CharField(max_length=7, default="#e07a3d", validators=[color_validator])
    border_color = models.CharField(max_length=7, default="#e7e0d4", validators=[color_validator])

    class Meta:
        verbose_name = "Website colors"
        verbose_name_plural = "Website colors"

    def __str__(self):
        return "Website colors"
