class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        window = {}

        left = 0
        formed = 0
        required = len(need)

        min_len = float("inf")
        start = 0

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            # Character requirement is satisfied
            if ch in need and window[ch] == need[ch]:
                formed += 1

            # Current window is valid
            while formed == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # Remove left character
                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        return s[start:start + min_len]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna