from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        #points to most current node item
        self.storage = DoublyLinkedList()
        #WE can use self.storage.length

    def append(self, item):
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail 
        else:
            #Not at the end
            if self.current.next is not None:
                #change current.next.value = item
                self.current.next.value = item
                #Change new current
                self.current = self.current.next
            #current is last item
            else:
                #change head to new node
                self.storage.head.value = item
                #add to head, delete head's next
                self.current = self.storage.head

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        cur_node = self.storage.head
        while cur_node is not None:
            if cur_node.value is not None:
                list_buffer_contents.append(cur_node.value)
            cur_node = cur_node.next

        return list_buffer_contents

