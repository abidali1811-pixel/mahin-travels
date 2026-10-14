from django import forms

from .models import Enquiry, Hotel, TourPackage, TransportOption


class EnquiryForm(forms.ModelForm):
    captcha = forms.CharField(
        label="Enter the characters shown",
        max_length=6,
        widget=forms.TextInput(attrs={"autocomplete": "off", "inputmode": "text"}),
    )

    class Meta:
        model = Enquiry
        fields = ["name", "email", "phone", "package", "hotel", "transport", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your full name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "phone": forms.TextInput(attrs={"placeholder": "+91 ..."}),
            "message": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "Tell us your travel dates, group size, and destinations.",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        self.captcha_answer = kwargs.pop("captcha_answer", None)
        super().__init__(*args, **kwargs)
        self.fields["package"].queryset = TourPackage.objects.filter(is_published=True)
        self.fields["package"].required = False
        self.fields["package"].empty_label = "General enquiry (no package yet)"
        self.fields["hotel"].queryset = Hotel.objects.filter(is_published=True)
        self.fields["hotel"].required = False
        self.fields["hotel"].empty_label = "No specific hotel"
        self.fields["transport"].queryset = TransportOption.objects.filter(is_published=True)
        self.fields["transport"].required = False
        self.fields["transport"].empty_label = "No specific transport"
        for name, field in self.fields.items():
            css = "input"
            if name == "message":
                css = "textarea"
            elif name in ("package", "hotel", "transport"):
                css = "select"
            field.widget.attrs["class"] = css

    def clean_captcha(self):
        value = self.cleaned_data["captcha"].strip().upper()
        if not self.captcha_answer or value != self.captcha_answer:
            raise forms.ValidationError("The security code did not match. Please try again.")
        return value
