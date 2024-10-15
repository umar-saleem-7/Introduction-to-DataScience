// Wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', function () {
    // Get the form element
    const contactForm = document.querySelector('.contact-form');

    // Add event listener to the form on submit
    contactForm.addEventListener('submit', function (event) {
        // Prevent the default form submission behavior
        event.preventDefault();

        // Get the values of the form fields
        const name = contactForm.querySelector('input[type="text"]').value;
        const email = contactForm.querySelector('input[type="email"]').value;
        const message = contactForm.querySelector('textarea').value;

        // Basic form validation
        if (name === '' || email === '' || message === '') {
            alert('Please fill out all fields.');
        } else {
            // Simulate successful form submission (you can replace this with an actual back-end submission)
            alert('Thank you for reaching out! Your message has been sent.');

            // Reset the form fields
            contactForm.reset();
        }
    });
});
