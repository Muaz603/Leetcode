class Solution(object):
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        if min_index > max_index:
            min_index, max_index = max_index, min_index

        from_front = max_index + 1

        from_back = n - min_index

        from_both = (min_index + 1) + (n - max_index)

        return min(from_front, from_back, from_both)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna