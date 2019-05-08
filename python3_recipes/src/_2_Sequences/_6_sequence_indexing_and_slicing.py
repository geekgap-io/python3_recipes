## Problem
### What are the various ways to index an element or a subset of elements in a sequence

## Answer
###  Use sequence indexing syntax: [start:end:step], in Python end excluded from the interval
s = 'Python3'
print(s[0:4])       #<0>
print(s[0:4:2])     #<1>
print(s[3:])        #<2>
print(s[:4])        #<3>
print(s[::-1])      #<4>
print(s[0])         #<5>
print(s[-1])        #<6>
try:
    print(s[50])    #<7>
except Exception as e:
    print(e)



csv_file_content = '''
Python3        Guido       1989
C++            Bjarne      1979       
C              Dennis      1969'''

language = slice(0,15)      #<8>
inventor = slice(15, 27)    #<8>
year = slice(27, 31)        #<8>

for line in csv_file_content.split('\n')[1:]:
    print('{} was invented in {} by {}'.format(line[language], line[year], line[inventor]))

## Discussion
### <0> Only get the characters from 0 to 3. YES to 3 because end=4 is excluded
### <1> Do the same but skip 1 character each time
### <2> Start from 3 but go till the end
### <3> Only tke the first 4 characters
### <4> get the reversed sequence
### <5> get only a the first element of the sequence
### <6> get the last one
### <7> index 50 is out of range so an exception is raised
### <8> we can also make use of the named slice to parse structured information and make the code more readable
