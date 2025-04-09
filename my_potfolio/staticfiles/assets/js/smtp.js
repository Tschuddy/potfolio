document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.php-email-form');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(form);
        const loading = form.querySelector('.loading');
        const errorMessage = form.querySelector('.error-message');
        const sentMessage = form.querySelector('.sent-message');
        
        // Show loading, hide others
        loading.style.display = 'block';
        errorMessage.style.display = 'none';
        sentMessage.style.display = 'none';
        
        fetch(form.action, {
            method: form.method,
            body: formData
        })
        .then(response => {
            loading.style.display = 'none';
            
            if (response.ok) {
                return response.text();
            } else {
                throw new Error('Network response was not ok');
            }
        })
        .then(data => {
            sentMessage.textContent = data;
            sentMessage.style.display = 'block';
            form.reset();
        })
        .catch(error => {
            loading.style.display = 'none';
            errorMessage.textContent = 'Error sending message. Please try again later.';
            errorMessage.style.display = 'block';
        });
    });
});