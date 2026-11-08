"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        # New nodes start as leaves until insertion connects their children.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        # A missing root represents a tree with no values.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # Smaller values belong on the left and larger values on the right.
        # Save the returned reference so insertion also works for an empty tree.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: this empty position becomes the new value's node.
        if node is None:
            return Node(value)

        # Follow only the subtree that can contain the value and reconnect it.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Equal values are ignored so each value appears only once in this BST.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Ordering lets each comparison discard one subtree rather than scan
        # every value. Search takes O(h) time for tree height h: O(log n) when
        # balanced, but O(n) if insertion order creates a long chain.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case: reaching a missing child means the value was not found.
        if node is None:
            return False
        if value == node.value:
            return True

        # A smaller target cannot be in the right subtree, and vice versa.
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Collect into a fresh list without changing the tree itself.
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # Empty subtrees contribute no values and stop this recursive branch.
        if node is None:
            return

        # Left values are smaller and right values are larger, so visiting
        # left, current, then right produces values in ascending order.
        self._inorder_recursive(node.left, values)
        values.append(node.value)
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # This insertion order creates both left and right subtrees.
    tree = BST()
    inserted_values = [50, 30, 70, 20, 40, 60, 80]
    for value in inserted_values:
        tree.insert(value)
    print(f"Values inserted: {inserted_values}")
    print(f"Root value: {tree.root.value}")
    # In this balanced example, each comparison rules out a whole subtree.
    # This basic BST does not rebalance itself when the insertion order changes.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # All left descendants precede their parent, followed by right descendants.
    print(f"In-order traversal: {tree.inorder()}")
    print("Left, current, right produces the values in ascending order.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Two stored values return True; two missing values return False.
    for value in (20, 60, 25, 90):
        print(f"Search for {value}: {tree.search(value)}")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Both traversal and search stop safely when the root is None.
    empty_tree = BST()
    print(f"Empty-tree traversal: {empty_tree.inorder()}")
    print(f"Search empty tree for 50: {empty_tree.search(50)}")

    # A one-node tree can find its root but has no other values.
    single_tree = BST()
    single_tree.insert(42)
    print(f"Single-node traversal: {single_tree.inorder()}")
    print(f"Search single-node tree for 42: {single_tree.search(42)}")
    print(f"Search single-node tree for 99: {single_tree.search(99)}")

    # The duplicate policy keeps existing nodes and ignores equal insertions.
    tree.insert(30)
    print(f"After inserting duplicate 30: {tree.inorder()} (unchanged)")

    # Sorted insertions create a chain because this tree does not self-balance.
    skewed_tree = BST()
    for value in (1, 2, 3, 4):
        skewed_tree.insert(value)
    print(f"Sorted insertion traversal: {skewed_tree.inorder()}")
    print(f"Search chain for 4: {skewed_tree.search(4)}")
    print("Sorted insertions can make search linear instead of logarithmic.")

    # Real-world example: store unique product IDs for an inventory lookup.
    print("\n=== PRODUCT INVENTORY SCENARIO ===")
    inventory = BST()
    product_ids = [1050, 1020, 1080, 1010, 1030, 1070, 1090]
    for product_id in product_ids:
        inventory.insert(product_id)
    print(f"Product IDs entered: {product_ids}")
    print(f"Product IDs in sorted order: {inventory.inorder()}")
    print(f"Product 1030 exists: {inventory.search(1030)}")
    print(f"Product 1060 exists: {inventory.search(1060)}")



if __name__ == "__main__":
    main()