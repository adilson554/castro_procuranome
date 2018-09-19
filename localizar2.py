#!/usr/bin/python
#-*- coding: utf-8 -*-
nao = ';   nao    ;'
sim = ';   sim    ;'





search = [" nome1",  " nome2"]
print len(search)


i = 0
while i<len(search):
        MsgOk= sim + search[i]
        MsgNok= nao + search[i]
        def check():

                datafile = file("seguro.txt")

                for line in datafile:
                        if search[i] in line:
                                found = True
                                break
                        else:
                                found = False
                return found

        if check():
            print MsgOk
        else:
            print MsgNok
        i = i + 1
