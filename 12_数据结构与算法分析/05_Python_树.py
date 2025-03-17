"""

二叉树应用实例
"""
from Functions_LS.ls_Tree import *

a = BinaryTree("liushen")
print(a.getRootVal())

s1 = "((88+2)*((136-(1*27))-9))"
t = buildParseTree(s1)
preorder(t)
inorder(t)
postorder(t)
print(evaluate(t))
print(printexp(t))