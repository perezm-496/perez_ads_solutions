import binary

class AVLNode(binary.BinaryTreeNode):

    def __init__(self, key, data, parent=None, height=-1):
        super().__init__(key, data, parent)
        self.height = height

    def __str__(self):
        txt = "["
        txt += str(self.key)
        txt += ":" + str(self.data)
        txt += ":height "+str(self.height)
        bal = 0
        if self.left is not None:
            bal -= self.left.height
        else:
            bal -= -1
        if self.right is not None:
            bal += self.right.height
        else:
            bal += -1

        txt += "::" + str(bal) + "]"
        return txt

class AVLTree(binary.BST):

    def __init__(self, key, data):
        super().__init__(key, data)
        self.root = AVLNode(key, data, parent=None, height=0)

    def height(self, v):
        if v is None:
            return -1
        return v.height
    
    def bst_delete(self, key):
        """
        Delete a node as in a normal BST.
        """
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

    def insert(self, key, data):
        """
        Insert a node as in a normal BST.
        Then search for unbalance nodes and fix the unbalance.
        """
        # Insert the node
        curr = self.root
        x = None
        while x is None:
            if key > curr.key:
                if curr.right is None:
                    curr.right = AVLNode(
                        key,
                        data,
                        parent=curr)
                    x = curr.right
                else:
                    curr = curr.right
            elif key < curr.key:
                if curr.left is None:
                    curr.left = AVLNode(
                        key,
                        data,
                        parent=curr)
                    x = curr.left
                else:
                    curr = curr.left
            else:
                #  The key is repeated.
                return None
        #  Start fixing the unbalance
        v = x
        while v is not None:
            #  Update the height
            left_height = self.height(v.left)
            right_height = self.height(v.right)
            new_height = max(right_height,left_height) + 1
            if v.height == new_height:
                #  No need to update more nodes.
                break
            v.height = new_height

            if right_height - left_height > 1:
                # Case a. The node increase the height of the right subtree
                if v.right.key < x.key:
                    # The new node was inserted at the right sub tree of v.right
                    v = self.left_rotation(v)
                else:
                    # The new node was inserted at the left sub tree of v.right
                    B = self.right_rotation(v.right)
                    v = self.left_rotation(v)
            elif right_height - left_height < -1:
                print("Unbalance found")
                # Case b. The node increase the height of the left subtree
                if v.left.key > x.key:
                    v = self.right_rotation(v)
                else:
                    A = self.left_rotation(v.left)
                    v = self.right_rotation(v)
            v = v.parent
        return x
    
    def right_rotation(self, v):
        parent = v.parent

        #  v becomes the right child of its left child
        A = v.left
        if A is None:
            return None
        
        R = A.right
        A.right = v
        v.parent = A
        v.left = R
        if R is not None:
            R.parent = v

        if parent is not None:
            if parent.key > A.key:
                parent.left = A
            else:
                parent.right = A
        
        A.parent = parent

        v.height = max(
            self.height(R),
            self.height(v.right)) + 1
        A.height = max(
            self.height(A.left),
            self.height(v)) + 1
        if self.root.key == v.key:
            self.root = A
        return A

    def left_rotation(self, v):
        parent = v.parent
        B = v.right
        if B is None:
            return None
        L = B.left
        B.left = v
        v.parent = B
        v.right = L
        if L is not None:
           L.parent = v
        if parent is not None:
            if parent.key > B.key:
                parent.left = B
            else:
                parent.right = B
        
        B.parent = parent

        # Update the heights

        v.height = max(
            self.height(v.left),
            self.height(L)) + 1
        B.height = max(
            self.height(v),
            self.height(B.right)) + 1
        
        if self.root.key == v.key:
            self.root = B
        
        return B

def check_avl(v):
    """
    Check if a tree has the avl property.
    Re-computes the heights and check that they were updated correctly.
    Re-computes the balance factor and check that all are in range.
    """
    if v is None:
        return True, True, -1
    is_bal_l, correct_h_l, left_height = check_avl(v.left)
    is_bal_r, correct_h_r, right_height = check_avl(v.right)
    is_bal = is_bal_l and is_bal_r
    correct_h = correct_h_l and correct_h_r
    val = max(
        left_height,
        right_height) + 1
    if val != v.height:
        correct_h = False
    if abs(right_height - left_height) > 1:
        is_bal = False
    return is_bal, correct_h, val
    
def show(node, offset=0):
    """
    In order traversal allows for a nice
    display of binary trees.
    """
    if node is None:
        return None
    show(node.left, offset=offset+1)
    if offset !=0:
        print("   "*(offset-1) + "--->" + str(node))      
    else:
        print(str(node))
    show(node.right, offset=offset+1)

T = AVLTree(200, "root")

import numpy as np

N = 10
acc = 0
for it in range(N):
    data = np.random.randint(0, 1024, 1024)
    T = AVLTree(data[0], data[0])
    for x in data[1:]:
        T.insert(x, x)
    b, c, v = check_avl(T.root)
    if not b:
        print("Failed Test")
        break
    else:
        print("Successful Test")
        acc += 1

print(f"Acc: {acc/N}")
