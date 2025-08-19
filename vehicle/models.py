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


class VehicleManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("type").prefetch_related("images")

    def get_active_query(self):
        return (
            super()
            .get_queryset()
            .select_related("type")
            .prefetch_related("images")
            .filter(is_deleted=False)
        )


class VehicleType(IsDeleteCreate):
    name = models.CharField(
        max_length=255,
        help_text="Название типа.",
        unique=True,
    )

    def __str__(self):
        return f"Тип техники: {self.name}"

    class Meta:
        verbose_name = "Тип техники"
        verbose_name_plural = "Типы техники"


class Vehicle(IsDeleteCreate):
    OPERATIONS_STATUS_CHOICES = [
        ("in_work", "В работе"),
        ("unuse", "Простой"),
        ("repair", "Ремонт"),
    ]

    with_images = VehicleManager()

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
        max_length=7,
    )

    def __str__(self):
        return f"Техника: {self.brand} - {self.reg_number}"

    class Meta:
        verbose_name = "Техника"
        verbose_name_plural = "Техника"


class VehicleImage(IsDeleteCreate):
    file = ImageField(
        upload_to="vehicle_images/",
        help_text="Загрузка изображения для техники.",
    )
    vehicle = models.ForeignKey(
        Vehicle,
        related_name="images",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return "Изображение техники"

    class Meta:
        verbose_name = "Изображение техники"
        verbose_name_plural = "Изображения техники"
