from django.contrib import admin

from booking.models import Booking, Table


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["table", "customer", "date", "time"]

    class Meta:
        model = Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    class Meta:
        model = Table
