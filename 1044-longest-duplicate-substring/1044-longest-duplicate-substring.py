class Solution(object):
    def longestDupSubstring(self, s):
        n = len(s)
        base = 26
        mod = 2**63 - 1

        def search(length):
            if length == 0:
                return ""

            h = 0
            power = pow(base, length - 1, mod)

            for i in range(length):
                h = (h * base + (ord(s[i]) - ord('a'))) % mod

            seen = {h: 0}

            for i in range(1, n - length + 1):
                h = (
                    (h - (ord(s[i - 1]) - ord('a')) * power) * base
                    + (ord(s[i + length - 1]) - ord('a'))
                ) % mod

                if h in seen:
                    start = seen[h]

                    if s[start:start + length] == s[i:i + length]:
                        return s[i:i + length]

                seen[h] = i

            return ""

        left = 1
        right = n - 1
        answer = ""

        while left <= right:
            mid = (left + right) // 2

            duplicate = search(mid)

            if duplicate:
                answer = duplicate
                left = mid + 1
            else:
                right = mid - 1

        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna