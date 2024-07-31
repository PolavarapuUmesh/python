#basic class 
class person:
    def __init__(self,name,age):    #__init__ cunstructor (this is a special method that initialize the class with name and age attributes)
        self.name = name
        self.age = age
    def bio(self):                  # Method (bio): A method that returns a greeting string using the class attributes.
        return f"Hello,my name is {self.name}and my age is {self.age}"
person1 = person("sesi",23)         # Usage: An instance of Person is created with the name "sesi" and age 23. The bio method is called to print a bio.
print(person1.bio)

