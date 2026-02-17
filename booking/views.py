from django.views.generic import TemplateView


# Create your views here.
class BookingView(TemplateView):
    template_name = "booking/main_page.html"


class AboutView(TemplateView):
    template_name = "booking/about.html"
