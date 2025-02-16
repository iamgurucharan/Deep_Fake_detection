// Add interactivity for file upload
document.addEventListener('DOMContentLoaded', function () {
    const fileInput = document.querySelector('input[type="file"]');
    const uploadLabel = document.querySelector('.upload-section label');

    if (fileInput && uploadLabel) {
        fileInput.addEventListener('change', function () {
            if (fileInput.files.length > 0) {
                uploadLabel.textContent = fileInput.files[0].name;
                uploadLabel.style.backgroundColor = '#00cc66';
            } else {
                uploadLabel.textContent = 'Choose a Video File';
                uploadLabel.style.backgroundColor = '#00ff88';
            }
        });
    }

    // Add smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});