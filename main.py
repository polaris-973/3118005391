# -*- encoding = 'utf-8' -*-
#coding = gbk
import jieba
import jieba.analyse
import hashlib
import math
import binascii
def cutText(text):
    file = open(text,'r',encoding='utf-8')
    seg_text = file.read()
    words_len = len(list(jieba.lcut(seg_text)))
    topK_num = math.ceil(0.08 * words_len)
    words = jieba.analyse.extract_tags(seg_text,topK=topK_num)
    file.close()
    return words
def removeStopwords(text):
    keywords = []
    stopwords = open('stopwords.txt','r',encoding='utf--8')
    seg_stopwords = stopwords.read()
    for word in text:
        if word not in seg_stopwords:
            keywords.append(word)
    return keywords
def getSimhash(str):
    vector = [128]
    i = 0
    size = len(str)
    for word in str:
        #利用MD5获得字符串的hash值
        md5 = hashlib.md5()
        md5.update(word.encode("utf-8"))
        hash_value = bin(int(md5.hexdigest(),16))[2:]
        #加权 合并
        for j in range(len(vector)):
            if hash_value[i] == '1':
                vector[j] += (10 - (i / (size / 10)))
            else:
                vector[j] -= (10 - (i / (size / 10)))
        i += 1
    #降维
    simHash_value = ''
    for x in range(len(vector)):
        if vector[x] <= 0:
            simHash_value += '0'
        else:
            simHash_value += '1'
    #return simHash_value
    return hash_value
#print(getSimhash('16456456656'))
print(getSimhash(cutText('orig.txt')))
#print(cutText('orig.txt'))
# print(getSimhash())
    







# res1 = cutText('orig.txt')
# res = removeStopwords(res1)
#print(res)

