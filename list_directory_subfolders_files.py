#https://stackoverflow.com/questions/2909975/python-list-directory-subdirectory-and-files

import os, time

def listFiles1(root): # listdir
    allFiles = []; walk = [root]
    while walk:
        folder = walk.pop(0)+"/"; items = os.listdir(folder) # items = folders + files
        for i in items: i=folder+i; (walk if os.path.isdir(i) else allFiles).append(i)
    return allFiles

def listFiles2(root): # listdir/join (takes ~1.4x as long) (and uses '\\' instead)
    allFiles = []; walk = [root]
    while walk:
        folder = walk.pop(0); items = os.listdir(folder) # items = folders + files
        for i in items: i=os.path.join(folder,i); (walk if os.path.isdir(i) else allFiles).append(i)
    return allFiles

def listFiles3(root): # walk (takes ~1.5x as long)
    allFiles = []
    for folder, folders, files in os.walk(root):
        for file in files: allFiles+=[folder.replace("\\","/")+"/"+file] # folder+"\\"+file still ~1.5x
    return allFiles

def listFiles4(root): # walk/join (takes ~1.6x as long) (and uses '\\' instead)
    allFiles = []
    for folder, folders, files in os.walk(root):
        for file in files: allFiles+=[os.path.join(folder,file)]
    return allFiles


for i in range(100): files = listFiles1("src") # warm up

start = time.time()
for i in range(100): files = listFiles1("src") # listdir
print("Time taken: %.2fs"%(time.time()-start)) # 0.28s

start = time.time()
for i in range(100): files = listFiles2("src") # listdir and join
print("Time taken: %.2fs"%(time.time()-start)) # 0.38s

start = time.time()
for i in range(100): files = listFiles3("src") # walk
print("Time taken: %.2fs"%(time.time()-start)) # 0.42s

start = time.time()
for i in range(100): files = listFiles4("src") # walk and join
print("Time taken: %.2fs"%(time.time()-start)) # 0.47s