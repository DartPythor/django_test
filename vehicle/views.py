from django.db import transaction
from django.views.generic.detail import DetailView
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

    def get_success_url(self):
        return reverse("vehicle:vehicle_type_read_update", args=(self.object.pk,))


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
    queryset = VehicleType.objects.filter(is_deleted=False)


class VehicleTypeDeleteView(DeleteView):
    model = VehicleType
    success_url = reverse_lazy("vehicle:vehicle_type_list")

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.is_deleted = True
            self.object.save()

            vehicles = Vehicle.objects.filter(type=self.object)
            vehicles.update(is_deleted=True)
            VehicleImage.objects.filter(vehicle__in=vehicles).update(is_deleted=True)

        return HttpResponseRedirect(success_url)


class VehicleCreateView(CreateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle/vehicle_form.html"
    success_url = reverse_lazy("vehicle:vehicle_list")

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
        with transaction.atomic():
            for photo in filter(lambda x: x is not None, all_photo):
                VehicleImage.objects.create(vehicle=self.object, file=photo)

        return response


class VehicleUpdateView(UpdateView):
    model = Vehicle
    form_class = VehicleForm
    template_name = "vehicle/vehicle_form.html"
    queryset = Vehicle.with_images.all()

    def get_success_url(self):
        return reverse("vehicle:vehicle_update", args=(self.object.pk,))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        context["existing_photos"] = self.object.images.all()
        return context

    def form_valid(self, form):
        delete_photos = self.request.POST.getlist("delete_photos")

        response = super().form_valid(form)

        all_photo = [
            self.request.FILES.get("photo1", None),
            self.request.FILES.get("photo2", None),
            self.request.FILES.get("photo3", None),
        ]
        with transaction.atomic():
            if delete_photos:
                VehicleImage.objects.filter(
                    id__in=delete_photos,
                    vehicle=self.object
                ).delete()

            for photo in filter(lambda x: x is not None, all_photo):
                VehicleImage.objects.create(vehicle=self.object, file=photo)

        return response


class VehicleListView(ListView):
    template_name = "vehicle/vehicle_list.html"
    paginate_by = 15
    model = Vehicle
    queryset = Vehicle.with_images.get_active_query()

    def get_queryset(self):
        queryset = super().get_queryset()
        brand = self.request.GET.get("brand")

        if brand:
            return queryset.filter(brand__icontains=brand)

        return queryset


class VehicleDeleteView(DeleteView):
    model = Vehicle
    success_url = reverse_lazy("vehicle:vehicle_list")

    def post(self, request, *args, **kwargs):
        with transaction.atomic():
            self.object = self.get_object()
            success_url = self.get_success_url()
            self.object.is_deleted = True
            self.object.save()
            self.object.images.update(is_deleted=True)
        return HttpResponseRedirect(success_url)


class VehicleDetailView(DetailView):
    model = Vehicle
    template_name = "vehicle/vehicle_detail.html"
    queryset = Vehicle.with_images.all()
