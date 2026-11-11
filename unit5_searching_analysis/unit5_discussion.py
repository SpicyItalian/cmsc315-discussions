"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


from timeit import timeit


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # A miss or a hit at the end checks all n items, so worst-case time is O(n).
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        value = lst[mid]
        if value == target:
            return mid
        # Sorted order lets us discard the midpoint and roughly half
        # the remaining candidates, giving O(log n) worst-case time.
        if value < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def show_result(dataset, target):
    """Print both results in the same format, using zero-based indexes."""
    print(
        f"Target {target!r}: linear = {linear_search(dataset, target)}, "
        f"binary = {binary_search(dataset, target)}"
    )


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    # TODO: Create a small dataset and test both searches.
    small = [2, 4, 6, 8, 10]
    print(f"Sorted data: {small} (-1 means not found)")
    show_result(small, 6)  # Both return 2, the third position.
    show_result(small, 7)  # Both return -1 because 7 is absent.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    # TODO: Create a larger dataset and compare results.
    large = list(range(0, 200_000, 2))
    runs = 100
    print(f"{len(large):,} sorted values; mean time per search over {runs} runs.")
    # A late hit and a miss force a full linear scan. Binary search
    # still halves the candidate range on each unsuccessful comparison.
    for target in (large[-1], large[-1] + 1):
        show_result(large, target)
        # Both searches use the same prebuilt list; setup is excluded.
        for name, search in (("Linear", linear_search), ("Binary", binary_search)):
            elapsed = timeit(lambda: search(large, target), number=runs)
            print(f"  {name}: {elapsed / runs * 1_000_000:,.2f} microseconds per search")
    print("Worst-case time: linear O(n); binary O(log n) on sorted data.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    # TODO: Demonstrate and explain edge cases.
    for label, data, target in (
        ("Empty list: neither search has an item to check", [], 4),
        ("Singleton hit: the only item is at index 0", [4], 4),
        ("Singleton miss: the only item differs from the target", [4], 5),
        ("First position: linear search stops after one check", small, 2),
        ("Negative values: sorted order still applies", [-9, -5, -1], -5),
    ):
        print(label)
        show_result(data, target)

    print("\n=== REAL-WORLD SCENARIO: LIBRARY INVENTORY ===")
    # One lookup can scan the unsorted arrival list directly. For repeated
    # lookups, sort once and use binary search on the sorted inventory IDs.
    arrivals = ["BK-104", "BK-102", "BK-101", "BK-103"]
    inventory = sorted(arrivals)
    target = "BK-104"
    print(f"Looking up {target} in a new shipment:")
    print(f"  Unsorted arrival list: index {linear_search(arrivals, target)}")
    print(f"  Sorted inventory: index {binary_search(inventory, target)}")
    print("  Both found the same book; the indexes refer to different lists.")


if __name__ == "__main__":
    main()
