
document.addEventListener("DOMContentLoaded", function () {

    async function updateLiveDashboard() {

        try {
            const response = await fetch("/api/live-queue", {
                cache: "no-store"
            });

            if (!response.ok) {
                throw new Error("Unable to fetch live queue data");
            }

            const data = await response.json();

            const waitingElement =
                document.querySelector("[data-live-waiting]");

            const servingElement =
                document.querySelector("[data-live-serving]");

            const completedElement =
                document.querySelector("[data-live-completed]");

            const totalElement =
                document.querySelector("[data-live-total]");

            if (waitingElement) {
                waitingElement.textContent = data.waiting;
            }

            if (servingElement) {
                servingElement.textContent = data.serving;
            }

            if (completedElement) {
                completedElement.textContent = data.completed;
            }

            if (totalElement) {
                totalElement.textContent = data.total;
            }

            const updateTime =
                document.getElementById("liveUpdateTime");

            if (updateTime) {
                updateTime.textContent =
                    "Last updated: " + new Date().toLocaleTimeString();
            }

        } catch (error) {
            console.error("Live dashboard update:", error);
        }
    }

    updateLiveDashboard();

    setInterval(updateLiveDashboard, 5000);

});
