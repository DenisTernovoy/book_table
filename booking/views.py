from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class BookingView(TemplateView):
    template_name = "booking/main_page.html"
