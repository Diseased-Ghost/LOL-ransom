import os
if __name__ == "__main__":
    for (root,dirs,files) in os.walk('.', topdown=True):
        print (root)
        print (dirs)
        print (files)
        print ('--------------------------------')
