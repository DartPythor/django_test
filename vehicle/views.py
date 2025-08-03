from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from vehicle.forms import VehicleForm
from vehicle.models import Vehicle, VehicleImage, VehicleType


class VehicleTypeCreateView(CreateView):
    template_name = "vehicle/vehicletype_form.html"
    model = VehicleType
    fields = ["name"]
    success_url = reverse_lazy("vehicle:vehicle_type_create")


class VehicleTypeUpdateView(UpdateView):
    template_name = "vehicle/vehicletype_form.html"
    model = VehicleType
    fields = ["name"]

    def get_success_url(self):
        return reverse("vehicle:vehicle_type_read_update", args=(self.object.pk,))


class VehicleTypeListView(ListView):
    template_name = "vehicle/vehicletype_list.html"
    paginate_by = 15
    model = VehicleType


class VehicleTypeDeleteView(DeleteView):
    model = VehicleType
    success_url = reverse_lazy("vehicle:vehicle_type_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle/vehicle_form.html"
    success_url = reverse_lazy("vehicle:vehicle_type_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = False
        context["existing_photos"] = []
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

        all_photo = [
            self.request.FILES.get("photo1", None),
            self.request.FILES.get("photo2", None),
            self.request.FILES.get("photo3", None),
        ]
        for photo in filter(lambda x: x is not None, all_photo):
            VehicleImage.objects.create(vehicle=self.object, file=photo)

        return response


class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle/vehicle_form.html"

    def get_success_url(self):
        return reverse("vehicle:vehicle_update", args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        context["existing_photos"] = self.object.images.all()
        return context

    def form_valid(self, form):
        delete_photos = self.request.POST.getlist("delete_photos")
        if delete_photos:
            VehicleImage.objects.filter(
                id__in=delete_photos,
                vehicle=self.object
            ).delete()

        return super().form_valid(form)
