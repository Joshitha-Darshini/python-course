#create a tuple with different data tpes
tuplex= (4,6,2,8,3,1)
print(tuplex)
#create a tuple 
tuplex= (4,6,2,8,3,1)
print(tuplex)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple 
tuplex= tuplex + (9,)
print(tuplex)
#counts the number of occurances of item 50 froma tuple
tuple1= (50,10.60,70,50)
print(tuple1.count(50))
#create a tuple 
turplex=(2,4,3,5,4,6,7,8,6,1)
#used tuple [start:stop] the start index is inclusive and the stop index
_slice= tuplex[3:5]
#its exclusive
print(_slice)
#if the strat idex isn't defined, is taken from the beginning of the tuple
_slice=tuplex[:6]
print(_slice)