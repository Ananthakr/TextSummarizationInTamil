#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py4j.java_gateway import JavaGateway
import re

tense=[0,0,0]
def extractData(sen):
    result=""
    prev=""
    sen=re.sub(r"[<>]",'',sen)
    for word in sen.split():
        #print word
        if(word=="Noun" and prev!="Interrogative"):
            result+=prev+"-"

        if(word=="Verb" and prev!="Auxiliary" and prev!="Finite"):
            result += prev + "-"

        if(word=="Entity"):
            result += prev + "-"

        if(word=="Auxiliary"):
            result += prev + "-"

        if(word=="Finite" and prev!="Negative"):
            result += prev + "-"

        if(word=="Adverb"):
            result += prev + "-"

        if(word=="Adjective" and prev!="Demonstrative"):
            result += prev + "-"

        if(word=="Negative"):
            result += prev + "-"

        if(word=="Past"):
            tense[0]+=1

        if (word == "Present"):
            tense[1] += 1

        if (word == "Future"):
            tense[2] += 1
        prev=word
    return result

def analyseSent(sen):
    gateway=JavaGateway()
    #sen="இறைமறுப்பு என்றால் மீவியற்கை கூறுகளை கேள்விக்குட்படுத்தலைக் குறிக்குமா அல்லது இல்லாத ஒன்றைப் பற்றி நிலைப்பாடு எடுக்கமுடியாது என்பதைப் பற்றிய நிலைப்பாடா அல்லது தெளிவாக இறை என்பதை நேரடியாக மறுக்கும் கொள்கையா என்று வெவ்வேறு கருத்துக்கள் உள்ளன"
    analysedSen=gateway.entry_point.analyseSent(sen)
    #print analysedSen
    x=''.join(analysedSen.splitlines())
    return extractData(x)

def analyseSummary(summary):
    notes=""
    for sen in summary.split('. '):
        notes+=analyseSent(sen)

    notes=notes[:-1]
    max_tense = tense.index(max(tense))
    #print tense
    if(max_tense==0):
        notes+="\nTense : Past "
    elif(max_tense==1):
        notes+="\nTense : Present "
    elif(max_tense==2):
        notes+="\nTense : Future "

    return notes


if __name__=='__main__':
    summary=raw_input("Enter summary:")
    print analyseSummary(summary)