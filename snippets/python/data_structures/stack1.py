stack=[]
def push():
    element = input("enter the element:")
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("remove element:",e)
        print(stack)