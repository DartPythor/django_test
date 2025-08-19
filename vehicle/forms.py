from django import forms
from vehicle.models import Vehicle


class VehicleForm(forms.ModelForm):
    photos = forms.ImageField(
        label="Добавить фото",
        widget=forms.ClearableFileInput(),
        required=False,
    )

    class Meta:
        model = Vehicle
        fields = [
            "reg_number",
            "brand",
            "date_purchase",
            "type",
            "mileage",
            "operation_status",
        ]
        widgets = {
            "date_purchase": forms.DateInput(attrs={"type": "date"}),
        }
        labels = {
            "reg_number": "Регистрационный номер",
            "brand": "Марка техники",
            "date_purchase": "Дата приобретения",
            "type": "Тип техники",
            "mileage": "Пробег (км)",
            "operation_status": "Текущий статус",
        }
