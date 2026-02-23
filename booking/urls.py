from django.urls import path
from booking.apps import BookingConfig
from booking.views import BookingView, AboutView, MainView, available_tables

app_name = BookingConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="main"),
    path("about/", AboutView.as_view(), name="about"),
    path("booking/", BookingView.as_view(), name="booking"),
    path("available_tables/", available_tables, name="available_tables"),
]
