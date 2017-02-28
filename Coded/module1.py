#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py4j.java_gateway import JavaGateway
import re


sentences = []
wordsCount = 0
senCount  = 0

def loadandPrepareDoc():
    gateway = JavaGateway()
    #entire document
    file=open("dataset/doc1.txt",'r+')
    doc=file.read()

    #splitted as paragraphs
    para=doc.split('\n')

    doc=re.sub(r"\n"," ",doc)
    #splitted as sentences
    sen_split=doc.split('.')

    global wordsCount
    global senCount

    #init for adding sentences and stem them
    sentences_stemmed=[]
    st_scr=[]
    #print len(sen_split)-1
    for i in range(len(sen_split)-1):

        wordsCount += len(sen_split[i].split())
        senCount += 1

        # here each sentence is picked and sent via py4j to stem
        #print sen_split[i]+"==>"
        sen_split[i]=re.sub(r"[','\"\"`~$#@%^&*()!?<>{}\/\\+=-_]", '', sen_split[i])
        sentences.append(sen_split[i])
        temp=gateway.entry_point.stemSent(sen_split[i])

        # <***> like words are stripped from the output of stemming
        temp = re.sub('[<\w+>]', '', temp)
        temp=re.sub('\n',' ',temp)
        if(temp!=''):
            sentences_stemmed.append(temp)
            #print temp


    return sentences_stemmed

if __name__=='__main__':
    for s in loadandPrepareDoc():
        print s