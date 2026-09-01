class Solution:
    def finalPrices(self, prices):
        stack = []

        for i in range(len(prices) - 1, -1, -1):
            price = prices[i]

            while stack and stack[-1] > price:
                stack.pop()

            if stack:
                prices[i] = price - stack[-1]

            stack.append(price)

        return prices

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna