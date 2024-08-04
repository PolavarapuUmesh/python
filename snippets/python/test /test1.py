# read input fro the user
import itertools
import collections
name = str(input("enter your name:"))
age = int(input("enter your age:"))
print(name)
print(age)

# string
input = ['a', 'b', 'c', 'd']
str = ''.join(input)
print(str)

# it prints common items in the lists
a = ['math', 'eng', 'tel', 'hin', 'ps']
b = ['soc', 'bio', 'tel', 'hin', 'eng']
print(set(a) & set(b))

# diff b/w 2
vu = [1, 2, 3, 4, 5]
klu = [1, 2, 3]
print(set(vu)-set(klu))

# max num in list


def max_num_in_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max


print(max_num_in_list([1, 2, -8, 0]))

# frequency of elements
elements = [1, 22, 33, 21, 122, 2435, 45, 99]
print("original_list:", elements)
changes = collections.Counter(elements)
print("after changes over:", changes)

# permutations
print(list(itertools.permutations([1, 2, 3])))

# remove duplicates values


def remove_duplicates(lst):
    return list(dict.fromkeys(lst))


a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
no_duplicates = remove_duplicates(a)
print(no_duplicates)

# functions


def add(num1, num2):    # with 2 arguments passed
    sum = num1+num2      # local variable sum works with in the function
    print("sum:", sum)


add(4, 99)              # add is a calling function
print("added two variables successfully")

# function with string arguments


def details(fname, lname):
    name = fname+" "+lname
    print("what is your full name:", name)


details("polavarapu", "umesh")


# continous arbitary arguments
def family(*kids):  # arbitary argument *-asterisk
    print("the youngest child is " + kids[1])


family("sai", "sesi")

# class


class Employee:
    def __init__(self, Name, age):
        self.name = name
        self.age = age
