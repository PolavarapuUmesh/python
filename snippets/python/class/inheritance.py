#class_inheritance
class job:
    def __init__(self,name):
        self.name=name 
    def dev(self):
        return 'employee got some increment'
class salary(job):
    def dev(self):
        return "happy"
tax=salary("income")
print(tax.dev)

