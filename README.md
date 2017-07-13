# First-Assignment

I am Computer Engineering student at the Hebrew University third year as part of CodeU program at Google for students we should submit this assignment

Q1: is_permutation.py: contains a function is_permutation(str1 = "", str2 = "") input: two strings output: if one is a permutation of the other

Q2: I made Node class : the consturactor accepts data to initialize the data, the default is 0. the data is only integer type. and set and get methods of the next node and the data.

linked_list class: I built singly linked list: Singly Linked Lists are a type of data structure. It is a type of list. In a singly linked list each node in the list stores the contents of the node and a pointer or reference to the next node in the list. It does not store any pointer or reference to the previous node. (from wikibooks) constructor: accepts one integer or list of integers or default 0: the linked list consist of the head node according to the data that given in the constructor. add_Node: accepts data of integer type, no default value. adding new node with the given data to the list. changeNode: accepts index if the node to be changed, starting from 1, and data of integer type, no default value. change the data of the node with the given index. getData: k - index of the k element in the linked list starting from 1. find the kth to last element of a singly linked list. output: list of the kth to last element of a singly linked list.

# CodeU Assignment - 2
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

# CodeU Assignment - 5 
unknown language is our 5 assignment. 
Given a dictionary (a list of words in lexicographic order) of all words in an unknown/invented language, find the alphabet (an ordered list of characters) of that language.

This language can contain any character (of the native char data type). Upper/lower case characters are treated differently for simplicity. Assume standard lexicographical ordering (order by characters from left to right, if X is a prefix of Y then X is sorted before Y), just with an unknown order of characters.

Write a function that will receive an ordered list of strings, and returns an ordered list of characters.

Example input: [ART, RAT, CAT, CAR]. Solution: [A, T, R, C].

I have created Graph class:
Constructor: The Graph consists of ordered Vertices such as
        every slot in vertices will contain keys: alphabet and values: tree tuple type
        (isvisit,list of adj, degree)
        isvisit - mark the vertex as visited or no.
        list of adj - all vertices the consist edges in the graph such as v --> u
                    v character before u character at the language.
        degree - the number of characters before v.            
        
Add_Edge: given v->u edge, adding all adjacents vertices u to v list of adj.
add_vertex: add new valid vertex (character)
recTopologicalSort: recursive method to find the topological order of characters of the given language
topologicalSort: find the topological order of characters 
findAllTogiticalPaths: The main function that converts the problem of the dictionary to graph of vertices that represent
    the characters of the language and the edges are v --> u
    v character before u character at the language.
    after that finding the specific order using the topological order algorithm.
main; testing findAllTogiticalPaths.

