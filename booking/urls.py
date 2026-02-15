from django.urls import path
from booking.apps import BookingConfig
from booking.views import BookingView

app_name = BookingConfig.name

urlpatterns = [
    path("", BookingView.as_view(), name="booking"),
]
