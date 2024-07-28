class employee:       #employee class uses pass to create an empty class definition
    pass              #pass is a statemnet that gives you to skip for now and use it further use
emp1=employee()       #emp1 is a instance variable 
emp2=employee()       #emp2 is a instance variable
emp3=employee()       #emp3 is a instance variable 
print(emp1,emp2,emp3) 

emp1.first="polavarapu" #assigned attribute to the emp1 instance variable
emp1.last="umesh"
emp1.email="umeshpolavarapu71@gmail.com"
emp1.pay=20,000

emp2.first="polavarapu"
emp2.last="suresh"
emp2.email="sureshpolavarapu71@gmail.com"
emp2.pay=70,000

emp3.first="polavarapu"
emp3.last="rajanessh"
emp3.email="rajaneeshpolavarapu@gmail.com"
emp3.pay=4,00,000

print(emp1.email,emp2.email,emp3.email)

