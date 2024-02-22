document.addEventListener('DOMContentLoaded', function() {
    function updateCountdown() {
        const now = new Date();
        // Adjust 'now' to EST timezone
        const est = new Date(now.toLocaleString("en-US", {timeZone: "America/New_York"}));

        // For testing purposes only
//        est.setHours(est.getHours() - 3);

        // Initialize market opening and closing times in EST
        const marketOpenEST = new Date(est);
        marketOpenEST.setHours(9, 30, 0, 0); // Market opens at 9:30 AM EST

        const marketCloseEST = new Date(est);
        marketCloseEST.setHours(16, 0, 0, 0); // Market closes at 4:00 PM EST

        // Determine whether we're counting down to market open or close
        let targetTimeEST, countdownMessage;
        if (est < marketOpenEST) {
            targetTimeEST = marketOpenEST;
            countdownMessage = "Market Opens In ->";
        } else if (est >= marketOpenEST && est < marketCloseEST) {
            targetTimeEST = marketCloseEST;
            countdownMessage = "Market Closes In ->";
        } else {
            // Adjust for the next market day if current time is past today's market closing
            marketOpenEST.setDate(marketOpenEST.getDate() + 1);
            targetTimeEST = marketOpenEST;
            countdownMessage = "Market Opens In ->";
        }

        // Function to format the countdown time, adjusting for different time zones
        function formatCountdown(targetTime, timeDiff) {
            const adjustedTargetTime = new Date(targetTime.getTime() + timeDiff);
            const diff = adjustedTargetTime - est; // Difference in milliseconds

            // Use the Date object to handle the countdown time
            const countdownTime = new Date(diff);

            // Since the Date object 'countdownTime' is based on epoch time (1970-01-01),
            // directly using getHours(), getMinutes(), and getSeconds() won't give correct countdown time directly.
            // Instead, calculate hours, minutes, and seconds considering the diff might not represent an actual 'time of day'.
            let hours = Math.floor(diff / (1000 * 60 * 60));
            let minutes = countdownTime.getUTCMinutes();
            let seconds = countdownTime.getUTCSeconds();

            // Adjust hours to handle negative values by subtracting from 24
            if (hours < 0) {
                hours = 0 - hours; // Convert negative hours to a countdown format from 24
            }

            // Formatting for leading zeros
            hours = hours < 10 ? '0' + hours : hours.toString();
            minutes = minutes < 10 ? '0' + minutes : minutes.toString();
            seconds = seconds < 10 ? '0' + seconds : seconds.toString();

            return `${hours}:${minutes}:${seconds}`;
        }

        // Time differences for CST, PST, and UTC relative to EST
        const timeDiffCST = -1 * 60 * 60 * 1000; // CST is 1 hour behind EST
        const timeDiffMST = -2 * 60 * 60 * 1000; // MST is 2 hour behind EST
        const timeDiffPST = -3 * 60 * 60 * 1000; // PST is 3 hours behind EST
        const timeDiffUTC = 5 * 60 * 60 * 1000; // UTC is 5 hours ahead of EST

        // Generates the countdown string for each timezone
        const countdownString = `${countdownMessage}
         EST: ${formatCountdown(targetTimeEST, 0)}`;

        // Update the countdown display
        const countdownElement = document.getElementById('marketCountdown');
        if (countdownElement) {
            countdownElement.textContent = countdownString;
        }

        // Re-trigger the countdown every second
        setTimeout(updateCountdown, 1000);
    }

    updateCountdown();
});
