from django.urls import path
from booking.apps import BookingConfig
from booking.views import BookingView, AboutView, MainView

app_name = BookingConfig.name

urlpatterns = [
    path("", MainView.as_view(), name="booking"),
    path("about/", AboutView.as_view(), name="about"),
    path("booking/", BookingView.as_view(), name="booking"),
]
