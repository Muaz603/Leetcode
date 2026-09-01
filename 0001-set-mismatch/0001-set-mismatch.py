class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        count = [0] * (n + 1)

        for num in nums:
            count[num] += 1

        duplicate = missing = 0

        for i in range(1, n + 1):
            if count[i] == 2:
                duplicate = i
            elif count[i] == 0:
                missing = i

        return [duplicate, missing]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna