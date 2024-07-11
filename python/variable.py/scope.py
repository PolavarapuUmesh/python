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