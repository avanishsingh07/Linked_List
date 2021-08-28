    def removeDuplicateElement(data):
        temp = data.head
        while temp.next is not None:
            if temp.data == temp.next.data:
                temp.next = temp.next.next

            else:
                temp = temp.next
