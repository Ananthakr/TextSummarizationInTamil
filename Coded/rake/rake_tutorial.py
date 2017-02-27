#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
import six

__author__ = 'a_medelyan'

import rake
import operator
import io

# EXAMPLE ONE - SIMPLE
stoppath = "../tamilStopList.txt"

'''# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 5, 3, 4)

# 2. run on RAKE on a given text
sample_file = io.open("data/docs/fao_test/w2167e.txt", 'r',encoding="iso-8859-1")
text = sample_file.read()

keywords = rake_object.run(text)

# 3. print results
print("Keywords:", keywords)

print("----------")'''
# EXAMPLE TWO - BEHIND THE SCENES (from https://github.com/aneesha/RAKE/rake.py)

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath)

text = "சுரங்கத்தின் உள்ளிருந்து சத்தமின்றி படியேறிப் பாய்ந்து வந்த குளிர்க்காற்று அவன் தோளை வளைத்து இறுக்கி மார்பில் தன் அங்கங்களைப் பொருத்திக் கொண்டது " \
       "பிம்பிசாரன் மனம் வழியாக எண்ணற்ற புணர்ச்சி ஞாபகங்கள் பாய்ந்து சென்றன. நடுங்க வைக்கும் குளிர் ததும்பும் அந்த அணைப்பு அவனை உத்வேகம் கொள்ளச் செய்தது. " \
       "அஞ்சவும் வைத்தது."\
       "கொன்ற மிருகத்தின் உடலைக் கிழித்துப் புசிக்கும் புலியின் பாவனை அவனுக்கு புணர்ச்சியின் போது கூடுவதுண்டு." \
       "எதிர் உடல் ஒரு தடை, உடைக்க வேண்டியது. வெல்ல வேண்டியது." \
       " பின் சுய திருப்தியுடன் வாளை எடுத்தபடி வானைப் பார்ப்பது மிகவும் பிடிக்கும் அவனுக்கு."



# 1. Split text into sentences
sentenceList = rake.split_sentences(text)

for sentence in sentenceList:
    print("Sentence:", sentence)

# generate candidate keywords
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
print("Phrases:", phraseList)

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

# generate candidate keyword scores
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

# sort candidates by score to determine top-scoring keywords
sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# for example, you could just take the top third as the final keywords
for keyword in sortedKeywords[0:int(totalKeywords / 3)]:
    print("Keyword: ", keyword[0], ", score: ", keyword[1])

print(rake_object.run(text))
