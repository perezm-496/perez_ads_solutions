"""Array pointer implementation of a tree."""


class ArrayPntNode:
    """
       Node implementation for the array pointer tree.
    """

    def __init__(self, key, data, branch_factor=2, parent=None):
        self.child_array = [None]*branch_factor
        self.key = key
        self.data = data
        self.parent = parent

    def children(self):
        return self.child_array

    def is_leaf(self):
        for x in self.child_array:
            if x is not None:
                return False
        return True

    def __str__(self):
        txt = "["
        txt += str(self.key)
        txt += ":" + str(self.data)
        txt += "]"
        return txt


