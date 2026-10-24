"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self._items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # Adding at the end makes the newest item the next one removed.
        self._items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Return None when empty instead of raising IndexError.
        return self._items.pop() if not self.is_empty() else None

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Inspect the newest item without changing the stack.
        return self._items[-1] if not self.is_empty() else None

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._items) == 0

    def get_length(self):
        return len(self._items)


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Add at the back so older items stay ahead of newer items.
        self._items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Remove the oldest item; an empty queue returns None.
        return self._items.popleft() if not self.is_empty() else None

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Inspect the oldest item without removing it.
        return self._items[0] if not self.is_empty() else None

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._items) == 0

    def get_length(self):
        return len(self._items)


class SupportDesk:
    """Process tickets in arrival order and track action history for undo."""

    def __init__(self):
        self.ticket_queue = Queue()
        self.action_stack = Stack()

    def add_ticket(self, ticket):
        if not isinstance(ticket, str) or not ticket.strip():
            raise ValueError("Ticket must be a nonempty string.")
        self.ticket_queue.enqueue(ticket)

    def peek_next_ticket(self):
        if self.ticket_queue.is_empty():
            return "No tickets available."
        return self.ticket_queue.front()

    def process_next_ticket(self):
        if self.ticket_queue.is_empty():
            return "No tickets to process."
        ticket = self.ticket_queue.dequeue()
        self.action_stack.push(ticket)
        return ticket

    def undo_last_action(self):
        # Remove only the history entry; the waiting queue stays unchanged.
        if self.action_stack.is_empty():
            return "No actions to undo."
        return self.action_stack.pop()

    def get_pending_ticket_count(self):
        return self.ticket_queue.get_length()

    def get_action_history_size(self):
        return self.action_stack.get_length()


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO ===")
    stack = Stack()
    for value in (10, 20, 30, 40):
        stack.push(value)
        print(f"Push {value}: added to the top.")
    print(f"Peek: {stack.peek()} (the top item remains in the stack).")
    print("LIFO removal order (expected 40, 30, 20, 10):")
    while not stack.is_empty():
        print(f"Pop: {stack.pop()}")
    print(f"Pop on empty stack: {stack.pop()} (None means no item).")
    print(f"Peek on empty stack: {stack.peek()}.")
    stack.push(99)
    print(f"Single-item pop: {stack.pop()}; empty afterward: {stack.is_empty()}.")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO ===")
    queue = Queue()
    for value in (10, 20, 30, 40):
        queue.enqueue(value)
        print(f"Enqueue {value}: added to the back.")
    print(f"Front: {queue.front()} (the front item remains in the queue).")
    print("FIFO removal order (expected 10, 20, 30, 40):")
    while not queue.is_empty():
        print(f"Dequeue: {queue.dequeue()}")
    print(f"Dequeue on empty queue: {queue.dequeue()} (None means no item).")
    print(f"Front on empty queue: {queue.front()}.")
    queue.enqueue(99)
    print(f"Single-item dequeue: {queue.dequeue()}; empty afterward: {queue.is_empty()}.")

    # Real-world scenario: tickets wait in FIFO order; undo history uses LIFO.
    print("\n=== SUPPORT DESK SIMULATOR ===")
    desk = SupportDesk()
    for ticket in ("Reset password", "Install printer", "Update software"):
        desk.add_ticket(ticket)
    print(f"Pending tickets: {desk.get_pending_ticket_count()}")
    print(f"Next ticket (preview only): {desk.peek_next_ticket()}")
    print(f"Processed: {desk.process_next_ticket()}")
    print(f"Processed: {desk.process_next_ticket()}")
    print(f"Undo most recent history entry: {desk.undo_last_action()}")
    print("Undo removes the history entry; it does not requeue the ticket.")
    print(f"Pending tickets: {desk.get_pending_ticket_count()}")
    print(f"Next ticket: {desk.peek_next_ticket()}")
    print(f"Remaining history entries: {desk.get_action_history_size()}")


    # Additional edge cases beyond the starter: invalid input and empty history.
    print("\n=== SUPPORT DESK EDGE CASES ===")
    empty_desk = SupportDesk()
    print(f"Preview with no tickets: {empty_desk.peek_next_ticket()}")
    print(f"Process with no tickets: {empty_desk.process_next_ticket()}")
    print(f"Undo with no history: {empty_desk.undo_last_action()}")
    for invalid_ticket in (None, "", "   ", 42):
        try:
            empty_desk.add_ticket(invalid_ticket)
        except ValueError as error:
            print(f"Rejected {invalid_ticket!r}: {error}")
    print(f"Pending after invalid inputs: {empty_desk.get_pending_ticket_count()}")

    # Repeated previews must leave the queue unchanged.
    empty_desk.add_ticket("Check network connection")
    print(f"First preview: {empty_desk.peek_next_ticket()}")
    print(f"Second preview: {empty_desk.peek_next_ticket()}")
    print(f"Pending after previews: {empty_desk.get_pending_ticket_count()}")


if __name__ == "__main__":
    main()
