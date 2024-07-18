import os
import time

pid = os.fork()

if pid == 0: # This is the child process
    print("Child process")
    time.sleep(5)  # Sleep for 5 seconds
    print("Child process exiting")
else:
    print("Parent process")
    print("Child process ID:", pid)
    time.sleep(10)  #
    print("Parent process exiting")