"""Simple implementation of a binary tree."""


class BinaryTreeNode:

    def __init__(self, key, data, parent=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        # Must trees don't use the parent
        self.parent = parent

    def __str__(self):
        txt = "["
        txt += str(self.key)
        txt += ":" + str(self.data)
        txt += "]"
        return txt


class BST:

    def __init__(self, key, data):
        self.root = BinaryTreeNode(key, data)

    def insert(self, key, data):
        curr = self.root
        while True:
            if key > curr.key:
                if curr.right is None:
                    curr.right = BinaryTreeNode(
                        key,
                        data,
                        parent=curr)
                    return curr.right
                else:
                    curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = BinaryTreeNode(
                        key,
                        data,
                        parent=curr)
                    return curr.left
                else:
                    curr = curr.left
            else:
                # The key is repeated.
                return None

    def search(self, key):
        curr = self.root
        while curr is not None:
            if key == curr.key:
                return curr
            elif key < curr.key:
                curr = curr.left
            else:
                curr = curr.right
        return None  # Not found response.

    def delete(self, key):
        ref = self.search(key)

        # In case the key is not found
        if ref is None:
            return -1  # Error code

        # First case the node is a leaf
        par = ref.parent
        if ref.left is None and ref.right is None:
            if par is None:
                self.root = None  # Empty tree
            if par.key > ref.key:
                par.left = None
            else:
                par.right = None
            return 1

        # Second case on child

        if ref.left is None:
            if par.key < ref.key:
                par.right = ref.right
            else:
                par.left = ref.right
            return 1
        if ref.right is None:
            if par.key < ref.key:
                par.right = ref.left
            else:
                par.left = ref.left
            return 1

        # Third case two child

        # Find the direct succesor
        suc_node = ref.right
        while suc_node.left is not None:
            suc_node = suc_node.left

        # Remove the node from its place in the tree
        answ_code = self.delete(suc_node.key)
        if answ_code == -1:
            return -1  # Something went horribly wrong

        # Replace the reference node witht he succesor
        if par.key < ref.key:
            par.right = suc_node
        else:
            par.left = suc_node
        suc_node.parent = par
        suc_node.left = ref.left
        suc_node.right = ref.right
        ref.left.parent = suc_node
        ref.right.parent = suc_node
        return 1


def show(node, offset=0):
    """
    In order traversal allows for a nice
    display of binary trees.
    """
    if node is None:
        return None
    show(node.left, offset=offset+1)
    print("      "*offset + str(node))
    show(node.right, offset=offset+1)


def show_tree(T):
    print("Binary Search Tree")
    show(T.root)


