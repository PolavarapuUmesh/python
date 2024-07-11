#local variables
def fun():
    i=3
    print("Declared_a_local_var:",i)
fun()

#gloabal_variable
i=20
def fun():
    g=10
    print("Declared_a_global_var:")
    print(g)
fun()
print(i)

#global_keyword
q=100
def fun():
    global q
    print("global_keyword:")
    q=200
    print(q)
fun()
print(q)

#functions
def ipl_teams(prediction):
    print("calling_fun:")
    print(f"mi {prediction}!")
    print(f"srh {prediction}!")
ipl_teams("loss")
ipl_teams("win")

#testing the buit-in functions
print(type(3))
print(type("sortout"))
print(type(print))
print(type(len))

#global_var
s="let me go"
def fun():
    global s
    s="let me wait for some time"
    print(s)
fun()
print(s)

#nonlocal_variables
def outer():
    a=9
    def inner():
        nonlocal a
        a=17
        print(a)
    inner ()
    print(a)
outer()

#functions_practise1
def msg(name):
    print("hello,"+name)
msg("umesh")
msg("ganesh")


#
def fun(grammer):
    print("let me,"+grammer)
fun("check")
fun("verify")

#add 2 fun
def add(a,b,c):
    return a+b+c
result=add(22,34,-11)
print(result)

#return_value
def num(c,d):
    mul=2*8
    print(mul)

#
def math(y,t):
    sub=y-t
    return sub


    