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

    def search(self,k):
        curr = self.root
        while curr is not None:
            if k == curr.key:
                return curr.value
            if k < curr.key:
                curr = curr.left
            if k > curr.key:
                curr = curr.right
        return None
    
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


t1 = BSTree()
t2 = BSTree()
t2.set_value("car", 17)
t2.set_value("ann", 31)
t2.set_value("ben", 90)
t2.set_value("abe", 5)
t2.set_value("angel", 14)
t2.set_value("dav", 89)
