# CodeU
Node:
For every node there is data, parent node, leftChild Node and rightChild Node.
There is a setters and getters and constructor.

Binary Tree:
the Binary Tree consist of Nodes with no duplicates keys and root node.
constructor: 
accepts key of the root Node

search(key, search_node):
Input:integer key in the array and optional start search node (the default is root Node)
Output:the node with the given key

add():
Input: key of Integer type, parent node key, boolean is right child.
Output: True or False.

Q1 - Print Ancestors :
Given a Binary Tree and a key, write a function that prints all the ancestors of the key in the given binary tree.
I built it as an attribute of the Binary Tree getAncestors(key):
Input: key of type Integer
Output: list of all the ancestors of the key in the given binary tree

Q2 - Common Ancestor 
Design an algorithm and write code to find the lowest common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure:
I built it as an attribute of the Binary Tree commonAncestor(key1,key2):
Input: 2 Keys of type Integer
Output: the lowest common ancestor of two nodes in a binary tree
