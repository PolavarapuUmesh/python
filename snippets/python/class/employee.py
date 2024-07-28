class employee:            #employee class uses pass to create an empty class definition
    def __init__(self,first,last,email,pay):
        self.first=first
        self.last=last
        self.email=email
        self.pay=pay       #pass is a statemnet that gives you to skip for now and use it further use
emp1=employee("polavarapu","umesh","umeshpolavarapu71@gmail.com",20000)            #emp1 is a instance variable 
emp2=employee("polavarapu","suresh","sureshpolavarapu71@gmail.com",70000)            #emp2 is a instance variable
emp3=employee("polavarapu","rajaneesh","rajaneeshpolavrapu@gmail.com",400000)            #emp3 is a instance variable 

print("employees first name:",[emp1.first,emp2.first,emp3.first])
print("employees last name:",[emp1.last,emp2.last,emp3.last])
print("employees email:",[emp1.email,emp2.email,emp3.email])
print("employees pay:",[emp1.pay,emp2.pay,emp3.pay])
