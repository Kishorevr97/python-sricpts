import random
import sys
import os
print(random.randint(1,7))
print(sys.argv[0], sys.argv[1])
print(sys.path)
print(os.getcwd())
os.chdir("/home/ubuntu")
print(os.getcwd())
print(os.listdir("/home/ubuntu"))
os.makedirs("kishore", exist_ok=True)
os.path.exist("/home/ubuntu")


