#!/usr/bin/env python
# coding=utf-8
import os

oriPath = "/home/chicho/Psout/allmappings.txt"

apiPerMappingDict = {}

f=open(oriPath)

lineList=f.readlines()

lineList.reverse()

methodList=[]

for line in lineList:
    if line.startswith("(") or line.startswith("<"):
        methodList.append(line)
        continue
    if line.startswith("Permission"):
        permission = line.split(":")[1].split("\n")[0]
        countMethod =len(methodList)
        apiPerMappingDict[permission]=methodList
        methodList=[]


#print apiPerMappingDict

oneTOoneMap={}
fout="/home/chicho/Psout/apiPerMappingDict_re"

mapfile=open(fout,"w+")

parse_resultPath="/home/chicho/Psout/apimapPermisssion_result.txt"

f=open(parse_resultPath)

countMap={}
for line in f.readlines(): # line is the paresed method from log and match the apiPermission 
    for key in apiPerMappingDict:
        vl=apiPerMappingDict[key]
        if line in vl:
            if key not in countMap:
                countMap[key]=1
            else:
                countMap[key]+=1
            break

mapfile.write(str(countMap))
print countMap

mapfile.close()
'''

for key in apiPerMappingDict:
    vl=apiPerMappingDict[key]
    for method in vl:
        cmd = key + "  " + method
        mapfile.write(cmd)


        oneTOoneMap[method]=key

mapfile.close()
'''

#for line in f.readlines():
#    if line.startswith("Permission"):
#        permission = line.split(":")[1]
#        if permission not in apiPerMappingDict:
#            tmpMethodList=[]
#        
#        continue
#    if line.startswith("(") or line.startswith("<"):
#        tmpMethodList.append(line)
