from django import forms

from booking.models import Booking
from config.forms import StyleFormMixin


class BookingForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
