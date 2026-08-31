class Solution(object):
    def evalRPN(self, tokens):

        stack = []

        for token in tokens:

            # If token is a number
            if token not in "+-*/":
                stack.append(int(token))
                continue

            # If token is an operator
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b

            elif token == "-":
                result = a - b

            elif token == "*":
                result = a * b

            else:
                # Division should truncate toward zero
                result = abs(a) // abs(b)

                if (a < 0) != (b < 0):
                    result = -result

            stack.append(result)

        return stack[-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna