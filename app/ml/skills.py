import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import json
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import SequenceMatcher

def prediction(list1):
    
    data = pd.read_csv('app/dataset/final_updated_dataset.csv')
    jobs=data['jobs'].tolist()
    skills=data.columns.tolist()
    skills.pop(0)
    
    skill_list=[]
    for i in list1:
        for j in skills:
            if SequenceMatcher(None, i,j).ratio()>0.7:
                skill_list.append(j)
                
#     print("skill_list :",skill_list)
    if(len(skill_list)==0):
        return False
    l2 = []
    for x in range(0,len(skills)):
        l2.append(0)
    
    X = data[skills]
    y = data[["jobs"]]
    a = np.ravel(y)
    a = a[1:]
    X = X.iloc[1:]
    
    f=open('app/dataset/career_data.json',encoding='utf-8')
    json_data = json.load(f)
    # data
    li=[]
    for i in range(0,len(json_data)):
        sen=""
        for j in json_data[i]['skill']:
            sen+=j+" "
        li.append(sen)

    d = pd.Series(li)

    
    vectorizer = TfidfVectorizer()
    feature_vectors = vectorizer.fit_transform(data)
    similarity = cosine_similarity(feature_vectors)
    li=[]
    model = MultinomialNB()
    model=model.fit(X,a)
    for k in range(0,len(skills)):
        for z in skill_list:
            if(z==skills[k]):
                l2[k]=1
    
    inputtest = [l2]
    predict = model.predict(inputtest)
    predicted = predict[0]
#     print("predicted : ",predicted)
    close_match = difflib.get_close_matches(predicted,jobs)
    print("close_match : " ,close_match)
    j=0
    i=0
    for i,j in enumerate(jobs):
        if(j==predicted):
#             print('done')
            break
    index = i
    similarity_score = list(enumerate(similarity[index]))
    
    sort = sorted(similarity_score,key = lambda x:x[1], reverse= True)
#     print("sort :",so
    new_sort=[]
    for i in sort:
        if(i[1]>0.6):
            new_sort.append(i)

    i=1
    for jobs in new_sort:
        ind = jobs[0]
        if ind==0:
            continue
        elif ind>255:
            continue
        else:    
            title = data[data.index==ind]['jobs'].values[0]
            li.append(title)
    return close_match


# sk=['finance','accounting']
# res = prediction(sk)
# print("RESULT :",res)