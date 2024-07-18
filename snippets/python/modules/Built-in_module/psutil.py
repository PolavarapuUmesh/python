import psutil,os,time

pid = os.fork()

if pid == 0: 
    print("Child process")
    time.sleep(5)  
    print("Child process exiting")
else:
    print("Parent process")
    print("Child process ID:", pid)
    time.sleep(10) 
    print("Parent process exiting")