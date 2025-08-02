from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from vehicle.models import VehicleType

class VehicleTypeCreateView(CreateView):
    template_name = "vehicle/vehicletype_form.html"
    model = VehicleType
    fields = ["name"]
    success_url = reverse_lazy("vehicle:vehicle_type_create")


class VehicleTypeUpdateView(UpdateView):
    template_name = "vehicle/vehicletype_edit_form.html"
    model = VehicleType
    fields = ["name"]
    success_url = reverse_lazy("vehicle_type_list")

    def get_success_url(self):
        return reverse("vehicle:vehicle_type_read_update", args=(self.object.pk,))


class VehicleTypeListView(ListView):
    template_name = "vehicle/vehicletype_list.html"
    paginate_by = 15
    model = VehicleType


class VehicleTypeDeleteView(DeleteView):
    model = VehicleType
    success_url = reverse_lazy("vehicle:vehicle_type_list")
