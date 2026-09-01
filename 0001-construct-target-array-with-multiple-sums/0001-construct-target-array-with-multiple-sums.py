import heapq

class Solution:
    def isPossible(self, target: List[int]) -> bool:
        total = sum(target)

        # Python has a min heap, so store negative values
        heap = [-x for x in target]
        heapq.heapify(heap)

        while True:
            largest = -heapq.heappop(heap)
            rest = total - largest

            # Already reached the starting array
            if largest == 1 or rest == 1:
                return True

            # Invalid state
            if rest == 0 or largest <= rest:
                return False

            # Reverse multiple operations at once
            previous = largest % rest

            if previous == 0:
                return False

            total = rest + previous

            heapq.heappush(heap, -previous)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna