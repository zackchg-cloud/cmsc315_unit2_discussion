from collections import deque

class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []  # A list naturally supports LIFO because append/pop operate at the end.

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # LIFO: The newest item goes on "top" and will be removed first.
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # If the stack is empty, return a helpful message instead of crashing.
        if self.is_empty():
            return "Stack is empty — cannot pop."
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Peek lets us *look* at the most recent item without removing it.
        if self.is_empty():
            return "Stack is empty — nothing to peek."
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # deque allows efficient FIFO operations from both ends.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # FIFO: The earliest item added is served first.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        if self.is_empty():
            return "Queue is empty — cannot dequeue."
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Front shows the next item that will be served.
        if self.is_empty():
            return "Queue is empty — nothing at the front."
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # STACK DEMO
    # ===============================
    print("\n=== STACK DEMO (LIFO) ===")
    stack = Stack()

    print("Pushing items: A, B, C, D")
    for item in ["A", "B", "C", "D"]:
        stack.push(item)
        print(f"Pushed {item} → Stack now: {stack.items}")

    print("\nDemonstrating LIFO behavior:")
    print(f"Popping top item → {stack.pop()}")
    print(f"Popping next item → {stack.pop()}")

    print("\nTesting pop() on empty stack:")
    empty_stack = Stack()
    print(empty_stack.pop())

    print("\nTesting peek() on empty stack:")
    print(empty_stack.peek())

    print("\nSingle-item stack test:")
    single = Stack()
    single.push("OnlyItem")
    print(f"Peek → {single.peek()}")
    print(f"Pop → {single.pop()}")
    print(f"Is empty after removal? {single.is_empty()}")

    # ===============================
    # QUEUE DEMO
    # ===============================
    print("\n=== QUEUE DEMO (FIFO) ===")
    queue = Queue()

    print("Enqueuing items: 1, 2, 3, 4")
    for item in [1, 2, 3, 4]:
        queue.enqueue(item)
        print(f"Enqueued {item} → Queue now: {list(queue.items)}")

    print("\nDemonstrating FIFO behavior:")
    print(f"Dequeuing front item → {queue.dequeue()}")
    print(f"Dequeuing next item → {queue.dequeue()}")

    print("\nTesting dequeue() on empty queue:")
    empty_queue = Queue()
    print(empty_queue.dequeue())

    print("\nTesting front() on empty queue:")
    print(empty_queue.front())

    print("\nSingle-item queue test:")
    single_q = Queue()
    single_q.enqueue("OnlyItem")
    print(f"Front → {single_q.front()}")
    print(f"Dequeue → {single_q.dequeue()}")
    print(f"Is empty after removal? {single_q.is_empty()}")

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================
    print("\n=== REAL-WORLD SCENARIO ===")
    print("Simulating a coffee shop line using a queue (FIFO):")

    coffee_line = Queue()
    for customer in ["Alice", "Bob", "Charlie"]:
        coffee_line.enqueue(customer)
        print(f"{customer} entered the line → {list(coffee_line.items)}")

    print("\nServing customers:")
    while not coffee_line.is_empty():
        print(f"Serving → {coffee_line.dequeue()}")

    print("\nSimulating undo history using a stack (LIFO):")
    undo_stack = Stack()
    for action in ["Type A", "Type B", "Delete B"]:
        undo_stack.push(action)
        print(f"Action recorded → {undo_stack.items}")

    print("\nUndoing actions:")
    while not undo_stack.is_empty():
        print(f"Undo → {undo_stack.pop()}")


if __name__ == "__main__":
    main()

