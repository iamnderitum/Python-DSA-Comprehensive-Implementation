class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def search(self, target):
        if self.data == target:
            print("Found It!!")
            return self
        
        if self.left and self.data > target:
            return self.left.search(target)
        
        if self.right and self.data < target:
            return self.right.search(target)
        
        print("Value is not in tree")

    def add(self, data):
        if self.data == data:
            return
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.add(data)

        if data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.add(data)

    def findMin(self):
        if self.left:
            return self.left.findMin()
        return self.data
    def delete(self, target):
        if self.data == target:
            # Do deletion here
            if self.left and self.right:
                # RTFM (Right Tree Find Minimum)
                minValue = self.right.findMin()
                self.data = minValue
                self.right = self.right.delete(minValue)
                return self
            else:
                return self.left or self.right
        if self.right and target > self.data:
            self.right = self.right.delete(target)

        if self.left and target < self.data:
            self.left = self.left.delete(target)
        return self

    def traversePreorder(self):
        print(self.data)
        if self.left: 
            self.left.traversePreorder()
        if self.right:
            self.right.traversePreorder()

    def traverseInorder(self):
        if self.left:
            self.left.traverseInorder()
        print(self.data)
        if self.right:
            self.right.traverseInorder()

    def traversePostorder(self):
        if self.left:
            self.left.traversePostorder()
        if self.right:
            self.right.traversePostorder
        print(self.data)

    def getNodesAtDepth(self, depth, nodes=[]):
        if depth == 0:
            nodes.append(self)
            return nodes
        if self.left:
            self.left.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))
        if self.right:
            self.right.getNodesAtDepth(depth - 1, nodes)
        else:
            nodes.extend([None] * 2 ** (depth - 1))

        return nodes
    def height(self, h=0):
        leftHeight = self.left.height(h + 1) if self.left else h
        rightHeight = self.right.height(h + 1) if self.right else h
        return max(leftHeight, rightHeight)
    
    def isBalanced(self):
        leftHeight = self.left.height() + 1 if self.left else 0
        rightHeight = self.right.height() + 1 if self.right else 0
        return abs(leftHeight - rightHeight) - 2
    
    def toStr(self):
        if not self.isBalanced():
            return str(self.data) + "*"
        return str(self.data)