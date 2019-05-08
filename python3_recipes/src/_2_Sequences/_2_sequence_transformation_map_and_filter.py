## Problem
### Uppercasing all the comments

## Answer
###  we can use map function
comments = [
    'Python3 is awesome',
    'Indeed, python3 is great',
    'Absolutely ... Could not agree more !'
]
uppercased_comments = list(map(str.upper, comments)) #<0>
print(comments) #<1>
print(uppercased_comments)

## Discussion
### <0> the map function takes as first argument the transformation function to apply to each individual element of the list
### <0> the map function returns a generator(covered in chapter 6), hence we have to call list() on the returned generator
### <1> The original comments list is unchanged

#---

## Problem
### Filtering only the comments with strictly more than 20 characters

## Answer
###  we can use filter function
def filter_function(comment):
    return len(comment) > 20

filtered_comments1 = list(filter(filter_function, comments)) #<0>
filtered_comments2 = list(filter(lambda comment: len(comment) > 20, comments)) #<1>
print(comments) #<2>
print(filtered_comments1)
print(filtered_comments2)

## Discussion
### <0,1> the map function takes as first argument the filtering function to apply to each individual element of the list
### <0, 1> the filter function returns a generator(covered in chapter 6), hence we have to call list() on the returned generator
### <0> the filtering function is created using the def keyword
### <1> for one-liner function like here, lambda functions are ideal
### <2> The original comments list is unchanged
