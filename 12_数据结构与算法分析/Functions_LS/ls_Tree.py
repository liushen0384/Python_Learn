"""
二叉树实现
"""
import operator


class BinaryTree():
    """
    二叉树实现
    """
    def __init__(self, rootbj):
        self.key = rootbj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def getRootVal(self):
        return self.key

    def setRootVal(self, newKey):
        self.key = newKey

    def preorder(self):
        """
        前序遍历二叉树内部函数
        :return:
        """
        print(self.key)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

def buildParseTree(fstr):
    """
    完全表达式二叉树的构建函数
    """
    pStack = []
    num = ""
    fTree = BinaryTree("")
    for i in fstr:
        if i in "0123456789":
            num = num + i
            continue
        elif num != "":
            fTree.setRootVal(num)
            num = ""
            fTree = pStack.pop()
        if i == "(":
            fTree.insertLeft("")
            pStack.append(fTree)
            fTree = fTree.getLeftChild()
        elif i in '+-/*':
            fTree.setRootVal(i)
            fTree.insertRight("")
            pStack.append(fTree)
            fTree = fTree.getRightChild()
        elif i == ")" and not pStack == []:
            fTree = pStack.pop()
    return fTree

def evaluate(parseTree):
    """
    完全括号表达式解析函数
    """
    opers = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    left = parseTree.getLeftChild()
    right = parseTree.getRightChild()
    if left and right:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(left), evaluate(right))
    else:
        return int(parseTree.getRootVal())

def preorder(tree):
    """
    二叉树前序遍历
    """
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postorder(tree):
    """
    二叉树后序遍历函数
    """
    if tree:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def inorder(tree):
    """
    二叉树中序遍历函数
    """
    if tree:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

def printexp(tree):
    """
    完全括号表达式还原函数
    """
    val = ''
    if tree:
        if tree.getRightChild():
            val = "(" + printexp(tree.getLeftChild())\
                + tree.getRootVal()\
                + printexp(tree.getRightChild()) + ")"
        else:
            val = tree.getRootVal()
    return val

class BinaryHeap:
    """
    二叉堆实现
    """
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def insert(self, item):
        """
        二叉堆插入元素
        """
        self.currentSize = self.currentSize + 1
        self.heapList.append(item)
        seek = self.currentSize
        while seek // 2 > 0:
            if self.heapList[seek // 2] > self.heapList[seek]:
                self.heapList[seek // 2], self.heapList[seek] =self.heapList[seek], self.heapList[seek // 2]
                seek = seek // 2

    def findMin(self):
        return self.heapList[1]

    def delMin(self):
        minItem = self.heapList[1]
        self.heapList[1] = self.heapList.pop()
        self.percDown(1)

    def minChild(self, i):
        """
        最小子节点查找
        """
        if (2 * i + 1) > self.currentSize:
            return 2 * i
        else:
            if self.heapList[2 * i] > self.heapList[2 * i + 1]:
                return 2 * i + 1
            else:
                return 2 * i

    def percDown(self, i):
        """
        根节点下移
        :param i:
        :return:
        """
        while 2 * i <= self.currentSize:
            mins = self.minChild(i)
            if self.heapList[i] > self.heapList[mins]:
                self.heapList[i], self.heapList[mins] = self.heapList[mins], self.heapList[i]
            i = mins

    def buildHeap(self, list):
        i = len(list) // 2
        self.currentSize = len(list)
        self.heapList = [0] + list[:]
        while i > 0:
            self.percDown(i)
            i = i - 1

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()