    document.addEventListener('DOMContentLoaded', function() {
        const deleteModal = document.getElementById('confirmDeleteModal');

        deleteModal.addEventListener('show.bs.modal', function(event) {
            const button = event.relatedTarget;
            const typeId = button.getAttribute('data-type-id');
            const typeName = button.getAttribute('data-type-name');

            document.getElementById('typeNameToDelete').textContent = typeName;
            document.getElementById('typeIdToDelete').value = typeId;
            document.getElementById('deleteForm').action = button.getAttribute('data-vehicle-url').replace('0', typeId);
        });
    });