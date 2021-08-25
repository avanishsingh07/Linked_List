    def reverseLL(self):
        previous = None
        current = self.head
        if current is None:
            return

        while current is not None:
            next = current.next
            current.next = previous
            previous = next
            current = next

        self.head = previous
