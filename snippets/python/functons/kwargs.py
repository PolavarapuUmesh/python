#**kwargs(keyword arguments)
def data(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
data(name="umesh",age=24,email="umeshpolavarapu71@gmail.com")

#**kwargs practise 1
def alphanum(**order):
    print(order)
alphanum(a=1,b=2,c=3)

#iterate **kwargs 
def env(**order):
    print(order)
    for key,value in order.items():
        print(key,value)
env(prod=2,dev=6,test=1,preprod=3)