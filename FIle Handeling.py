import os
def writing(filename,text):
    f = open(filename,"w")
    f.write(text)
    f.close()
def append(filename,text):
    f = open(filename,"a")
    f.write(text)
    f.close()
def reading(filename):
    try:
        f = open(filename,"r")
        text = f.read()
        print(text)
        f.close()
    except FileNotFoundError as e:
        print(e)
def searching(filename,word):
    try:
        f = open(filename,"r")
        linecount = 0
        for line in f.readlines():
            linecount+=1
            strlist = line.split(" ")
            wordcount = 0
            for j in strlist:
                wordcount+=1
                if(j==word):
                    return(linecount,wordcount)
        else:
            return None
    except FileNotFoundError as e:
        print(e)
def modify(filename,oldword,newword):
    t = searching(filename,oldword)
    if(t!=None):
        myList = []
        try:
            f = open(filename,"r")
            for line in f.readlines():
                line = line.replace(oldword,newword)
                myList.append(line)
            f.close()
            f = open(filename,"w")
            f.write(''.join(myList))
            f.close()
        except FileNotFoundError as e:
            print(e)
    else:
        print("Search Failed")

os.rename("file1.txt","file.txt")

modify("file1.txt","AdarshI","Adarsh I")

print("Success")