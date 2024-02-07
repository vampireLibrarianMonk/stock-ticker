document.addEventListener('DOMContentLoaded', function() {
    // Main function to update the countdown timer
    function updateCountdown() {
        const now = new Date();
        const est = new Date(now.toLocaleString("en-US", {timeZone: "America/New_York"})); // Current time in EST

        // Calculate the target time for 9:30 AM EST, marking the market opening
        const marketOpenEST = new Date(est);
        marketOpenEST.setHours(9, 30, 0, 0); // Sets the opening time to 9:30 AM EST

        // Adjust for the next day if current time is past today's market opening
        if (est > marketOpenEST) {
            marketOpenEST.setDate(marketOpenEST.getDate() + 1); // Move to the next day
        }

        // Formats the countdown time as a string
        function formatCountdown(timeDifference) {
            const diff = marketOpenEST - est + timeDifference; // Calculates time difference including adjustments

            // Handle cases where the countdown would otherwise be negative
            if (diff < 0) {
                return "Market Open"; // Indicates the market is currently open
            }

            // Breakdown the difference into hours, minutes, and seconds
            let hours = Math.floor(diff / (1000 * 60 * 60));
            let minutes = Math.floor((diff / (1000 * 60)) % 60);
            let seconds = Math.floor((diff / 1000) % 60);

            // Ensures two-digit formatting for each time component
            hours = hours < 10 ? '0' + hours : hours;
            minutes = minutes < 10 ? '0' + minutes : minutes;
            seconds = seconds < 10 ? '0' + seconds : seconds;

            return `${hours}:${minutes}:${seconds}`; // Returns the formatted string
        }

        // Time differences for CST, PST, and UTC relative to EST
        const timeDiffCST = -1 * 60 * 60 * 1000; // CST is 1 hour behind EST
        const timeDiffPST = -3 * 60 * 60 * 1000; // PST is 3 hours behind EST
        const timeDiffUTC = 5 * 60 * 60 * 1000; // UTC is 5 hours ahead of EST (not accounting for DST)

        // Generates the countdown string for each timezone
        const countdownString = `Market Opens In ->
         EST: ${formatCountdown(0)} |
         CST: ${formatCountdown(timeDiffCST)} |
         PST: ${formatCountdown(timeDiffPST)} |
         UTC: ${formatCountdown(timeDiffUTC)}`;

        // Finds and updates the HTML element displaying the countdown
        const countdownElement = document.getElementById('marketCountdown');
        if (countdownElement) {
            countdownElement.textContent = countdownString; // Updates the displayed countdown
        }

        // Re-trigger the countdown every second for real-time updates
        setTimeout(updateCountdown, 1000);
    }

    // Calls the countdown function initially to start the process
    updateCountdown();
});