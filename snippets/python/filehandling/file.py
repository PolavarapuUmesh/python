import os
print(os.chdir('/home/umesh/Desktop/python-programs/snippets/python/filehandling/'))

f=open('test.txt','r')
print(f.name)
f.close()

#using with context manager
with open('test.txt','r') as f:
    f_content=f.read()
    print(f_content)