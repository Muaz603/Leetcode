class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        ans = 0

        for num in nums:
            if num == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0

        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna