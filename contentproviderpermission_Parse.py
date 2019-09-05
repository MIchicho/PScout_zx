#!/usr/bin/env python
# coding=utf-8
# filename  :  contentproviderpermission_Parse.py
# Author    :  Chicho
# Date      :  Aug 3, 2016

import os
import sys

contentProPermission_dict={}

originPath = "/home/chicho/Psout/jellybean_contentproviderpermission.txt"

logPath = "/home/chicho/Psout/test1.log"

f = open(originPath)

contentPermissionMap={}

for line in f.readlines():
    conProPerInfo = line.split()
    length = len(conProPerInfo)
    contentProvider = conProPerInfo[0]
    permission = conProPerInfo[length-1]

    if contentProvider not in contentPermissionMap:
        contentPermissionMap[contentProvider]=permission


    cmd = '''egrep -o {0} {1} >> contentPerMappingResult'''.format(contentProvider,logPath)
    os.system(cmd)
    print "The processing is running..."


f.close()

#print contentPermissionMap

#sys.exit(0)

path = os.path.dirname(logPath)

contentProFilePath = os.path.join(path,"contentPerMappingResult")

countContentPermissionMap={}

if os.path.exists(contentProFilePath):
    fcont = open(contentProFilePath)

    for line in fcont.readlines():
        valueList=[]
        conInfo = line.split("\n")[0]
        permission = contentPermissionMap[conInfo]
        if conInfo not in countContentPermissionMap:
            valueList.append(permission)
            valueList.append(1)
            countContentPermissionMap[conInfo]=valueList
        else:
            tmpValueList = countContentPermissionMap[conInfo]
            tmpValueList[1] += 1
            countContentPermissionMap[conInfo] = tmpValueList



    for cp in countContentPermissionMap:
        cmd = '''echo {0},  {1},  {2} >> countContentPermission'''.format(cp,countContentPermissionMap[cp][0],countContentPermissionMap[cp][1])
        os.system(cmd)
        



print "The work is done!"
