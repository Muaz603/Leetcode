class Solution(object):
    def repeatedStringMatch(self, a, b):
        repeated = ""
        count = 0

        while len(repeated) < len(b):
            repeated += a
            count += 1

        if b in repeated:
            return count

        repeated += a
        count += 1

        if b in repeated:
            return count

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna