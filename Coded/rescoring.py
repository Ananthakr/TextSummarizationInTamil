#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

keys_1=[]
keys_2=[]
keys_3=[]

def checkAvail(se,pat):
    patr=r''+pat
    mf=re.search(patr,se)
    '''if mf:
        print "found"
    else:
        print "not found"'''
    return mf

def rescoreSent(sen,keys):
    scr=0;

    for tri in keys['tri']:
        res=checkAvail(sen,tri[0])
        if(res):
            scr=tri[1]/10

    for bi in keys['bi']:
        res = checkAvail(sen, bi[0])
        if (res):
            scr = bi[1]/(2*10)

    for uni in keys['uni']:
        res = checkAvail(sen, uni[0])
        if (res):
                scr = uni[1]/(3*10)

    return scr

def rescoringDoc(text,keys):
    rescrDoc=[]
    for sen in text.keys():
        text[sen]+=rescoreSent(sen,keys)
        rescrDoc.append(text[sen])
        #print text[sen]
    return rescrDoc

if __name__=='__main__':
    sent=raw_input("Enter the sentence list")
    keys_1=raw_input("Enter unigram keyphrases")
    keys_2=raw_input("Enter bigram keyphrases")
    keys_3=raw_input("Enter trigram keyphrases")
    sent="இறை நம்பிக்கைகள் தோன்றிய காலம் தொட்டே, அத்தகைய நம்பிக்கைகளை கேள்விக்குட்படுத்திய, ஐயப்பட்ட, மறுத்த நிலைப்பாடுகளும் இருந்து வந்திருக்கின்றன. இந்திய மெய்யியலில் பொருளியவாத, இறைமறுப்புக் கொள்கையை உலகாயதம் முன்னிறுத்தியது.[1] பெளத்தம், சமணம் ஆகியவையும் உலகை படைக்கும், பாதுகாக்கும், அழிக்கும் பண்புகளைக் கொண்ட கடவுளை அல்லது கடவுள்களை நிராகரித்தன. மேற்குலக, கிரேக்க மெய்யியலில் Epicureanism, Sophism போன்று மெய்யியல்கள் இறைமறுப்பு கொள்கைகளைக் கொண்டிருந்தன. அறிவொளிக் காலத்தைத் தொடந்த அறிவியலின் வளர்ச்சி பல்வேறு வகைகளில் பொருளியவாத, இறைமறுப்புக் கோட்படுகளுக்கு கூடிய ஆதாரங்களையும் வாதங்களையும் வழங்கி உள்ளது. 2000 களில் ஐக்கிய அமெரிக்காவிலும், ஐரோப்பாவிலும் அப்போது விரிபு பெற்று வந்த சமய தீவரவாதத்தை எதிர்த்து புதிய இறைமறுப்பு எழுந்தது"
    pat="காலம் தொட்டே"

