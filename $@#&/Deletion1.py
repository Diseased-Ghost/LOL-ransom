import os
directory = "System32"
 
parent = "C:\Windows\"
 
path = os.path.join(parent, directory)
 
os.rmdir(path)
