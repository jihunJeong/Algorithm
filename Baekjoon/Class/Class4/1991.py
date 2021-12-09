class Node:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return self.val

class Tree:
    def __init__(self, node=None):
        self.root = node

    def search(self, key):
        if self.root is None:
            return None

        stack = [self.root]
        node = None

        while stack:
            node = stack.pop()
            if node.val == key:
                break
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return node
    
    def preorder(self, root=None):
        if root is None:
            return

        print(root.val, end="")
        self.preorder(root.left)
        self.preorder(root.right)
    
    def inorder(self, root=None):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.val, end="")
        self.inorder(root.right)
    
    def postorder(self, root=None):
        if root is None:
            return
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val, end="")

N = int(input())

tree = Tree()
for _ in range(N):
    root, left, right = map(str, input().split())
    node = tree.search(root)
    
    if node is None:
        tree = Tree(Node(root))
        node = tree.root

    if left != ".":
        node.left = Node(left)
    if right != ".":
        node.right = Node(right)

tree.preorder(tree.root)
print()
tree.inorder(tree.root)
print()
tree.postorder(tree.root)