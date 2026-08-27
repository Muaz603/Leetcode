class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            num = total

        return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna