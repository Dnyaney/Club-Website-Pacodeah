document.addEventListener('DOMContentLoaded', () => {
    const body = document.body;
    const targetUrl = body.getAttribute('data-target-url');

    // Ensure the URL exists before trying to redirect
    if (targetUrl) {
        setTimeout(() => {
            window.location.href = targetUrl;
        }, 3000); 
    } else {
        console.error("Target URL not found on body data-target-url attribute.");
    }
});