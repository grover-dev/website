#Usage:
#Asks for type of addition: title, text, image
#For title, text can just paste text
#for image add path
#Can then ask to preview which launches flask app
#If works, can then export to given path (image auto placed)

#import statements:
import shutil, os
from os import path

print("Web Page Gen v1.0")

while 1:
    print("Enter name of the page:")
    name = input() + '.html'
    if path.exists(name):
        print("file already exists, please pick new name")
    else:
        break

file = open(name, 'w')
head = """{% extends "template.html" %}
{% block content %}
"""
file.write(head)
print("file name:", name)
imageArr = []
while 1:
    print("input file type (h-header/t-text/i-image/q-quit)")
    lineType = input().lower()
    if lineType == 'q':
        break
    if not ((lineType == 'h') or (lineType == 't') or lineType == 'i'):
        print("unknown filetype, re-enter of quit")
    else:
        if lineType == 'h':
            print("input header")
            text = input()
            headerPrefix = """<h1 class="post">"""
            headerSuffix = """</h1>
            """
            file.write(headerPrefix + text + headerSuffix)
        elif lineType == 't':
            print("input text")
            text = input()
            textPrefix = """<p class="post">"""
            textSuffix = """</p>
            """
            file.write(textPrefix + text + textSuffix)
        else:
            print("input path to image")
            pathStr = input()
            #TODO: pull src name from the path, also clone the image into local location
            if path.exists(pathStr):
                print("input image alt name")
                imageName = input()
                pathStr = path.realpath(pathStr)
                head, tailOrg = path.split(pathStr)
                imageArr.append(tailOrg)
                head, tail = path.split(path.realpath(file.name))
                shutil.copy(pathStr, head + "\\" + tailOrg)
                textPrefix = """<img class="post" alt = \" """ + imageName + """ \" src = \" """ + tailOrg + " \">" + """
                """
                file.write(textPrefix)
            else:
                print("file not found")
bottom = """{% endblock %}"""
file.write(bottom)
fileName = file.name
file.close
while 1:
    print("move to final destination?(y/n)")
    ans = input().lower()
    if not ((ans == "y") or (ans == "n")):
        print("unknown respons, re-enter")
    elif ans == "y":
        print("input destination")
        dst = input()
        dst = path.realpath(dst)
        if path.exists(dst):
            head, tail = path.split(path.realpath(fileName))
            shutil.copy(path.realpath(fileName), dst +"\\"+tail)
            #os.remove(path.realpath(fileName))
            for pos in imageArr:
                shutil.copy(head+"\\"+str(pos), dst +"\\"+str(pos))
                #os.remove(head+"\\"+imageArr[pos])
            print("moving successful")
            while 1:
                print("delete local copy?(y/n)")
                delteAns = input().lower()
                if not ((delteAns == "y") or (delteAns == "n")):
                    print("unknown respons, re-enter")
                else:
                    os.remove(path.realpath(fileName))
                    for pos in imageArr:
                        os.remove(head+"\\"+pos)
                    break
            break
        else:
            print("destination not found")
    else:
        break