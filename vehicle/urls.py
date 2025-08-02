from django.urls import path

from vehicle.views import VehicleTypeCreateView

app_name = "vehicle"
urlpatterns = [
    path(
        "/vehicle-types/create/",
        VehicleTypeCreateView.as_view(),
        name="vehicle_type_create",
    ),
]
