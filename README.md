# First-Assignment

I am Computer Engineering student at the Hebrew University third year as part of CodeU program at Google for students we should submit this assignment

Q1: is_permutation.py: contains a function is_permutation(str1 = "", str2 = "") input: two strings output: if one is a permutation of the other

Q2: I made Node class : the consturactor accepts data to initialize the data, the default is 0. the data is only integer type. and set and get methods of the next node and the data.

linked_list class: I built singly linked list: Singly Linked Lists are a type of data structure. It is a type of list. In a singly linked list each node in the list stores the contents of the node and a pointer or reference to the next node in the list. It does not store any pointer or reference to the previous node. (from wikibooks) constructor: accepts one integer or list of integers or default 0: the linked list consist of the head node according to the data that given in the constructor. add_Node: accepts data of integer type, no default value. adding new node with the given data to the list. changeNode: accepts index if the node to be changed, starting from 1, and data of integer type, no default value. change the data of the node with the given index. getData: k - index of the k element in the linked list starting from 1. find the kth to last element of a singly linked list. output: list of the kth to last element of a singly linked list.

#Third-Assignment
Given a grid of letters and a dictionary, find all the words from the dictionary that can be formed in the grid. 
 
The rules for forming a word:
● You can start at any position.
● You can move to one of the 8 adjacent cells (horizontally/vertically/diagonally).
● You can't visit the same cell twice in the same word. 
 
Assume you have a dictionary class with these two methods:
● isWord(string): Returns whether the given string is a valid word.
● isPrefix(string): Returns whether the given string is a prefix of at least one word in the dictionary. 
 
Your function receives the number of rows, number of columns, a 2-dimensional array of characters (of the native char data type), and the dictionary. You should return the set of all words found. 
word_search.py cantains :
*Interface of Dictionary Class with two methods: as specify above.
*find_words_prefix: helper function
Input:
charecter - the charecter in the grid
i,j - indexes of the character
num_of_rows, num_of_columns: dims of the grid
grid: the grid list of 2Dim. of characters
dictionary: valid words
isVisit1: list of 2 dim of bool type specify if we visit the character and check if exist valid path.
valid_words: empty list - for the recursia (the output)

 word_search: the main function
 Input: as specify above
 output: list of valid words
 
 main:
 tests of valid and invalid inputs.
