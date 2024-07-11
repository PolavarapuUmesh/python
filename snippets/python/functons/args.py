#*args parameter(non keyword arguments)
def fun(*args):
    for arg in args:
        print(arg)
fun(18,3,422,2)

#*args practise 1
def school(*names):
    for arg in names:
        print("school_name:")
        print(arg)
school("bashyam","mont","kkr","st'jhons")

#iterate the fun
def num(*order):
    print(order)
    for i in order:
        print(i)
num(1,2,3,4,5)

#*args practise2
def cal(a,b):
    return a+b
    print(add)
cal(1,2)

#*args practise3
def sum_values(*num):
    result=0
    for i in num:
        result = result+i
    return result
total=sum_values(1,2,3,4,5)
print(total)
