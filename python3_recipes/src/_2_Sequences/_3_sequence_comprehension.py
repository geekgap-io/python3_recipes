## Problem
### Uppercasing all the comments without using map

## Answer
###  we can use sequence comprehension which are much more concise and readable
comments = [
    'Python3 is awesome',
    'Indeed, python3 is great',
    'Absolutely ... Could not agree more !'
]
uppercased_comments1 = [comment.upper() for comment in comments] #<0>
uppercased_comments2 = [str.upper(comment) for comment in comments] #<1>
print(comments) #<2>
print(uppercased_comments1)
print(uppercased_comments2)

## Discussion
### <0> list comprehension: each element of the new list being a transformation of the original one using the .upper() of the object
### <1> list comprehension: each element of the new list being a transformation of the original one using the str.upper() function
### <0, 1> both ways are much more cleaner and concise than the approach using map (see recipe 2.2)
### <2> The original comments list is unchanged

#---

## Problem
### Filtering only the comments with strictly more than 20 characters without using filter

## Answer
###  we can use sequence comprehension with an if clause
filtered_comments = [comment for comment in comments if len(comment) > 20] #<0>
print(filtered_comments)
print(comments) #<1>

## Discussion
### <0> adding an if clause to the element of the original list on the right hand side of the comprehension enables filtering which ones appear on the left side
### <1> The original comments list is unchanged
