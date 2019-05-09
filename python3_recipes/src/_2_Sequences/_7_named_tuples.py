from collections import namedtuple

## Problem
### Your code is getting harder to read because you are accessing sequences elements by indices all over the place
### How can you make it cleaner

## Answer
###  Use named tuples
Date = namedtuple('Date', ['day', 'month', 'year'])
Comment = namedtuple('Comment', ['author', 'content', 'likes', 'date'])

comment1 = Comment('Junior', 'Python3 is awesome', 10, Date(9, 5, 2019))    #<0>
print(comment1)
print(comment1.author)  #<1>
print(comment1[0])  #<1>
print(comment1.author == comment1[0]) #<1>

print(comment1.date.year) #<2>
print(comment1.date[2]) #<2>

comment2 = Comment(date=Date(9, 5, year=2019), author='Jr', likes=15, content='Python3 is really cool') #<3>
print(comment2)
_, comment_content, likes, date = comment2  #<4>
print(comment_content)
print(likes)
print(date.month)

print(isinstance(date, tuple), isinstance(comment1, tuple), isinstance(comment2, tuple)) #<5>

## Discussion
### <0> Initialization of named tuples is the same as for regurlar tuples and could be nested
### <1> each element could be accessed either by index or name; both are perfectly equivalent with the later being much more readable
### <2> we can access nested named tuple elements too
### <3> named tuples initialization can be done with positional or keyword arguments, or both.
### <4> tuple unpacking still applies.
### <5> in fact a namedtuple is just a special type of tuple.
