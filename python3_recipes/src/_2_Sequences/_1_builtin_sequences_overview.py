import collections
import array

# 1. Grouping sequences by the type of objects they contain:

## Problem
### Which Sequences to use when the objects they contain must be of same type?

## Answer
###  Flat Sequences: str, bytes, bytearray, memoryview, array.array
comment = 'Python3 is awesome'
print(type(comment))
print(type(comment[0]))
print(type(comment[1]))

## Discussion
### Flat Sequences store the value of each item they contain within their own memory space
### Thus they are more compact in memory but they are limited to holding primitive values like characters, bytes and numbers



## Problem
###  Which Sequences to use when the inner objects can be of different types?

## Answer
###  Container Sequences: list, tuple, collections.deque
a_string = 'a string'
an_integer = 10
a_float = 4.1

a_list = [a_string, an_integer, a_float]
a_tuple = (a_string, an_integer, a_float,)
a_deque = collections.deque([a_string, an_integer, a_float])

print(a_list)
print(a_tuple)
print(a_deque)

## Discussion
### Unlike Flat Sequences, Container Sequences store a reference to the objects the contain and not the objects themselves
### Thus, they can store inner objects of any type, which gives more flexibility but is less compact in memory.


#---

# 2. Grouping sequences by mutability

## Problem
### Which Sequences allow in-place updates?

## Answer
### Mutable Sequences: list, bytearray, array.array, collections.deque
comments = ['Python3 is great', 'Yes, I agree']
print(id(comments))   #<0>

comments[0] = 'Python3 is GREAT' #<1>
print(comments)
print(id(comments))   #<2>

comments.append('Yeah, me too !')  #<3>
print(len(comments))
print(comments)
print(id(comments))

comments.pop()   #<4>
print(len(comments))
print(comments)
print(id(comments))

## Discussion
### <0> print the id of the python comments object in memory
### <1> in-place update of the first comment to the same comments
### <2> the id is the same as before, proof that the update is indeed in-place on the same "comments" sequence object
### <3>, <4> adding or removing a comment are also in-place operations


## Problem
### Which Sequences DO NOT allow in-place updates?

## Answer
### Immutable Sequences: tuple, str, bytes
comments = ('python3 is great', 'Yes, I agree',)
print(type(comments))
# The line below throws an Error: TypeError: 'tuple' object does not support item assignment
comments[0] = 'Python3 is GREAT' #<0>


comment_1 = comments[0]
print(comment_1)
# The line below throws an Error: TypeError: 'str' object does not support item assignment
comment_1[0] = 'P'  #<1>

## Discussion
### <0> Throws an Error because tuple are immutable in Python, ie: once set, they can't be updated.
### <1> Same applies for str


