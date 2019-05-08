## Problem
### You have a sequence for which the lenght is known, with each element representing a specific information depending on its index
### How do you get access to each piece of information in the sequence without using indexing syntax

## Answer
###  Use sequence unpacking
comment = ('Junior', 'Python3 is awesome', 5, (8, 5, 2019))
comment_author, comment_content, likes, date = comment #<0>
print(comment_author)
print(comment_content)
print(likes)
print(date)

_, comment_content, _, (day, month, year) = comment #<1>
print(comment_content)
print(day)
print(month)
print(year)


## Discussion
### <0> we are able to unpack each specific information according to its position in the sequence
### <1> we can even unpack nested elements like the day, month and year in the date and ignore some elements if we want to using underscore _

#---

## Problem
### You have a sequence for which the lenght is unknown, but you know useful informations are usually located at the ends
### How do you get access to the head or tail element of a sequence for which the length is not known

## Answer
###  Use sequence unpacking

# getting the best and worse reviews of different movies
reviews_movie1 = sorted([3.1, 4.5, 2.6, 4.8]) #<0>
reviews_movie2 = sorted([5.0, 4.2, 3.4, 2.1, 4.1, 4.7, 3.9]) #<0>

worse_movie1, *middle, best_movie1 = reviews_movie1 #<1>
worse_movie2, *_, best_movie2 = reviews_movie2 #<2>

print(reviews_movie1)
print(worse_movie1)
print(best_movie1)
print(middle)

print(reviews_movie2)
print(worse_movie2)
print(best_movie2)


## Discussion
### <0> sort each movie reviews in ascending order
### <1> get the worse and best reviews and also all the others in the middle
### <2> get the worse and best reviews and ignore all the others.
