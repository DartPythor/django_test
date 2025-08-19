    document.addEventListener('DOMContentLoaded', function() {
        const deleteModal = document.getElementById('confirmDeleteModal');

        deleteModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget;
            const vehicleId = button.getAttribute('data-vehicle-id');
            const vehicleName = button.getAttribute('data-vehicle-name');

            document.getElementById('vehicleNameToDelete').textContent = vehicleName;
            document.getElementById('vehicleIdToDelete').value = vehicleId;
            document.getElementById('deleteForm').action = button.getAttribute('data-vehicle-url').replace('0', vehicleId);
        });
    });