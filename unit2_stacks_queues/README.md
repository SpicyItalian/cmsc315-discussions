# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## My Implementation

I used a Python list for the stack and `collections.deque` for the queue.
The stack removed items from the same end where they were added. The queue
added items at the back and removed them from the front with `popleft()`.
I kept the TODO prompts and added comments explaining the operations.

I added 10, 20, 30, and 40 to both structures. The stack returned
40, 30, 20, 10, while the queue returned 10, 20, 30, 40. Empty removals and
previews returned `None`. I also checked that removing the only item left
each structure empty and that previews did not remove anything.

For my support desk example, tickets were processed in arrival order and
stored in a stack after processing. Removing a history entry returned the
most recently processed ticket without adding it back to the queue. Blank
or non-string ticket descriptions raised `ValueError`.

I ran the program from the project folder using:

```sh
python unit2_stacks_queues/unit2_discussion.py
```

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.


### My Reflection

[GitHub repository](https://github.com/SpicyItalian/cmsc315-discussions)

I learned how stacks and queues handled the same values in different orders.
I used a list for my stack and a deque for my queue. The stack followed LIFO
because it added and removed items at the same end. The queue followed FIFO
because it added items at the back and removed them from the front.

One part that needed care was handling empty structures. I returned `None`
for empty removals and previews, and I checked single-item cases to make
sure the structures became empty after removal. I also checked that
previewing a ticket left it in the queue.

My support desk example used a queue to process tickets in the order they
arrived, like customers waiting at a coffee shop. It used a stack to remove
the newest history entry first, similar to a text editor's undo history.
In my example, undo removed the record without restoring the ticket.

Both structures used O(n) storage for n entries, plus the stored data.
Adding more tickets or keeping more history increased memory use, so a
larger program could limit capacity or clear old history.
