from __future__ import absolute_import
from __future__ import division
from __future__ import print_function


class Node(object):
    """Node class collects helper functions for BinarySearchTree."""
    def __init__(self, val, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTree(object):
    """Binary search tree class.

    Property:
    - The left subtree of a node contains only nodes with vals lesser than 
      the node's val.
    - The right subtree of a node contains only nodes with vals greater than 
      the node's val.

    Travesal:
    - Inorder: left -> root -> right
    - Preorder: root -> left -> right
    - Postorder: left -> right -> root
    """
    def __init__(self):
        self.root = None

    def search_recur(self, root, val):
        """Search val starting from root by recursion.

        Time complexity: O(logn), where n is the node number.
        Space complexity: O(logn).
        """
        if not root:
            return False

        if val == root.val:
            return True
        elif val < root.val:
            return self.search_recur(root.left, val)
        else:
            return self.search_recur(root.right, val)

    def search_iter(self, root, val):
        """Search val starting from root by iteration.

        Time complexity: O(logn), where n is the node number.
        Space complexity: O(1).
        """
        current = root
        while current:
            if val == current.val:
                return True
            elif val < current.val:
                current = current.left
            else:
                current = current.right
        return False

    def _insert_recur_util(self, root, new_val):
        """Helper function for insert_recur()"""
        new_node = Node(new_val)

        if new_val < root.val:
            if not root.left:
                root.left = new_node
                new_node.parent = root
                return None
            else:
                self._insert_recur_util(root.left, new_val)
        else:
            if not root.right:
                root.right = new_node
                new_node.parent = root
                return None
            else:
                self._insert_recur_util(root.right, new_val)

    def insert_recur(self, new_val):
        """Insert a new node with val by recursion.

        Time complexity: O(logn).
        Space complexity: O(logn).
        """
        if not self.root:
            self.root = Node(new_val)
            return None

        self._insert_recur_util(self.root, new_val)

    def insert_iter(self, new_val):
        """Insert a new node with val by iteration.

        Use current and parent to track new node's insertion postion
        and its parent.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        new = Node(new_val)

        parent = None
        current = self.root

        # Go down to the bottom node whose parent will be new node's parent.
        while current:
            parent = current
            if new_val < current.val:
                current = current.left
            else:
                current = current.right
        new.parent = parent

        if not parent:
            # If the tree is empty.
            self.root = new
        elif new_val < parent.val:
            parent.left = new
        else:
            parent.right = new

    def find_minimum(self, root):
        """Find minimum starting from root.

        Time complexity: O(logn), where n is the node number.
        Space complexity: O(1).
        """
        current = root
        while current.left:
            current = current.left
        return current

    def find_maximum(self, root):
        """Find maximum starting from root.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        current = root
        while current.right:
            current = current.right
        return current

    def find_successor(self, root):
        """Find succesor of root, i.e. next biggest node.

        Time complexity: O(logn), where n is the node number.
        Space complexity: O(1).
        """
        current = root

        # If root's right existed, find leftmost node in root's right subtree.
        if current.right:
            return self.find_minimum(current.right)

        # If not, go up the tree to the lowest ancestor of node, 
        # whose "left" child is also an ancestor of node.
        parent = current.parent
        while parent and current == parent.right:
            current = parent
            parent = parent.parent
        return parent

    def find_predecessor(self, root):
        """Find predecessor of root, i.e. previous biggest node.

        Time complexity: O(logn), where n is the node number.
        Space complexity: O(1).
        """
        current = root

        # If root's left existed, find rightmost node in root's left subtree.
        if current.left:
            return self.find_maximum(current.left)

        # If not, go up the tree to the lowest ancestor of node, 
        # whose "right" child is also an ancestor of root.
        parent = current.parent
        while parent and current == parent.left:
            current = parent
            parent = parent.parent
        return parent

    def _transplant(self, from_node, to_node):
        """Helper function for delete(): Transplant a subtree.
        
        Time complexity: O(1).
        Space complexity: O(1).
        """
        if not to_node.parent:
            self.root = from_node
        elif to_node == to_node.parent.left:
            # If to_node is its parent's left node.
            to_node.parent.left = from_node
        else:
            # If to_node is its parent's right node.
            to_node.parent.right = from_node

        if from_node:
            from_node.parent = to_node.parent

    def delete(self, del_node):
        """Delete node.

        Time complexity: O(logn).
        Space complexity: O(1).
        """
        if not del_node.left:
            # If node has no left child, transplant right subtree to it.
            self._transplant(del_node.right, del_node)
        elif not del_node.right:
            # If node has no right child, transplant left subtree to it.
            self._transplant(del_node.left, del_node)
        else:
            # Node has both left & right children.
            # Find its "lower" succesor which has no left child.
            trans_node = self.find_minimum(del_node.right)

            # If trans_node's parent is not del_node,
            # transplant its right node to it, and take over del_node's right. 
            if trans_node.parent != del_node:
                self._transplant(trans_node.right, trans_node)
                trans_node.right = del_node.right
                trans_node.right.parent = trans_node

            # Finally, transplant trans_node to del_node.
            self._transplant(trans_node, del_node)
            trans_node.left = del_node.left
            trans_node.left.parent = trans_node

    def inorder_recur(self, root):
        """Inorder traversal: left -> root -> right, by recursion.

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return None

        self.inorder_recur(root.left)
        print(root.val)
        self.inorder_recur(root.right)

    def inorder_iter(self, root):
        """Inorder traversal: left -> root -> right, by iteration.

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return None

        previous = None
        current = root

        # Use stack for DFS for inorder traversal.
        stack = []

        while current or stack:
            # If current exists, push to stack and visit leftmost node.
            while current:
                stack.append(current)
                current = current.left

            # Pop stack as current and print its value.
            current = stack.pop()
            print(current.val)

            # Update current and previous by inorder traversal.
            previous = current
            current = current.right

    def preorder_recur(self, root):
        """Preorder traversal: root -> left -> right, by recursion.

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return None

        print(root.val)
        self.preorder_recur(root.left)
        self.preorder_recur(root.right)

    def preorder_iter(self, root):
        """Preorder traversal: root -> left -> right, by iteration.

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return None

        stack = [root]

        while stack:
            current = stack.pop()
            print(current.val)

            # Push right before left since we use stack with FILO.
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder_recur(self, root):
        """Postorder traversal: left -> right -> root, by recursion.

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return None

        self.postorder_recur(root.left)
        self.postorder_recur(root.right)
        print(root.val)

    def postorder_iter(self, root):
        """Postorder traversal: left -> right -> root, by iteration.

        Time complexity: O(n).
        Space complexity: O(logn) for balanced tree; O(n) for single sided tree.
        """
        if not root:
            return None

        # Collect revsersed traverses.
        rev_traverses = []

        stack = [root]

        while stack:
            current = stack.pop()
            rev_traverses.append(current.val)

            # Push left before right since we use stack with FILO.
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        for val in rev_traverses[::-1]:
            print(val)


def main():
    """
    Tree:
        6
       / \
      4   7
     / \   \
    2   5   8
    """
    bst = BinarySearchTree()
    bst.insert_recur(6)
    bst.insert_recur(4)
    bst.insert_recur(7)
    bst.insert_iter(2)
    bst.insert_iter(5)
    bst.insert_iter(8)

    # Inorder walk: 2, 4, 5, 6, 7, 8.
    print('Inorder traversal by recursion:')
    bst.inorder_recur(bst.root)
    print('Inorder traversal by iteration:')
    bst.inorder_iter(bst.root)

    # Preorder walk: 6, 4, 2, 5, 7, 8.
    print('Preorder traversal by recursion:')
    bst.preorder_recur(bst.root)
    print('Preorder traversal by iteration:')
    bst.preorder_iter(bst.root)

    # Postorder walk: 2, 5, 4, 8, 7, 6.
    print('Postorder traversal by recursion:')
    bst.postorder_recur(bst.root)
    print('Postorder traversal by iteration:')
    bst.postorder_iter(bst.root)

    # Search existing val 6.
    print('Search existing node with val 6:')
    print(bst.search_recur(bst.root, 6))
    print('Search existing node with val 6:')
    print(bst.search_iter(bst.root, 6))
    # Search nonexisting val 10.
    print('Search nonexisting node with val 10:')
    print(bst.search_recur(bst.root, 10))
    print('Search nonexisting node with val 10:')
    print(bst.search_iter(bst.root, 10))

    # Find min of root: 2.
    print('Find min: {}'.format(bst.find_minimum(bst.root).val))
    # Find min of root's right: 7.
    print('Find min from 7: {}'.format(bst.find_minimum(bst.root.right).val))

    # Find max of root: 2.
    print('Find max: {}'.format(bst.find_maximum(bst.root).val))
    # Find max of root's right: 8.
    print('Find max from 7: {}'.format(bst.find_maximum(bst.root.right).val))

    # Find successor of root: 7.
    print('Find successor: {}'.format(bst.find_successor(bst.root).val))
    # Find successor of root's left's right: 6.
    print('Find successor from left\'s right: {}'
          .format(bst.find_successor(bst.root.left.right).val))

    # Find predecessor of root: 5.
    print('Find predecessor of root: {}'
          .format(bst.find_predecessor(bst.root).val))
    # Find predecessor of root's left's right: 4.
    print('Find predecessor from root\'s left: {}'
          .format(bst.find_predecessor(bst.root.left.right).val))

    # Delete root's left: 5, the run inorder walk: 2, 5, 6, 7, 8.
    bst.delete(bst.root.left)
    print('Inorder traversal by recursion:')
    bst.inorder_recur(bst.root)

    # Further delete root: 6, the run inorder walk: 2, 5, 7, 8.
    bst.delete(bst.root)
    print('Inorder traversal after deleting 6:')
    bst.inorder_recur(bst.root)


if __name__ == '__main__':
    main()
