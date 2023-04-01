
class LLNode:
    """Defines the value-containing node object for a linked list."""
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """Defines a linked list object, consisting of a linked set of LLNode objects."""

    def __init__(self):
        """Initializes a linked list to be empty."""
        self.first = None

    def prepend(self, value):
        """Adds a node with `value` to the front of a linked list."""
        newNode = LLNode(value)
        newNode.next = self.first
        self.first = newNode

    def append(self, value):
        "Adds a node with `value` to the end of a linked list."""
        if self.first is None:
            self.first = LLNode(value)
        else:
            current = self.first
            # Scan looking for the last node.
            while current.next is not None:
                current = current.next
            current.next = LLNode(value)

    def asString(self):
        """Returns a string that is the linked list's sequence."""
        if self.first is None:
            return "<>"
        else:
            s = "<" + str(self.first.value)
            current = self.first.next
            while current is not None:
                s = s + ", " + str(current.value)
                current = current.next
            s = s + ">"
            return s

    def delete(self, value):
        """Removes `value` from the linked list if there."""
        previous = None  # Track the node one behind.
        current  = self.first

        # If the linked list is empty, return None.
        if current is None:
            return None
        
        # Scan all the nodes looking for the value.
        while current.value != value:
            previous = current
            current = current.next
        # Stop scan when we've found it or scanned them all.
        if previous is None:  # If it was found at the front...
             # Remove from the front.
             self.first = current.next
        else:                 # If it was one of the later nodes...
             # Skip past it with the previous node's link.
             previous.next = current.next

    def __str__(self):
        return self.asString()

    def __repr__(self):
        return self.asString()

