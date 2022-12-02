# python scripts for editing md-files

import os
import pandas as pd
from datetime import datetime
import re
from slugify import slugify
import shutil
import requests

gitpath = "/Users/xx/xx/xx/"
path = gitpath+"_python/"
oldpath = gitpath+"fredrika-xmag/content/post/"
newpath = gitpath+"_python/output/"

#create list of md-files in directory
def listfiles(oldpath):
    list = []
    for file in os.listdir(oldpath):
        if file.endswith(".md"):
            #list.append(os.path.join(oldpath, file))
            list.append(os.path.join(file))
    return list

#replace text in files
def updatefile(oldpath, newpath, filelist, searchexp, replaceexp):
    i=0
    for file in filelist:
        i=i+1
        #if i>1:
        #    break
        text_file = open(oldpath+file, "r")
        data = text_file.read()
        text_file.close()
        print(str(i)+" Old: "+oldpath+file)
        data = re.sub(searchexp, replaceexp, data)
        text_file = open(newpath+file, "w")
        text_file.write(data)
        text_file.close()
        print(str(i)+" New: "+newpath+file)

# extract img urls from files
def extract(list, searchexp):
    i=0
    imglist = []
    for file in list:
        i=i+1
        text_file = open(file, "r")
        data = text_file.read()
        text_file.close()
        print(str(i)+" "+file)
        z = re.findall(searchexp, data)
        for each in z:
            print(each[:-1])
            imglist.append(each[:-1])
    return imglist

def downloadfiles(list):
    i = 0
    for url in list:
        i = i+1
        print(i)
        filename = url.replace("https://projektfredrika.fi/wp-content/uploads/", "").split("/")
        path1 = filename[0]
        path2 = filename[1]
        file = filename[2]
        fullpath = newpath+path1+"/"+path2+"/"
        if not os.path.exists(newpath+"/"+path1):
            os.makedirs(newpath+"/"+path1)
        if not os.path.exists(newpath+"/"+path1+"/"+path2):
            os.makedirs(newpath+"/"+path1+"/"+path2)
        print(url)
        print(filename)
        res = requests.get(url, stream = True)
        if res.status_code == 200:
            with open(fullpath+file,'wb') as f:
                shutil.copyfileobj(res.raw, f)
                print('Image sucessfully Downloaded: ',fullpath+file)
        else:
            print('Image Couldn\'t be retrieved:', url)

#imglist = extract(list, "https://projektfredrika.fi/wp-content/uploads/.*\)")
#downloadfiles(list)

searchexp = "---[\n]*!.*\)\n"
replaceexp = "---"
filelist = listfiles(oldpath)
updatefile(oldpath, newpath, filelist, searchexp, replaceexp)
