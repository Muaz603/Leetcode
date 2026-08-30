class Solution(object):
    def oddEvenList(self, head):

        if not head or not head.next:
            return head

        odd = head
        even = head.next

        # Save the start of even list
        evenHead = even

        while even and even.next:

            # Connect odd nodes
            odd.next = even.next
            odd = odd.next

            # Connect even nodes
            even.next = odd.next
            even = even.next

        # Attach even list after odd list
        odd.next = evenHead

        return head

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna