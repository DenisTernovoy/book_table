from django.views.generic import TemplateView, CreateView

from booking.forms import BookingForm
from booking.models import Booking


# Create your views here.
class MainView(TemplateView):
    template_name = "booking/main_page.html"


class AboutView(TemplateView):
    template_name = "booking/about.html"


class BookingView(CreateView):
    template_name = "booking/booking.html"
    model = Booking
    form_class = BookingForm
