# -*- encoding = 'utf-8' -*-
import jieba
def cutText(text):
    file = open(text,'r',encoding='utf-8')
    seg_text = file.read()
    words = jieba.lcut(seg_text)
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


res1 = cutText('orig.txt')
res = removeStopwords(res1)
print(res)

