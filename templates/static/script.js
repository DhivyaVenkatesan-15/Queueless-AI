
document.addEventListener("DOMContentLoaded", function () {

    // Automatically hide flash messages after 5 seconds.
    const alerts = document.querySelectorAll(".alert");

    alerts.forEach(function (alert) {
        setTimeout(function () {
            alert.style.transition = "opacity 0.5s ease";
            alert.style.opacity = "0";

            setTimeout(function () {
                alert.remove();
            }, 500);

        }, 5000);
    });

    // Confirm before performing admin queue operations.
    const operationForms = document.querySelectorAll(
        'form[action*="serve-next"], form[action*="complete-token"]'
    );

    operationForms.forEach(function (form) {
        form.addEventListener("submit", function (event) {
            const confirmed = window.confirm(
                "Are you sure you want to perform this queue operation?"
            );

            if (!confirmed) {
                event.preventDefault();
            }
        });
    });

});
