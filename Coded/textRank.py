import io
import itertools
import os

import click
import networkx as nx
import nltk
from nltk.tokenize import RegexpTokenizer

'''@click.group()
def cli():
    pass
'''
#nltk.download('punkt')


def lDistance(firstString, secondString):
    """Function to find the Levenshtein distance between two words/sentences -
    gotten from http://rosettacode.org/wiki/Levenshtein_distance#Python
    """
    if len(firstString) > len(secondString):
        firstString, secondString = secondString, firstString
    distances = range(len(firstString) + 1)
    for index2, char2 in enumerate(secondString):
        newDistances = [index2 + 1]
        for index1, char1 in enumerate(firstString):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]


def buildGraph(nodes):
    """nodes - list of hashables that represents the nodes of the graph"""
    gr = nx.Graph()  # initialize an undirected graph
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))

    # add edges to the graph (weighted by Levenshtein distance)
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = lDistance(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)

    return gr




def extractSentences(text):
    # sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    # print text
    # sent_detector = RegexpTokenizer(r'\w+')
    # sentenceTokens = sent_detector.tokenize(text.strip())

    sentenceTokens = text.split('. ')

    for i in sentenceTokens:
        print i

    graph = buildGraph(sentenceTokens)
    print("Length of graph"+str(len(graph)))
    calculated_page_rank = nx.pagerank(graph, weight='weight')

    print "page rank"

    for p in calculated_page_rank.keys():
        print calculated_page_rank[p]


    # most important sentences in ascending order of importance
    sentences = sorted(calculated_page_rank, key=calculated_page_rank.get,
                       reverse=True)

    # return a 100 word summary
    summary = '. '.join(sentences)

    '''summaryWords = summary.split()
    summaryWords = summaryWords[0:101]
    summary = ' '.join(summaryWords)'''

    return summary

def scoreWrapper(sentenceTokens):

    graph = buildGraph(sentenceTokens)
    #print("Length of graph" + str(len(graph)))
    calculated_page_rank = nx.pagerank(graph, weight='weight')

    return calculated_page_rank


if __name__=='__main__':
    text = raw_input("Enter doc: ")
    summary = extractSentences(text)
    # keys=extractKeyphrases(text)
    print "Summary: " + summary
    # print "Keys: "+keys