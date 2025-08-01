import decimal

from django.db import models
from django.core.validators import MinValueValidator
from sorl.thumbnail import ImageField


class IsDeleteCreate(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата создания.",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Дата обновления.",
    )
    is_deleted = models.BooleanField(
        default=False,
        help_text="Логическое удаление.",
    )

    class Meta:
        abstract = True


class VehicleType(IsDeleteCreate):
    name = models.CharField(
        max_length=255,
        help_text="Название типа.",
    )


class Vehicle(IsDeleteCreate):
    OPERATIONS_STATUS_CHOICES = [
        ("in_work", "В работе"),
        ("unuse", "Простой"),
        ("repair", "Ремонт"),
    ]

    reg_number = models.CharField(
        max_length=255,
        help_text="Регистрационный номер.",
    )
    brand = models.CharField(
        max_length=255,
        help_text="Марка.",
    )
    date_purchase = models.DateField(
        help_text="Дата покупки.",
    )
    type = models.ForeignKey(
        VehicleType,
        on_delete=models.CASCADE,
        help_text="Тип техники.",
    )
    mileage = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        help_text="Пробег.",
        validators=[MinValueValidator(decimal.Decimal("0.000"))],
    )
    operation_status = models.CharField(
        choices=OPERATIONS_STATUS_CHOICES,
        max_length=6,
    )


class VehicleImage(IsDeleteCreate):
    file = ImageField(upload_to="vehicle_images/")
    vehicle = models.ForeignKey(
        Vehicle,
        related_name="images",
        on_delete=models.CASCADE,
    )
