class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return (
            word.isupper()
            or word.islower()
            or word[0].isupper() and word[1:].islower()
        )

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna