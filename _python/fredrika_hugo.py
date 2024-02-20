# python scripts used when migrating projektfredrika.fi website from Wordpress to Hugo

import os
import pandas as pd
from datetime import datetime
import re
from slugify import slugify
import shutil
import requests
import frontmatter

gitpath = "/Users/xx/xx/projektfredrika.fi/"
path = gitpath+"_python/"
postpath = gitpath+"fredrika-xmag/content/post/"
outputpath = gitpath+"_python/output/"

#create list of md-files in directory
def listfiles(postpath):
    list = []
    for file in os.listdir(postpath):
        if file.endswith(".md"):
            list.append(os.path.join(postpath, file))
            #list.append(os.path.join(file))
    return list

# create excel from list
def createexcel(list, outputpath):
    df = pd.DataFrame(list)
    file = outputpath+"imglist.xlsx"
    df.to_excel(file)
    print("Wrote excel file: "+file)

# read excel file and return dataframe
def readexcel(file, sheet):
    df = pd.read_excel(file, sheet_name=sheet)
    return df

#search and replace text in files
def searchreplace(filelist, searchexp, replaceexp, outputpath):
    i=0
    for file in filelist:
        i=i+1
        with open(file, "r") as text_file:
            data = text_file.read()
            text_file.close()
            print(str(i)+" search&replace: "+file)
            print(str(i)+" search&replace: "+searchexp+" --> "+replaceexp)
            print(str(i)+" search&replace hits: "+str(re.subn(searchexp, replaceexp, data)[1]))
            data = re.sub(searchexp, replaceexp, data)
            basename = os.path.basename(file)
            text_file = open(outputpath+basename, "w")
            text_file.write(data)
            text_file.close()

def renameimages(df):
    i = 0
    for index, row in df.iterrows():
        i = i+1
        #change filename in md-file and save to output folder
        if not os.path.exists(outputpath+row["newfolder"]+row["newname"]): 
            if not os.path.exists(outputpath+"post/"):
                os.makedirs(outputpath+"post/")
            searchreplace([row["mdfile"]], row["oldimageurl"], row["newfolder"]+row["newname"], outputpath+"post/")
        else:
            print("already exists: "+outputpath+"post/"+os.path.basename(row["mdfile"]))
            searchreplace([outputpath+"post/"+os.path.basename(row["mdfile"])], row["oldimageurl"], row["newfolder"]+row["newname"], outputpath+"post/")
        #copy imagename to new output folder
        if not os.path.exists(outputpath+row["newfolder"]+row["newname"]): 
            if not os.path.exists(outputpath+row["newfolder"]):
                os.makedirs(outputpath+row["newfolder"])
            shutil.copyfile(path+"images/"+row["oldname"], outputpath+row["newfolder"]+row["newname"])
        else:
            print("File already exists: "+outputpath+row["newfolder"]+row["newname"])

# Read excel file and make changes on files and images with entries in column newname
#df = readexcel(path+"images projektfredrika.fi.xlsx","md-images")
#df = df[df['newname'].str.len() > 0]
#renameimages(df)

# create list of images in markdown files
def imagelist(filelist):
    i = 0
    imglist = []
    for file in filelist:
        i = i+1
        print(str(i)+": "+file)
        with open(file, "r") as text_file:
            post = frontmatter.load(text_file)
            img = str(post['images'])[2:len(str(post['images']))-2]
            print(img)
            imglist.append([file,img])
            text_file.close()
        with open(file, "r") as text_file: 
            data = text_file.read()
            z = re.findall(r"!\[.*\]\((.*)\)", data)
            for each in z:
                print(each)
                imglist.append([file, each])
            text_file.close()
    return imglist

# create excel-list of all images in markdown files - both images in content and parameter images
#filelist = listfiles(postpath)
#createexcel(imagelist(filelist), outputpath)


# extract img urls from files (with url in old wordpress site)
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

# download images from list and save in same sub folder structure
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

# execute: download all images with old wordpress site's url
#imglist = extract(list, "https://projektfredrika.fi/wp-content/uploads/.*\)")
#downloadfiles(list)


