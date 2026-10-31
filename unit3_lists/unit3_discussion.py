"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Check the index before removal so invalid requests do not crash or mutate
    # the list. Valid negative indexes count backward from end.
    # Reject non-integer indexes, including bool, instead of passing them to pop.
    if type(index) is not int or not -len(lst) <= index < len(lst):
        return None

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Scan sequentially bc unsorted list has no shortcut to a match.
    for index, current_value in enumerate(lst):
        if current_value == value:
            return index

    # -1 to distinguish a missing value from a match at index zero.
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.")

    # Start with several values and show how each insertion changes their order.
    values = [10, 20, 30, 40]
    print(f"Original list: {values}")
    insert_at(values, 0, 5)
    print(f"Inserted 5 at the beginning: {values}")

    # Compute a middle position from the current length rather than hard-code it.
    middle_index = len(values) // 2
    insert_at(values, middle_index, 15)
    print(f"Inserted 15 at middle index {middle_index}: {values}")

    # An index equal to the length inserts after all existing elements.
    insert_at(values, len(values), 50)
    print(f"Inserted 50 at the end: {values}")

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.")

    # Remove from the beginning, then show both the return value and remaining list.
    removed = delete_at(values, 0)
    print(f"Deleted beginning value {removed}; updated list: {values}")

    # Recalculate the middle because deletion changed the current list length.
    middle_index = len(values) // 2
    removed = delete_at(values, middle_index)
    print(f"Deleted middle value {removed} at index {middle_index}; list: {values}")

    # The final valid nonnegative index is one less than the current length.
    removed = delete_at(values, len(values) - 1)
    print(f"Deleted end value {removed}; updated list: {values}")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.")

    found_index = search_value(values, 20)
    print(f"Search for existing value 20: index {found_index}; list: {values}")

    missing_index = search_value(values, 99)
    print(f"Search for missing value 99: {missing_index} (-1 means not found)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.")

    for invalid_index in (len(values), -len(values) - 1, "first"):
        removed = delete_at(values, invalid_index)
        print(f"Delete at invalid index {invalid_index!r}: {removed}; list: {values}")

    # An empty list supports insertion but has nothing to delete or find.
    empty_values = []
    print(f"Delete from empty list: {delete_at(empty_values, 0)}")
    print(f"Search empty list: {search_value(empty_values, 10)}")
    insert_at(empty_values, 0, 7)
    print(f"Insert into empty list: {empty_values}")

    # Removing the sole value returns list to empty state.
    removed = delete_at(empty_values, 0)
    print(f"Removed only value {removed}; empty afterward: {len(empty_values) == 0}")

    # return the first matching position.
    duplicates = [7, 3, 7]
    print(f"Search for 7 in {duplicates}: first index {search_value(duplicates, 7)}")

    # remove the final item safely.
    removed = delete_at(duplicates, -1)
    print(f"Deleted with index -1: {removed}; updated list: {duplicates}")

    # ordered list edits by position.
    print("\n=== SONG PLAYLIST SCENARIO ===")
    playlist = ["Song A", "Song B", "Song C"]
    print(f"Original playlist: {playlist}")
    insert_at(playlist, 1, "Song X")
    print(f"Inserted Song X at index 1: {playlist}")

    song_index = search_value(playlist, "Song B")
    if song_index != -1:
        removed = delete_at(playlist, song_index)
        print(f"Found and removed {removed}; playlist: {playlist}")

    # dont let missing song cause final song to be removed accidentally.
    song_index = search_value(playlist, "Song Z")
    if song_index == -1:
        print(f"Song Z was not found; playlist unchanged: {playlist}")



if __name__ == "__main__":
    main()