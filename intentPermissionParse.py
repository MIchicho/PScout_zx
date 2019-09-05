#!/usr/bin/env python
# coding=utf-8
import os

intentPermission_dict={}

originPath = "/home/chicho/Psout/PScout/results/jellybean_intentpermissions"


destPath = "/home/chicho/Psout/test.log"

f = open(originPath)

intentdict={}

for line in f.readlines():
    intentInfo = line.split(" ")[0]
    permission = line.split()[1]
    valueList=[]
    if intentInfo not in intentdict:
        valueList.append(permission)
        valueList.append(1)
        intentdict[intentInfo]=valueList
    else:
        tmpValueList=intentdict[intentInfo]
        tmpValueList[1]+=1
        intentdict[intentInfo]=tmpValueList

    
    cmd = '''grep -e {0} {1} >> intentPerMappingResult'''.format(intentInfo,destPath)
    os.system(cmd)
    print "The processing is running..."


f.close()

path = os.path.dirname(destPath)

intentFilePath = os.path.join(path,"intentPerMappingResult")

intentList=[]

newIntentDict={}

if os.path.exists(intentFilePath):
    fint = open(intentFilePath)
    for line in fint.readlines():
        valueList=[]
        intentInfo = line.split(":")[1].split(")")[0]
        intentPermission = intentdict[intentInfo][0]
        if intentInfo not in newIntentDict:
            valueList.append(intentPermission)
            valueList.append(1)
            newIntentDict[intentInfo]=valueList
        else:
            tmpValueList = newIntentDict[intentInfo]
            tmpValueList[1] += 1
            newIntentDict[intentInfo]=tmpValueList

       # intentList.append(intentInfo)
       # uniqueIntent = set(intentList)

    #for intent in uniqueIntent:
    #    if intent in intentdict:
    #        cmd = '''echo {0} {1} >> countIntentPermission'''.format(intent,intentdict[intent])
    #        os.system(cmd)

    for intent in newIntentDict:
        cmd = '''echo {0},  {1},  {2} >> countIntentPermission'''.format(intent,newIntentDict[intent][0],newIntentDict[intent][1])
        os.system(cmd)





print "The Work is done!"
