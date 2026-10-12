from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("packages/<slug:slug>/", views.package_detail, name="package_detail"),
    path("hotels/", views.hotels, name="hotels"),
    path("gallery/", views.gallery, name="gallery"),
    path("contact/", views.contact, name="contact"),
    path("chat/", views.chat_api, name="chat_api"),
]
