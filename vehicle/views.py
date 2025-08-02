from django.views.generic.edit import CreateView

from vehicle.models import VehicleType


class VehicleTypeCreateView(CreateView):
    template_name = "vehicle/vehicletype_form.html"
    model = VehicleType
    fields = ["name"]
