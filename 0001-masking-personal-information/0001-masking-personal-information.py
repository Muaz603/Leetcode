class Solution:
    def maskPII(self, s: str) -> str:
        # Email
        if '@' in s:
            name, domain = s.split('@')
            name = name.lower()
            domain = domain.lower()

            return name[0] + "*****" + name[-1] + "@" + domain

        # Phone
        digits = ''.join(ch for ch in s if ch.isdigit())

        country_code = len(digits) - 10
        last_four = digits[-4:]

        if country_code == 0:
            return "***-***-" + last_four

        return "+" + "*" * country_code + "-***-***-" + last_four

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna