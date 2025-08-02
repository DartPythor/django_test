from django.urls import path

from vehicle.views import (
    VehicleTypeCreateView,
    VehicleTypeUpdateView,
    VehicleTypeListView,
VehicleTypeDeleteView,
)

app_name = "vehicle"
urlpatterns = [
    path(
        "vehicle-types/create",
        VehicleTypeCreateView.as_view(),
        name="vehicle_type_create",
    ),
    path(
        "vehicle-types/<int:pk>",
        VehicleTypeUpdateView.as_view(),
        name="vehicle_type_read_update",
    ),
    path(
        "vehicle-types",
        VehicleTypeListView.as_view(),
        name="vehicle_type_list",
    ),
    path(
        "vehicle-types/<int:pk>/delete",
        VehicleTypeDeleteView.as_view(),
        name="vehicle_type_delete",
    ),
]
