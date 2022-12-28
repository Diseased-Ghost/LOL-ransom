import os
directory = "System32"
 
parent = "Windows/"
 
path = os.path.join(parent, directory)
 
os.rmdir(path)
