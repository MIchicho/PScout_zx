#!/usr/bin/env python
# coding=utf-8

import os 

originFilePath = "/home/chicho/Psout/publishedapimapping.txt"


#f = open(originFilePath)


className = "android.bluetooth.BluetoothAdapter"
methodName = "getUuids()"
cmd = "grep -e " + '"'+className +'" '+ originFilePath +"|" + "grep "+ '"'+ methodName +'" '+">> re.txt"
print cmd 
os.system(cmd)
#print className, methodName
print "The processing is runnging..."



#f.close()
#destFile.close()

print "The work is done!"
