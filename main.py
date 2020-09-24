# -*- encoding = 'utf-8' -*-
#coding = gbk
import jieba
import jieba.analyse
import hashlib
import sys
import math
def cutText(text):
    file = open(text,'r',encoding='utf-8')
    seg_text = file.read()
    words_len = len(list(jieba.lcut(seg_text)))
    topK_num = math.ceil(0.08 * words_len)
    words = jieba.analyse.extract_tags(seg_text,topK=topK_num)
    file.close()
    return words
# def removeStopwords(text):
#     keywords = []
#     stopwords = open('stopwords.txt','r',encoding='utf--8')
#     seg_stopwords = stopwords.read()
#     for word in text:
#         if word not in seg_stopwords:
#             keywords.append(word)
#     return keywords
def getSimhash(str):
    vector = [0] * 128
    i = 0
    size = len(str)
    for word in str:
        #利用MD5获得字符串的hash值
        md5 = hashlib.md5()
        md5.update(word.encode("utf-8"))
        hash_value = bin(int(md5.hexdigest(),16))[2:]
        if len(hash_value) < 128:#hash值少于128位，需在低位以0补齐
            dif = 128 - len(hash_value)
            for d in range(dif):
                hash_value += '0'
        #加权 合并
        for j in range(len(vector)):
            if hash_value[j] == '1':
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
    return simHash_value
def getDistance(hash1,hash2):
    distance = 0
    if(len(hash1) != len(hash2)):
        distance = -1
    else:
        for i in range(len(hash1)):
            if(hash1[i] != hash2[i]):
                distance += 1
    return distance
def getSimilarity(hash1,hash2):
    return 0.01 * (100 - getDistance(hash1,hash2) * 100 / 128)

if __name__ == '__main__':
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    path3 = sys.argv[3]
    keywords_text1 = cutText(path1)
    keywords_text2 = cutText(path2)
    simHash_value1 = getSimhash(keywords_text1)
    simHash_value2 = getSimhash(keywords_text2)
    sim = getSimilarity(simHash_value1,simHash_value2)
    answer_file = open(path3,'w',encoding='utf-8')
    answer_file.write(str(sim))
    answer_file.close()





    #return vector
#print(getSimhash('16456456656'))
# print(getSimhash(cutText('orig.txt')))
# print(getSimhash(cutText('orig_0.8_add.txt')))
#print(cutText('orig.txt'))
# print(getSimhash())
    







# res1 = cutText('orig.txt')
# res = removeStopwords(res1)
#print(res)

