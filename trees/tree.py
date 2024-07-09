from node import Node

class Tree:
    def __init__(self, root) -> None:
        self.root = root

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
tree = Tree(Node(50))

tree.root.left = Node(25)
tree.root.right = Node(75)
tree.root.left.left = Node(10)
tree.root.left.right = Node(35)
tree.root.left.right.left = Node(30)
#tree.root.left.right.right = Node(42)
tree.root.left.left.left = Node(5)
tree.root.left.left.left.left = Node(3)
#tree.root.left.left.right=Node(13)
#tree.root.left.left.left.left=Node(2)

print(tree.height())
print(tree.getNodesAtDepth(4))
tree.printTree()
"""
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