document.addEventListener('DOMContentLoaded', () => {
    // Select all elements with animation classes
    const animatedElements = document.querySelectorAll('.fade-in, .fade-up');

    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.1 // Trigger when 10% of element is visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, observerOptions);

    animatedElements.forEach(el => observer.observe(el));
    
    // Console Hello
    console.log("Developed by Muddam Karthik - 2025");
});