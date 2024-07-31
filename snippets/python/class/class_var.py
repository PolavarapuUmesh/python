class counter:
    count=0
    def __init__(self):
        counter.count +=1
    def get_count(self):
        return counter.count
counter1 = counter()
counter2 = counter()
print(counter1.get_count)
print(counter2.get_count)