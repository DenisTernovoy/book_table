from django.http import JsonResponse

from django.views.generic import TemplateView, CreateView

from rest_framework.reverse import reverse_lazy

from booking.forms import BookingForm
from booking.models import Booking, Table


# Create your views here.
class MainView(TemplateView):
    template_name = "booking/main_page.html"


class AboutView(TemplateView):
    template_name = "booking/about.html"


class BookingView(CreateView):
    template_name = "booking/booking.html"
    model = Booking
    form_class = BookingForm
    success_url = reverse_lazy("booking:main")

    def form_valid(self, form):
        return super().form_valid(form)


def available_tables(request):
    date = request.GET.get("date")
    time = request.GET.get("time")
    quantity = request.GET.get("quantity")

    # Получение занятых столиков
    booked_tables = Booking.objects.filter(date=date, time=time).values_list(
        "table_id", flat=True
    )

    # Доступные столики
    tables = Table.objects.filter(capacity__gte=quantity)
    available = tables.exclude(id__in=booked_tables).order_by("id")

    tables_data = [{"id": table.pk, "number": table.number} for table in available]
    return JsonResponse(tables_data, safe=False)
