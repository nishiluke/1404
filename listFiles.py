import os
print("The  file s and folders in {} are :".format(os.getcwd()))
items = os.listdir('.')
for item in items:
    print(item)