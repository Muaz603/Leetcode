class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        maxArea = 0

        for i in range(len(heights) + 1):
            curr = 0 if i == len(heights) else heights[i]

            while stack and curr < heights[stack[-1]]:
                h = heights[stack.pop()]
                left = stack[-1] if stack else -1
                width = i - left - 1
                maxArea = max(maxArea, h * width)

            stack.append(i)

        return maxArea

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna