#!/usr/bin/env python
# -*- coding: utf-8 -*-

from py4j.java_gateway import JavaGateway
import textRank
import rakeKeyPhr
import rescoring
import module1

'''
*** since scores are generated for stemmed sentences this
*** function relates the original sentence with its relevant final score
*** ip:sentence list and score array
*** op:array of objects with sen and scr as object elements
'''
def getFinalScore(sentences,scores):
    newSentences=[]
    i=0
    for sen in sentences:
        try:
            obj = {}
            obj['sen']=sen
            obj['scr']=scores[i]
            newSentences.append(obj)
            i+=1
        except:
            print "Error occured at index "+str(i)+" length of scores is: "+str(len(scores))
    return newSentences

'''
*** extracts sentences from the sorted objects list for creating final summary
*** op:sentence list and score array
*** ip:array of objects with sen and scr as object elements
'''
def getSentence(sentSorted):
    sentences=[]
    for s in sentSorted:
        sentences.append(s['sen'])
    return sentences

#load and stem the document imported from module1
print "Loading and stemming the document..."
sentences_stemmed=module1.loadandPrepareDoc()

#calling textrank and printing results
print "Calling TextRank..."
textRankscr=textRank.scoreWrapper(sentences_stemmed)
#for i in textRankscr.keys():
    #print textRankscr[i]


#calling rake module and print keywords
print "Calling RAKE..."
keywords=rakeKeyPhr.getKeys(sentences_stemmed)
#print("keywords: ")
#for i in keywords.keys():
#    for j in keywords[i]:
#        print(j[0]+" "+str(j[1]))

#rescoring function is called to generate new scores
print "Rescoring the sentences..."
res=rescoring.rescoringDoc(textRankscr,keywords)


#unstemmed sentences are added final scores
sentScored=getFinalScore(module1.sentences,res)

#for sorting the rescored list
print "Sorting the sentences..."
sentSorted = sorted(sentScored, key=lambda x: x['scr'], reverse=True)

#patch sentences and create summary
summary = '. '.join(getSentence(sentSorted))
summaryWords = summary.split()
summaryWords = summaryWords[0:101]
summary = ' '.join(summaryWords)

print "Summary:\n"+summary