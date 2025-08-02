document.addEventListener("DOMContentLoaded", function () {
  const deleteModalEl = document.getElementById("confirmDeleteModal");
  const deleteModal = new bootstrap.Modal(deleteModalEl);

  let imageToDelete = null;

  const imageNameElem = deleteModalEl.querySelector("#imageToDeleteName");

  const deleteIcons = document.querySelectorAll('.image-item .delete-icon');

  deleteIcons.forEach((icon, index) => {
    icon.addEventListener('click', () => {
      const imageItem = icon.closest('.image-item');
      const name = imageItem.dataset.imageName || `#${index + 1}`;
      imageToDelete = imageItem;
      imageNameElem.textContent = name;
      deleteModal.show();
    });
  });

  const confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
  confirmDeleteBtn.addEventListener('click', () => {
    if (imageToDelete) {
      imageToDelete.remove();
      imageToDelete = null;
    }
    deleteModal.hide();
  });
});
