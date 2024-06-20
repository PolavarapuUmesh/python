dict={"role":"devops","exp":"5"}
print(dict["role"])

# it removes all the duplicate items
set={1,2,1,3,4,4}
print(len(set))

# if you want to remove a string you can remove by using remove method 
env=["user","employee","customer"]
env.remove("customer")
print(env)

# this is used to add a string at last position
env=["friend","enemy","well_wisher"]
env.append("mutual")
print(env)

# length 
length=[12,3,4,4,5]
env=len(length)
print(env)

# read input from the user
name=input("enter your name:")
age=int(input("how old are you:"))
print(input)

guess=["rabhani","yadav","22.3","88","mutton tastes good"]
print("88" not in guess)
