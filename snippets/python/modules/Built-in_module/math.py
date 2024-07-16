#math module
import math
print(math.pi)
print(math.pow(2,4))
print(math.sqrt(12))
print(math.ceil(2.1))
print(math.floor(1.9))
print(math.sin(45))
print(math.tan(45))
print(math.cos(0))
print(math.copysign(3,3))

#statstic module
import statistics
print(statistics.mean([1,24,21,54,2,33])) # it is gives avgerage value
print(statistics.median([1,2.23,3.2,22])) # gives mid vale
print(statistics.mode([292,273,33,2223,3.3,7.3])) # most repeated value
print(statistics.stdev([1.2,1.4,3.2,2.2,9])) # sample in form a list 

#system modules
import sys
print(sys.version_info)
print(sys.builtin_module_names)
print(sys.maxsize)
print(sys.path)

#os modules 
#to perform many tasks of operations
import os
print(os.rmdir("d:\\umesh"))
print(os.mkdir("d:\\umesh"))
print(os.getcwd())
print(os.chdir("d\\umesh"))
