class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        time = 0

        for i in range(len(tickets)):
            if i <= k:
                time += min(tickets[i], target)
            else:
                time += min(tickets[i], target - 1)

        return time

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna