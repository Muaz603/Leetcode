from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):

        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        start_r = 0
        start_c = 0

        count = 0

        for r in range(m):
            for c in range(n):

                if classroom[r][c] == 'S':
                    start_r = r
                    start_c = c

                elif classroom[r][c] == 'L':
                    litter[(r, c)] = count
                    count += 1

        if count == 0:
            return 0

        full_mask = (1 << count) - 1

        queue = deque()
        queue.append((start_r, start_c, energy, 0))

        # best[(r, c, mask)] = maximum energy
        best = {}

        best[(start_r, start_c, 0)] = energy

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        moves = 0

        while queue:

            size = len(queue)

            for _ in range(size):

                r, c, e, mask = queue.popleft()

                if mask == full_mask:
                    return moves

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        index = litter[(nr, nc)]
                        nmask |= (1 << index)

                    # Reset energy
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    state = (nr, nc, nmask)

                    # If we have already reached this state
                    # with equal or greater energy, skip it.
                    if state in best and best[state] >= ne:
                        continue

                    best[state] = ne
                    queue.append((nr, nc, ne, nmask))

            moves += 1

        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna