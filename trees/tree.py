from node import Node

class Tree:
    def __init__(self, root, name) -> None:
        self.root = root
        self.name = name

    def _nodeToChar(self, n, spacing):
        if n is None:
            return "_" + (" " * spacing)
        spacing = spacing - len(n.toStr()) + 1
        return n.toStr() + (" " * spacing)
    def printTree(self):
        height = self.root.height()
        spacing = 3
        width = int((2 ** height - 1) * (spacing + 1) + 1)
        # Root offset
        offset = int((width - 1) / 2)
        for depth in range(0, height + 1):
            if depth > 0:
                # Print Directional lines
                print(" " * (offset + 2) + (" "*(spacing + 2)).join(
                    ["/" + (" " * (spacing - 2)) + "\\"] * (2 ** (depth - 1)))
                )
            row = self.root.getNodesAtDepth(depth, [])
            print((" " * offset) + " ".join([self._nodeToChar(n, spacing) for n in row]))
            spacing = offset + 1
            offset = int(offset/2) - 1

        print("")

    def add(self, data):
        return self.root.add(data)
    
    def delete(self, target):
        self.root = self.root.delete(target)

    def search(self, target): ## This is a wrapper function
        return self.root.search(target)
    
    def traversePreorder(self):
        self.root.traversePreorder()

    def traversePostorder(self):
        self.root.traversePostorder()

    def traverseInorder(self):
        return self.root.traverseInorder()
    
    def getNodesAtDepth(self, depth):
        return self.root.getNodesAtDepth(depth)
    def height(self, h=0):
        return self.root.height()
    
    def isBalanced(self):
        return self.root.isBalanced()

def rotateRight(root):
    pivot = root.left
    reattachNode = pivot.right
    root.left = reattachNode
    pivot.right = root
    return pivot

def rotateLeft(root):
    pivot = root.right
    reattachNode = pivot.left
    root.right = reattachNode
    pivot.left = root
    return pivot


unbalancedLeftLeft = Tree(Node(30), "UNBALANCED LEFT LEFT")
unbalancedLeftLeft.root.left = Node(20)
unbalancedLeftLeft.root.left.right = Node(21)
unbalancedLeftLeft.root.left.left = Node(10)
unbalancedLeftLeft.root.left.left.left = Node(9)
unbalancedLeftLeft.root.left.left.right = Node(11)
unbalancedLeftLeft.printTree()

unbalancedLeftLeft.root = rotateRight(unbalancedLeftLeft.root)

unbalancedLeftLeft.printTree()

unbalancedRightRight = Tree(Node(10), "UNBALANCED RIGHT RIGHT")
unbalancedRightRight.root.right = Node(20)
unbalancedRightRight.root.right.left = Node(19)
unbalancedRightRight.root.right.right = Node(30)
unbalancedRightRight.root.right.right.left = Node(29)
unbalancedRightRight.root.right.right.right = Node(31)
unbalancedRightRight.printTree()

unbalancedRightRight.root = rotateLeft(unbalancedRightRight.root)

unbalancedRightRight.printTree()

unbalancedLeftRight = Tree(Node(30), "UNBALANCED LEFT RIGHT")
unbalancedLeftRight.root.right = Node(31)
unbalancedLeftRight.root.left = Node(10)
unbalancedLeftRight.root.left.right = Node(20)
unbalancedLeftRight.root.left.left = Node(9)
unbalancedLeftRight.root.left.right.left = Node(19)
unbalancedLeftRight.root.left.right.right = Node(21)
unbalancedLeftRight.printTree()

unbalancedLeftRight.root.left = rotateLeft(unbalancedLeftRight.root.left)
unbalancedLeftRight.root = rotateRight(unbalancedLeftRight.root)


unbalancedLeftRight.printTree()

unbalancedRightLeft = Tree(Node(30), "UNBALANCED RIGHT LEFT")
unbalancedRightLeft.root.left = Node(31)
unbalancedRightLeft.root.right = Node(10)
unbalancedRightLeft.root.right.left = Node(20)
unbalancedRightLeft.root.right.right = Node(9)
unbalancedRightLeft.root.right.left.right = Node(19)
unbalancedRightLeft.root.right.left.left = Node(21)
unbalancedRightLeft.printTree()

unbalancedRightLeft.root.right = rotateRight(unbalancedRightLeft.root.right)
unbalancedRightLeft.root = rotateLeft(unbalancedRightLeft.root)
unbalancedRightLeft.printTree()
"""
#tree = Tree(Node(50))

tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
#tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
#tree.root.left.left.right=Node(13)
#tree.root.left.left.left.left=Node(2)

print(tree.height())
print(tree.getNodesAtDepth(4))
tree.printTree()

tree.add(15)
tree.add(85)
tree.printTree()
tree.delete(25)
tree.delete(50)
tree.printTree()
print(tree.isBalanced())

print("Traverse Pre-Order")
tree.traversePreorder()

print("Traverse In-Order")
tree.traverseInorder()

print("Traverse Post-Order")
tree.traversePostorder()
"""