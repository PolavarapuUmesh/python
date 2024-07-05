<<<<<<< HEAD
news=['tv5','1,2,3','abn'] 
print(news[0:2:2])
=======
news=['tv5','1,2,3','abn']
news.append('tv9') 
print(news)

# methods in list insert,delete,append,extend
list=["hello","hi","thankyou"]
print("original list:", list)
list.append("ok")
print("list after appending:", list)
list.remove("ok")
print("list after removing:", list)
list.extend([7,8,9])
print("list after extending(7,8,9):", list)
del list[0]
print("list after deleting index 0:", list)
print("final list element:")
for elements in list:
    print(elements)

#insert a sring to list
workingdays=["mon","tue","wed","fri","sat","sun"]
print(workingdays[4])
workingdays.insert(3, "thu")
print(workingdays)

#remove a element from a list 
employee_name=["umesh","sai","ashok","praveen"]
del employee_name[2]
print(employee_name)

#pop method 
employee_id=["181fa070001","181fa70002"]
popped=employee_id.pop(1)
print("just removed:", popped)

#
ap_elections=["ncbn","pk","sharmi","paul"]
ap_elections.append("jagu")
del ap_elections[4]
print(ap_elections)

#
aws_services=["ec2","vpc","rds","waf","alb"]
popped=aws_services.pop(4)
print("just removed",popped)
print(aws_services)

#slicing with del operator
cars=["honda","hyndai","tata","benz","benz"]
del cars[cars.index("tata"): cars.index("tata") +2]
print(cars)

#
working_days=["mon","tue","wed","thu","fri","sat","sun"]
del working_days[working_days.index("sat"):workingdays.index("sat")+ 2 ]
print("those days are working days:", working_days)

#
food_items=["milk","bread","jam","chapathi","dosa","jam","jam"]
while food_items.count("jam") > 0:
    food_items.remove("jam")
print(food_items)

#
sports=["cricket","kabadi","tennis","football","basketball"]
for item in sports:
    if item == "football":
        sports.extend(item)
print(sports)

# use for loop
squares=[]
for i in range(8):
    squares.append(i * i)
print(squares)

# list comprehensions
cricket_kit=["bat","ball","helmet","pads","guard","shoe","ball"]
print(id(cricket_kit))
cricket_kit[:]=[item for item in cricket_kit if item != "ball"]
print(id(cricket_kit))
print(cricket_kit)

#revrese function using list
list=[1,2,3,4,5,6,[1,23,34]]
print(id(list))
list.reverse()
print(list)

#reverse fun using list
list=[1,2,3,4,5]
copy_list=list[:]
copy_list.reverse()
print(list,copy_list)

#swap variable in list
me="umesh"
ved="office"
print(me,ved)
me,ved=ved,me
print(me,ved)

#swap example2
seq=[4,3]
not_seq=[2,3]
mem=seq
seq=not_seq
not_seq=mem
print(seq,not_seq)

#
aws_services=["vpc","ec2","elb","s3"]
print("list before swap:")
print(aws_services)
aws_services[0],aws_services[2]=aws_services[2],aws_services[0]
print("list after swap:")
print(aws_services)

#swap variables
Numbers=[4,2,3,1]
numeric=["a","b","c","d"]
position=Numbers
Numbers=numeric
numeric=position
print(Numbers,numeric)

#swap elements in the list
Num=[4,2,3,1]
print("id:",id(Num))
print("before swap:")
print(Num)
Num[0],Num[3]=Num[3],Num[0]
print("after swap:")
print(Num)

#swap position in element of list
storage_clasess=["fa","ia","aia","a","da"]
index=1
print(storage_clasess[index],storage_clasess[-index-2])
storage_clasess[index],storage_clasess[-index-2]=storage_clasess[-index-2],storage_clasess[index]
print(storage_clasess[index],storage_clasess[-index-2])

#reverse list by using algorithm(0)n 
s3=[1,2,3,4,5]
for index in range(len(s3)//2):
    s3[index],s3[-index-1]=s3[-index-1],s3[index]
print(s3)

#reverse iteration
s3=[1,2,3,4,5]
data_reversed=[]
for item in reversed(s3):
    data_reversed.append(item)
print(s3)
print(data_reversed)
    
#
name="umesh"
mobile="samsungs20fe"
mn=8977050507
for item in str(mn):
    print(item)
    
#reverse list with slicing 
l=[1,3,5,7,9]
print(id(l))
l=l[::-3]
print(id(l))
print(l)

#
keys=["num","alpha_num","alpha","spc","ins"]
popped=keys.pop(1)
print("i removed:",popped)
print(keys)

#
firstname="umesh"
lastname="polavarapu"
print(firstname)
print(lastname)
fullname=firstname+" "+lastname+ "."
print(fullname)

#
l=[11,33,44,55,334,443]
while 11 in l:
    l.remove(11)
print(l)

#
l=[11,33,44,55,334,443]
for item in l[:]:
    if item == 11:
        l.remove(item)
print(l)

#
l=[11,33,44,55,334,443]
for index in range(len(l) // 2):
    l[index],l[-index-1]=l[-index-1],l[index]
print(l)

#sort method prints in order
l=[11,33,44,22,334,443]
l.sort()
print(l)


#sort data in reverse order
l=[11,33,44,55,334,-443,0,-1]
print("before reversing a list:",l)
print("after revering a list:",(sorted(l,reverse=True)))

#
order=["aA","Aa","EWq","WWd","ssw","w"]
print(sorted(order))


>>>>>>> 3b2f1c3 (new python practices)
