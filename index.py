import os

# for dirpath, dirnames,  filenames in os.walk('/'):
#     print(dirpath)

[dirpath, dirnames,  filenames] = os.walk('/')
print(dirpath)