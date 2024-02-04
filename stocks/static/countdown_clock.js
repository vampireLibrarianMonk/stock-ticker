document.addEventListener('DOMContentLoaded', function() {
    function updateCountdown() {
        const now = new Date();
        const est = new Date(now.toLocaleString("en-US", {timeZone: "America/New_York"}));

        // Calculate the target time for 9:30 AM EST
        const marketOpenEST = new Date(est);
        marketOpenEST.setHours(9, 30, 0, 0); // Market opens at 9:30 AM EST

        // Adjust for the next day if the current time is past 9:30 AM EST
        if (est > marketOpenEST) {
            marketOpenEST.setDate(marketOpenEST.getDate() + 1);
        }

        // Function to format the countdown string
        function formatCountdown(timeDifference) {
            const diff = marketOpenEST - est + timeDifference;

            // Avoid negative countdown (for past times)
            if (diff < 0) {
                return "Market Open";
            }

            // Convert the difference to hours, minutes, and seconds
            let hours = Math.floor(diff / (1000 * 60 * 60));
            let minutes = Math.floor((diff / (1000 * 60)) % 60);
            let seconds = Math.floor((diff / 1000) % 60);

            // Format numbers to have at least two digits
            hours = hours < 10 ? '0' + hours : hours;
            minutes = minutes < 10 ? '0' + minutes : minutes;
            seconds = seconds < 10 ? '0' + seconds : seconds;

            return `${hours}:${minutes}:${seconds}`;
        }

        // Calculate time differences from EST to CST, PST, and UTC
        const timeDiffCST = -1 * 60 * 60 * 1000; // 1 hour behind EST
        const timeDiffPST = -3 * 60 * 60 * 1000; // 3 hours behind EST
        const timeDiffUTC = 5 * 60 * 60 * 1000; // UTC is 5 hours ahead of EST (not considering DST)

        // Update the countdown for each time zone
        const countdownString = `Market Opens In -> EST: ${formatCountdown(0)} | CST: ${formatCountdown(timeDiffCST)} | PST: ${formatCountdown(timeDiffPST)} | UTC: ${formatCountdown(timeDiffUTC)}`;

        // Display the countdown
        const countdownElement = document.getElementById('marketCountdown');
        if (countdownElement) {
            countdownElement.textContent = countdownString;
        }

        // Update the countdown every second
        setTimeout(updateCountdown, 1000);
    }

    // Initialize the countdown
    updateCountdown();
});
