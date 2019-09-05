#!/usr/bin/env python
# coding=utf-8



import os 

originFilePath = "/home/chicho/Psout/test.log"

dest_path = "/home/chicho/Psout/allmappings.txt"


f = open(originFilePath)

#destFile = open(dest_path,"w+")

for line in f.readlines():
    if line.startswith("[AI]"):
        classInfo = line.split(" ")[4].split(";")[0].split("L")[1]
        classList =classInfo.split("/")
        className = ".".join(classList)
        methodName = line.split(" ")[5]
        cmd = '''grep -e  {0}  {1} | grep {2} >> apimapPermisssion_result.txt'''.format(className,dest_path,methodName)
        os.system(cmd)
        print className, methodName
        print "The processing is runnging..."



f.close()
#destFile.close()

print "The work is done!"
