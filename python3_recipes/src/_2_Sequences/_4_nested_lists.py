## Problem
### Suppose you maintain an e-commerce store and currently have 3 customers with 6 items in sale,
### You would like to keep an updated record of the scores each customer gives to a purchased item.
### How could you do that using lists

## Answer
### We can use a list of lists. The outer list representing the the customers and the inner list the items.
### We can initialize a list of list with all elements to None initialy and update once a customer purchase and review and item
### However there is a wrong and a right way to initialize a list of list: Let's start with the wrong way.

### The wrong way:
reviews = [[None] * 6] * 3 #<0>
print(reviews)

# Let's say customer 2 purchases and reviews item 6 with a score of 3.9
reviews[1][5] = 3.9 #<1>
print(reviews) #<2>

print(id(reviews[0])) #<3>
print(id(reviews[1])) #<3>
print(id(reviews[2])) #<3>


### The right way: with (nested) list comprehension
reviews = [[None] * 6 for i in range(3)]  #<4>
#reviews = [[None for j in range(6)] for i in range(3)] #is also good
print(reviews)

# Let's say customer 2 purchases and reviews item 6 with a score of 3.9
reviews[1][5] = 3.9 #<5>
print(reviews) #<6>

print(id(reviews[0])) #<7>
print(id(reviews[1])) #<7>
print(id(reviews[2])) #<7>

## Discussion
### <0> Wrong initialization of a list of lists.
### <1, 2> Because the initialization was done poorly, editing a single cell causes changes elsewhere.
### <3> For proof we can see the all the elements of the outer list are merely references pointing to the same inner list object: The id in memory is the same.

### <4> Right initialization of a list of lists.
### <5, 6> Because the initialization was done correctly, editing a single cell doesn't causes changes elsewhere.
### <7> For proof we can see each element in the outer list is a reference pointing to a different inner list object: The id in memory are different.

#---