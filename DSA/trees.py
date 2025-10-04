class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def insert(self, key):
        if key < self.val:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.val)
        if self.right:
            self.right.print_tree()                

head = TreeNode(10)
head.insert(5)
head.insert(15)
head.insert(3)
head.insert(7)
head.print_tree()
print(head.left.val)




