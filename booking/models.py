from django.db import models


class Table(models.Model):
    """Модель стола в ресторане"""

    CLASSES = (
        ("Common", "Обычный"),
        ("Vip", "VIP"),
    )

    number = models.PositiveIntegerField(
        unique=True, verbose_name="Номер столика", db_index=True
    )
    capacity = models.PositiveSmallIntegerField(verbose_name="Вместимость")
    type_table = models.CharField(choices=CLASSES, verbose_name="Тип столика")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.number}-{self.type_table}"

    class Meta:
        verbose_name = "Столик"
        verbose_name_plural = "Столики"
        ordering = ["-number"]


class Booking(models.Model):
    """Модель бронирования в ресторане"""

    STATUSES = [
        ("Open", "Открыта"),
        ("Confirmed", "Подтверждена"),
        ("Closed", "Закрыта"),
        ("Cancelled", "Отменена"),
    ]
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)

    quantity = models.PositiveSmallIntegerField("Количество гостей", default=1)
    date = models.DateField(verbose_name="Дата")
    time_from = models.TimeField(verbose_name="Время начала")
    time_to = models.TimeField(verbose_name="Время окончания")

    customer = models.CharField(max_length=50, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    comment = models.CharField(
        max_length=255, verbose_name="Пожелания", null=True, blank=True
    )

    price = models.PositiveIntegerField(verbose_name="Стоимость", default=0)
    status = models.CharField(choices=STATUSES, verbose_name="Статус")

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.table}-{self.date}-{self.time_from}-{self.time_to}"

    class Meta:
        verbose_name = "Бронь"
        verbose_name_plural = "Брони"
        ordering = ["-created_at"]
