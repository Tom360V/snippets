#!/usr/bin/env python
import os
import shutil

def copyFiles(src, dst, size):
    print "src:" + src
    for f in os.listdir(src) :
        b = os.path.getsize(src+f)
        print "check file: " + f + " size: " + str(b)
        if(b > size):
            print "copy: " + src+f + " -> " + dst
            shutil.copy2(src+f, dst)
        else:
            print f + " to small:" + str(b)

def isJPG(file):
    try:
        im=Image.open(filename)
        print True
    except IOError:
        print False

def renameFiles(path):
    idx=0
    ext_to_skip = ["py", "sh", "jpg"]
#    ext_to_skip = ["py", "sh"]
    
    for f in os.listdir(path) :
        if(not os.path.isfile(f)):
            continue
        splitted = f.split(".")
        body = splitted[0]
        
        if len(splitted) == 1 :
            ext = ""
        else:
            ext = splitted[1]
        
        if ext in ext_to_skip:
            print "skip '" + f + "'"
        else:
#            if( isJPG(f) == False ):
#                print f + " is not a jpg"
#                continue
            file_already_exist = True
            while (file_already_exist):
                idx+=1
                newName = "img_" + str(idx).zfill(3) + ".jpg"
                file_already_exist = os.path.exists(newName)
                
            os.rename(f, newName)
            print "renamed " + f + " to " + newName
            
if __name__ == "__main__":
    src = "/cygdrive/c/Users/tkoene/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
    dst = "./"
    copyFiles(src, dst, 100000)
    renameFiles(dst)
    print "done"