class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        first = len(s) % k
        result = []

        if first:
            result.append(s[:first])

        for i in range(first, len(s), k):
            result.append(s[i:i + k])

        return "-".join(result)
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna