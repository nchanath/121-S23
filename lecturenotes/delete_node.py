class BSTNode:
    def __init__(self,k,v):
        self.key = k
        self.value = v
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return (self.root == None)

    def get_value(self, k): # tree search
        n = self.root
        while n != None:
            if n.key == k:
                return n.value
            elif n.key > k:
                n = n.left
            else:
                n = n.right
        return None

    def set_value(self, k, v): # tree insertion
        p = None
        n = self.root

        while n != None:
            p = n
            if k == n.key:
                n.value = v
                return
            elif k < n.key:
                n = n.left
            else:
                n = n.right

        e = BSTNode(k,v)
        if p == None:
            self.root = e
        elif k < p.key:
            p.left = e
        else:
            p.right = e

    def min_key(self):
        if self.root == None:
            return None
        else:
            n = self.root
            while n.left != None:
                n = n.left
            return n.key

    def size(self): # tree traversal

        def subtree_size(n):
            if n == None:
                return 0
            else:
                return 1 + subtree_size(n.left) + subtree_size(n.right)

        return subtree_size(self.root)

    def as_list(self):

        def subtree_list(n):
            if n == None:
                return []
            else:
                return subtree_list(n.left) + [(n.key,n.value)] + subtree_list(n.right)

        return subtree_list(self.root)

    def as_string(self):
        kvs = self.as_list()
        if len(kvs) == 0:
            return "{}"
        else:
            s = "{"
            for kv in kvs[:-1]:
                s += repr(kv[0])+": "+repr(kv[1])+", " 
            kv = kvs[-1]
            s += repr(kv[0])+": "+repr(kv[1])+"}"
            return s

    def __repr__(self):
        return self.as_string()

    __str__ = __repr__

    def __bool__(self):
        return not self.is_empty()

    def __contains__(self,k):
        return (self.get_value(k) != None)

    def __len__(self):
        return (self.size())

    def __getitem__(self,k):
        return self.get_value(k)

    def __setitem__(self,k,v):
        return self.set_value(k,v)

    def print_tree(self):
        def get_ascii_art(node):
            if node is None:
                return []
            lines = []
            left_lines = get_ascii_art(node.left)
            right_lines = get_ascii_art(node.right)
            key_str = str(node.key) + ": " + str(node.value)
            key_len = len(key_str)
            left_width = 0 if not left_lines else len(left_lines[0])
            right_width = 0 if not right_lines else len(right_lines[0])
            full_width = left_width + key_len + right_width
            lines.append(" " * left_width + key_str + " " * right_width)
            if len(left_lines) < len(right_lines):
                left_lines.extend([' ' * left_width] * (len(right_lines) - len(left_lines)))
            elif len(right_lines) < len(left_lines):
                right_lines.extend([' ' * right_width] * (len(left_lines) - len(right_lines)))
            for l, r in zip(left_lines, right_lines):
                lines.append(l + ' ' * key_len + r)
            return lines

        for line in get_ascii_art(self.root):
            print(line)

    def delete(self, k):
        # Find the node to be deleted and its parent node
        p = None
        n = self.root
        while n is not None and n.key != k:
            p = n
            if k < n.key:
                n = n.left
            else:
                n = n.right

        if n is None:  # key not found in tree
            return

        # Case 1: Node to be deleted has no children
        if n.left is None and n.right is None:
            if n == self.root:
                self.root = None
            elif n == p.left:
                p.left = None
            else:
                p.right = None

        # Case 2: Node to be deleted has one child
        elif n.left is None:
            if n == self.root:
                self.root = n.right
            elif n == p.left:
                p.left = n.right
            else:
                p.right = n.right
        elif n.right is None:
            if n == self.root:
                self.root = n.left
            elif n == p.left:
                p.left = n.left
            else:
                p.right = n.left

        # Case 3: Node to be deleted has two children
        else:
            # Find the minimum node in the right subtree of n
            min_parent = n
            min_node = n.right
            while min_node.left is not None:
                min_parent = min_node
                min_node = min_node.left

            # Replace n's key and value with that of the minimum node
            n.key = min_node.key
            n.value = min_node.value

            # Delete the minimum node (which has at most one child)
            if min_node == min_parent.left:
                min_parent.left = min_node.right
            else:
                min_parent.right = min_node.right    

t1 = BSTree()
t2 = BSTree()
t2.set_value("car", 17)
t2.set_value("ann", 31)
t2.set_value("ben", 90)
t2.set_value("abe", 5)
t2.set_value("angel", 14)
t2.set_value("dav", 89)
