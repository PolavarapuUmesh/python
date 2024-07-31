#read input fro the user
name=str(input("enter your name:"))
age=int(input("enter your age:"))
print(name)
print(age)

#string
input=['a','b','c','d']
str=''.join(input)
print(str)

#it prints common items in the lists 
a=['math','eng','tel','hin','ps']
b=['soc','bio','tel','hin','eng']
print(set(a)&set(b))

#diff b/w 2
vu=[1,2,3,4,5]
klu=[1,2,3]
print(set(vu)-set(klu))

#max num in list
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list([1, 2, -8, 0]))

#frequency of elements
import collections
elements=[1,22,33,21,122,2435,45,99]
print("original_list:",elements)
changes=collections.Counter(elements)
print("after changes over:",changes)

#permutations
import itertools
print(list(itertools.permutations([1,2,3])))

#remove duplicates values
def remove_duplicates(lst):
    return  list(dict.fromkeys(lst))
a = [10,20,30,20,10,50,60,40,80,50,40]
no_duplicates=remove_duplicates(a)
print(no_duplicates)

