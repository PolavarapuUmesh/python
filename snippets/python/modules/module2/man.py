from mod import add,sub,mul

a=float(input("enter number1:"))
b=float(input("enter number2:"))
select_option=int(input("Enter 1 for addition or Enter 2 for subtraction & Enter 3 for multiplication"))
if select_option == 1: #if the user entered 1st option the statement will pass
    result = add(a,b)
    print("The result of addition is:",result)
elif select_option == 2: #if the user entered 2nd option the statement will pass
    result = sub(a,b)
    print("The result of subtraction is:",result)
elif select_option == 3: #if the user entered 3rd option the statement will pass
    result = mul(a,b)
    print("The result of multiplication:",result)
else:
    print("you have choosen the wrong option") #if you are not choosen 1 or 2 option it will print this statemnet 

#import--> is a built-in keyword
#module--> at where the module you are going to perform on

