# value is available in the list so the result is true
app=["vedantu","zepto","youtube"]
print("zepto" in app)

# value is available in the list so the result is not_true
not_app=["umesh","python","fb"]
print("umesh" not in not_app)

# how to remove elements from a list by using remove method 
language=["telugu","hindi","maths"]
games=["chess","cricket","volleyball"]
games.append("tennis")
print(games)

# if we want add an element to set can we use add method .set doen't allow append method
num = {1, 2, 3, 4}
num.add(5)
print(num)

# items are preseted in list and to remove one string from the elements section we may use remove method
fruits=["apple","banana","grapes","water"]
fruits.remove("water")
print(fruits)

#
healthy=["chicken","mutton","vegetables"]
not_healthy=["alchol","cigar","vegetables"]
if "vegetables" not in not_healthy:
    not_healthyhealthy.remove("alchol,cigar")
print(not_healthy)


healthy=["food","sleep","gym"]
not_healthy=["overthinking","eating_junk_food","gym"]
print(id(not_healthy))
not_healthy[:]=[item for item in not_healthy if item in healthy]
print(id(not_healthy))
print(not_healthy)

#replace a string of characters
original_string=["hello how are you"]
modified_string=original_string[0].replace("how are you", "how was you'r day")
print(modified_string)

#length of the list and here len is a function
conversation=["hi", "are you ok with what you have"]
print(len(conversation))

#print position of a string in the list
i=["l1","l2","f1","f2"]
print(i[3])
print(len(i))

#remove an object from the list 
n=["green","blue","red"]
n.remove("red")
print(n)

#
a=["let","me","complete","first"]
for i in range(len(a)): 
    print(a[i])
range(0, 1)

#counting elements in a lsit 
container=["pod1","deploy","service","hpa","pod1","pod1"]
print(container.count("pod1"))

#sets 
bucket1=["images","logs","files","videos"]
bucket2={"images","logs","code","files"}
print("files" not in bucket2)

#it is to print item count & item in a single set
bucket1=["images","logs","files","videos","logs"]
counts=[[bucket1.count(item), item] for item in set(bucket1)]
print(counts)

#count how many items in a list
bucket2=["groups","roles","users","policies","roles"]
item=[bucket2.count(item) for item in set(bucket2)]
print(item)

#
from collections import Counter
list=["i1","i2","i3","i2","i1"]
print(Counter(list))    

# collentions in python
from collections import Counter
a="aaabbbbdhdhhhfjjjjj" 
my_counter=Counter(a)
print(set(my_counter.most_common(2)))

#
l1=["aq","we"]
l2=["ie","oe"]
print(len(l1), GeneratorExit(l2))


#
set=("wed","thu")
list=["l1","l2"]
print(len(set), (list))

#
ipl=["srh","mi","rcb","csk"]
ipl.remove("csk")
print(ipl)

# it counts the characters of a string
bike_companies=["honda","suzuki","tvs","tvs","honda","hero"]
from collections import Counter
print(Counter("bike_companies"))

# combine a lists and print 
working_days=["mon","tues","wen","thur","fri"]
non_working_days=["sat","sun"]
all_working_days = working_days + non_working_days
print("days per a week :")
for day in all_working_days:
    print(day)

# insert a string to a list
groceries=["vegitables","meat","milk","eggs"]
groceries.insert(4, "chocolates")
print(groceries)

# methods in list insert,delete,append,extend
list=["hello","hi","thankyou"]
print("original list:", list)
list.append("ok")
print("list after appending(ok):", list)
list.remove("ok")
print("list after removing(ok):", list)
list.extend([7,8,9])
print("list after extending(7,8,9):", list)
del list[0]
print("list after deleting index 0:", list)
print("final list element:")
for elements in list:
    print(elements)
    