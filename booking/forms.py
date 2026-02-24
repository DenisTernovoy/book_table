from django import forms
from datetime import datetime, time

from django.core.exceptions import ValidationError

from booking.models import Booking
from config.forms import StyleFormMixin


class BookingForm(StyleFormMixin, forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.today = datetime.now()
        self.fields["table"].widget.attrs.update({"placeholder": "Выберите дату"})
        self.fields["date"].widget.attrs.update(
            {"min": self.today.date().replace(day=self.today.day + 1)}
        )
        self.fields["quantity"].widget.attrs.update({"min": 2})

    min_time = time(11, 0)  # 11:00
    max_time = time(20, 0)  # 20:00

    # Генерация списка времени с интервалом в 1 час
    time_options = []
    current_time = min_time
    while current_time <= max_time:
        time_options.append(
            (
                current_time.strftime("%H:%M"),  # Значение для <option>
                current_time.strftime("%H:%M"),  # Текст для отображения
            )
        )
        # Добавляем 1 час
        current_time = current_time.replace(hour=current_time.hour + 1)

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control",
                "style": "width:207px",
            }
        ),
        input_formats=["%Y-%m-%d"],
        label="Дата",
    )

    time = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                "type": "select",
                "class": "form-control",
                "style": "width:207px",
                "placeholder": "Выберите время",  # Плейсхолдер для Bootstrap
            }
        ),
        label="Дата",
        choices=time_options,
    )

    class Meta:
        model = Booking
        fields = [
            "table",
            "quantity",
            "date",
            "time",
            "customer",
            "phone",
            "comment",
        ]

    def clean_table(self):
        table = self.cleaned_data["table"]
        if not table:
            raise ValidationError("введите столик")

        return table
