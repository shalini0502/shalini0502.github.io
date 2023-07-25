document.getElementById('convertForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.getElementById('handwritingImage');

    if (fileInput.files.length > 0) {
        formData.append('handwritingImage', fileInput.files[0]);

        fetch('/convert', {
            method: 'POST',
            body: formData
        })
        .then(response => response.text())
        .then(text => {
            const outputDiv = document.getElementById('outputText');
            outputDiv.textContent = text;
        })
        .catch(error => console.error('Error:', error));
    }
});
