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

#
bucket1=["images","logs","files","videos","logs"]
counts=[[bucket1.count(item), item] for item in set(bucket1)]
print(counts)

