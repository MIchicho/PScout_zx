#!/usr/bin/env python
# coding=utf-8


path = "/home/chicho/Psout/jellybean_allmappings"

dest_path = "/home/chicho/Psout/allmappings.txt"

f=open(path)

outf=open(dest_path,"w+")

for line in f.readlines():
    if line.startswith("<") or line.startswith("("):
        messageList = line.split()
        del messageList[len(messageList)-1]
        messageInfo = " ".join(messageList)
        outf.write(messageInfo + "\n")
    else:
        outf.write(line)

f.close()
outf.close()


