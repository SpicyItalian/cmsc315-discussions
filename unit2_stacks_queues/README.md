# Unit 2 Discussion: Stacks and Queues

## Overview

I implemented a stack and a queue in Python and combined them in a support
desk scenario. The stack demonstrated LIFO (last-in, first-out), and the
queue demonstrated FIFO (first-in, first-out).

## Learning Objectives

- Implemented stack operations.
- Implemented queue operations.
- Demonstrated LIFO and FIFO behavior.
- Checked empty structures, single-item boundaries, and invalid tickets.

## Requirements

I completed all student tasks while retaining the original `# TODO (Student)`
prompts, class names, method signatures, and demonstration instructions:

1. Implemented stack operations.
2. Implemented queue operations.
3. Demonstrated LIFO behavior.
4. Demonstrated FIFO behavior.
5. Created and checked edge cases.
6. Added a real-world support desk scenario.

## Run the Program

I ran the program from the repository root with Python 3:

```sh
python unit2_stacks_queues/unit2_discussion.py
```

The program used only the Python standard library and required no additional
packages. It could also be run from IntelliJ after selecting a Python interpreter.

## Implementation and Observed Results

I used a Python list for `Stack`. Both `push()` and `pop()` operated at the
same end, so the newest item was removed first. After I pushed 10, 20, 30,
and 40, the removal order was **40, 30, 20, 10**.

I used `collections.deque` for `Queue`. `enqueue()` appended at the back,
and `dequeue()` used `popleft()` to remove the oldest item from the front.
After I enqueued 10, 20, 30, and 40, the removal order was **10, 20, 30, 40**.
Using a deque avoided shifting all remaining items during front removal.

`peek()` and `front()` returned an item without removing it. `is_empty()`
identified empty structures, and `get_length()` returned their sizes.

## Edge Cases and Verification

I ran the complete program and checked its behavior with assertions:

| Case | Observed result |
| --- | --- |
| Popped or peeked at an empty stack | Returned `None` without an exception. |
| Dequeued or viewed an empty queue | Returned `None` without an exception. |
| Removed the only stack or queue item | Returned the item and left the structure empty. |
| Repeatedly previewed the next ticket | Returned the same ticket without changing the queue length. |
| Added `None`, an empty string, spaces, or a number as a ticket | Raised `ValueError` and left the queue unchanged. |
| Processed with no waiting tickets | Returned `No tickets to process.` and recorded no action. |
| Previewed with no waiting tickets | Returned `No tickets available.` |
| Undid with no recorded actions | Returned `No actions to undo.` |
| Undid several processed tickets | Removed history entries in reverse processing order. |

The generic stack and queue accepted arbitrary values, including `None`.
Consequently, `None` as an empty-operation result was ambiguous if `None`
had also been stored. The demonstrations used non-None values, and the
support desk rejected non-string and blank tickets. An exception-based
empty-operation API would have removed that ambiguity in a larger application.

## Support Desk Scenario

I combined the two structures through their public methods:

| Method | Implemented behavior |
| --- | --- |
| `add_ticket(ticket)` | Validated the description and queued the ticket. |
| `peek_next_ticket()` | Previewed the oldest waiting ticket. |
| `process_next_ticket()` | Removed the oldest ticket and pushed its description onto history. |
| `undo_last_action()` | Removed the newest history entry without requeuing the ticket. |
| `get_pending_ticket_count()` | Returned the queue length. |
| `get_action_history_size()` | Returned the stack length. |

I added Reset password, Install printer, and Update software. The program
processed the first two tickets and removed the Install printer history
entry first. It finished that scenario with **one pending ticket (Update
software)** and **one history entry (Reset password)**. Undo represented
removing an action record; it did not reverse the completed service itself.

The queue modeled first-come, first-served requests, like customers at a
coffee shop. The stack modeled accessing the newest action first, like
an editor's undo history. A complete editor would also reverse the actual edit.

This Python discussion implementation remained separate from the Java lab
and its JUnit requirements.

## Time and Memory Analysis

I chose operations with O(1) removal, preview, and length access. Python
list append had amortized O(1) time because occasional resizing could copy
existing references. Deque operations at either end took O(1) time.

Each structure required O(n) container space for n stored entries. In the
support desk, p pending tickets and h history entries required O(p + h)
container space, plus memory for the ticket strings. Longer descriptions
used more memory. Processing moved a reference from the queue into history,
so reducing the queue length alone did not release the recorded ticket.
Neither structure imposed a fixed capacity. Retaining unlimited history or
accepting unlimited tickets could eventually exhaust available memory;
a larger system could bound the queue and archive or limit older history.

## Template and Backup Preservation

I retained all original TODO prompts and added the implementation below them.
The existing `.gitignore` rule excluded `_ORIGINAL_BACKUP/`, and I left that
folder untouched.

## Discussion Board Reflection

Original reflection prompts:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain the differences between stacks and queues as this relates to real-world applications.

### Initial Post Draft

Repository: [cmsc315-discussions](https://github.com/SpicyItalian/cmsc315-discussions)

I implemented my stack with a Python list and my queue with
`collections.deque`. The stack added and removed values at the same end,
which produced LIFO behavior. The queue added values at the back and removed
them from the front with `popleft()`, which produced FIFO behavior without
shifting the remaining items.

My support desk scenario combined both structures. Incoming tickets waited
in the queue, so the oldest request was processed first, similar to customers
lining up at a coffee shop. Processed tickets were recorded in the stack,
so removing a history entry accessed the most recent action first, similar
to a text editor's undo history. In my simulation, undo removed only the
record; it did not return the ticket to the queue.

I checked empty removals and previews, single-item boundaries, repeated
previews, and invalid ticket descriptions. These checks helped me distinguish
viewing an item from removing it and keep empty operations predictable.

Each structure used O(n) container memory for n entries, plus the stored
data. Adding tickets or retaining more history increased memory use, so a
larger system would benefit from capacity limits or history cleanup.

## Submission Checklist Review

- Completed the Python implementation, explanatory comments, and edge cases.
- Retained the original TODO prompts and documented the work in past tense.
- Added a real-world scenario and discussed efficiency and memory growth.
- Prepared the initial post and included the configured GitHub repository link.
- Left posting in LEO and the two peer responses for the student to complete.
  Peer-specific comparisons required the classmates' actual implementations.
- Kept `submission_checklist.md` unchanged because it covered all weekly
  discussions, including actions outside this code task.
