document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.delete-icon');
    const deleteModal = new bootstrap.Modal(document.getElementById('confirmDeleteModal'));
    let currentPhotoId, currentPhotoElement;

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            currentPhotoId = this.dataset.photoId;
            currentPhotoElement = this.closest('.image-item');

            document.getElementById('imageToDeleteName').textContent =
                this.dataset.photoName;

            deleteModal.show();
        });
    });

    document.getElementById('confirmDeleteBtn').addEventListener('click', function() {
        const deleteInput = document.createElement('input');
        deleteInput.type = 'hidden';
        deleteInput.name = 'delete_photos';
        deleteInput.value = currentPhotoId;

        document.querySelector('form').appendChild(deleteInput);

        currentPhotoElement.remove();

        deleteModal.hide();
    });
});