import * as bootstrap from 'bootstrap'

const previewEntryButton = document.querySelector('#btn-preview-entry');
const previewModal = new bootstrap.Modal(document.getElementById('entry-preview-modal'));
const previewModalHeading = document.querySelector('#entry-preview-modal .modal-body #date');
const previewModalBody = document.querySelector('#entry-preview-modal .modal-body #body');

previewEntryButton.addEventListener('click', () => {
    const body = document.querySelector('#id_body').value;
    const date = document.querySelector('#id_date_published').value;

    const params = new URLSearchParams({
        body,
        date
    });

    const url = `/entries/preview/?${params.toString()}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            previewModalHeading.innerHTML = data.title;
            previewModalBody.innerHTML = data.body;
            previewModal.show();
        });
});
