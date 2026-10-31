# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.


### Discussion Board Reflection

I learned how inserting, deleting, and searching affected a Python list.
My functions used `insert()` to add an item at a position, `pop()` to remove
and return an item, and a loop to find the first matching value. Testing
beginning, middle, and end positions helped me see how indexes changed after
an edit.

One detail that needed care was validating deletion indexes. I returned
`None` for invalid indexes so the list stayed unchanged. I also checked
empty lists, single-item lists, and duplicate values. Another important
check was handling a search result of `-1`, since passing it directly to
`pop()` would remove the final item instead of leaving the list alone.

My playlist example inserted a song, found another song by title, and removed
it by index. It showed how list operations supported edits to an ordered
collection.

In a larger application, beginning and middle edits could become slower
because later items needed to shift. Searching could also take longer as
the list grew because it checked values one at a time. This helped explain
why choosing a data structure depended on the operations used most often.
