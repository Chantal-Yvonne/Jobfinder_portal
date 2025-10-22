$(document).ready(function() {
    $("#contactForm").validate({
        rules: {
            name: {
                required: true,
                minlength: 2
            },
            email: {
                required: true,
                email: true
            },
            subject: {
                required: true,
                minlength: 4
            },
            message: {
                required: true,
                minlength: 10
            }
        },
        messages: {
            name: {
                required: "Please enter your name",
                minlength: "Name must be at least 2 characters"
            },
            email: {
                required: "Please enter your email address",
                email: "Enter a valid email"
            },
            subject: {
                required: "Please enter a subject",
                minlength: "Subject must be at least 4 characters"
            },
            message: {
                required: "Please enter your message",
                minlength: "Message must be at least 10 characters"
            }
        },
        submitHandler: function(form) {
            form.submit();
        }
    });
});
