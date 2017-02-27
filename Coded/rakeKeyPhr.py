import rake.rake as rake
import operator

#data/docs/fao_test/w2167e.txt

rake_obj_uni = rake.Rake("tamilStopList.txt",6,1,2)
rake_obj_bi = rake.Rake("tamilStopList.txt",6,2,1)
rake_obj_tri = rake.Rake("tamilStopList.txt",6,3,1)

'''
***use RAKE to extract keywords
***i/p: sentences i arraylist
***o/p: 2d array with string and score
'''
def getKeys(sent):
    bi=[]
    tri=[]
    uni=[]
    keys = {}

    #get unigram and scores
    uni=rake_obj_uni.run(sent)[0:10]

    #get bigram and scores
    bi=rake_obj_bi.run(sent)[0:10]

    #get trigram and scores
    tri=rake_obj_tri.run(sent)[0:10]

    keys['uni']=uni
    keys['bi']=bi
    keys['tri']=tri

    return keys

if __name__=='__main__':
    sample_file = open("dummy.txt", 'r')
    text = sample_file.read()
    keywords=getKeys(text)

    print("keywords: ")
    for i in keywords.keys():
        for j in keywords[i]:
            print(j[0]+" "+str(j[1]))
