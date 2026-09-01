class Solution:
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prevTime = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":

                if stack:
                    result[stack[-1]] += time - prevTime

                stack.append(fid)
                prevTime = time

            else:

                result[stack[-1]] += time - prevTime + 1
                stack.pop()
                prevTime = time + 1

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna