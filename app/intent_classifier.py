import numpy as np
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import OneHotEncoder
from keras import Sequential
from keras.models import load_model
from keras.layers import Dense, Dropout, Input
from starlette.responses import Response
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import random
import time
from fastapi.responses import JSONResponse

from app.prediction.career import growth_rate
from app.service.job import job_seek
from app.service.pdf import pdf_search
from app.service.video import scrape_video
from app.service.universal import scrape_text


stop_words = stopwords.words('english')

def clean_corpus(corpus):
  corpus = [ doc.lower() for doc in corpus]
  cleaned_corpus = []
  
  stop_words = stopwords.words('english')
  wordnet_lemmatizer = WordNetLemmatizer()

  for doc in corpus:
    tokens = word_tokenize(doc)
    cleaned_sentence = [] 
    for token in tokens: 
      if token not in stop_words and token.isalpha(): 
        cleaned_sentence.append(wordnet_lemmatizer.lemmatize(token)) 
    cleaned_corpus.append(' '.join(cleaned_sentence))
  return cleaned_corpus

with open('app/nlp/intents.json', 'r',encoding='utf-8') as file:
  intents = json.load(file)

corpus = []
tags = []

for intent in intents['intents']:
    for pattern in intent['patterns']:
        corpus.append(pattern)
        tags.append(intent['tag'])

cleaned_corpus = clean_corpus(corpus)

vectorizer = TfidfVectorizer()
encoder = OneHotEncoder()
X = vectorizer.fit_transform(cleaned_corpus)
y = encoder.fit_transform(np.array(tags).reshape(-1,1))

model = load_model('app/nlp/chatbot.hdf5')

INTENT_NOT_FOUND_THRESHOLD = 0.93

def predict_intent_tag(message):
  message = clean_corpus([message])
  X_test = vectorizer.transform(message)
  
  y = model.predict(X_test.toarray()) 

  if y.max() < INTENT_NOT_FOUND_THRESHOLD:
    return 'noanswer'
  
  prediction = np.zeros_like(y[0])
  prediction[y.argmax()] = 1
  tag = encoder.inverse_transform([prediction])[0][0]
  return tag

def get_intent(tag):
  
  for intent in intents['intents']:
    if intent['tag'] == tag:
      return intent

job_list = []
rand = ['🤖Bot is thinking...', 'Hang on tight⌛', 'Gathering best results for you...🔍']


def search(query:dict):    
    tag = predict_intent_tag(query["message"])
    intent = get_intent(tag)
    
    if intent != None and intent['tag'] == 'greeting' and query["flow"] == 'EMPTY':
      response = random.choice(intent['responses'])
      data =  {"template":1,"message": [response],"flow": "EMPTY","num":-1}
      data = json.dumps(data)
      print(data)
      return Response(content=data, media_type="text/plain; charset=utf-8")
    
    elif query["flow"] == 'career' or (intent != None and intent['tag'] == 'career'):
      # if query["num"] == -1:
      #   flow = "career"
      #   num = 1
      #   data = {"template":1,"message": ["Please refer the below website to get an insight of all the skills👇", "https://marcresi.github.io/CareerList/"], "flow": flow,"num": num}
      #   Response(content=data, media_type="text/plain; charset=utf-8")

      # else:
      #   career_list = growth_rate(query["message"])
      return {"template":3,"message":["Click here for more info"],"flow":"career","num":-1}
      
    elif query['flow'] == 'job' or (intent != None and intent['tag'] == 'job'):

      if query['num'] == -1 :
        flow = "job"
        num = 1
        return {"template":1,"message": ["Enter the Job Role"],"flow": flow,"num": num}

      if query['num'] == 1 :
        job_list.append(query['message'])
        flow = "job"
        num = 2
        return {"template":1,"message": ["Enter the Job Location"],"flow": flow,"num": num}
      
      if query["num"] == 2 :
        job_list.append(query['message'])
        flow = "job"
        num = 3
        return {"template":1,"message": ["Enter the Job Type : [FULLTIME, PARTTIME, CONTRACTOR, INTERNSHIP]"],"flow": flow,"num": num}
      
      if query["num"] == 3 :
        job_list.append(query['message'])
        print(job_list)
        job_res = job_seek(job_list)
        job_list.clear()
        if job_res != None:
          flow = "EMPTY"
          num = -1
          data  = {"template":2,"message": job_res,"flow": flow,"num": num}
          data = json.dumps(data)
          return Response(content=data,media_type="text/plain; charset=utf-8")
        else:
          flow = "EMPTY"
          num = -1
          data = {"template":1,"message": ["Sorry, Pragati couldn't find jobs for you 😔"],"flow": flow,"num": num}
          json_data = json.dumps(data, ensure_ascii=False).encode("utf-8")
          return JSONResponse(content=json_data, media_type="application/json; charset=utf-8")

        
    elif intent != None and (intent['tag'] == 'goodbye' or intent['tag'] == 'thanks'):
      response = random.choice(intent['responses'])
      return {"template":1,"message": [response],"flow": "EMPTY","num":-1}
    
    #TODO
    elif intent != None and intent['tag'] == 'college':
      return {"template":3,"message": ["Click here for more info"],"flow": "college","num":-1}

    #TODO
    elif intent != None and (intent['tag'] == 'subject' or  intent['tag'] == 'stream'):
      return {"template":3,"message": ["Click here for more info"],"flow": "subject","num":-1}
  
    
    # elif intent != None and intent['tag'] != 'document' and intent['tag'] != 'video':
    #   response = random.choice(intent['responses'])
    #   return {"message": response,"flow": "EMPTY","num":-1}
    
    elif intent != None and intent['tag'] == 'document':
      pdf_res = pdf_search(query["message"])
      pdf_res.insert(0,"Refer the below Material")
      return {"template":4,"message": pdf_res,"flow": "document","num":-1}

    elif intent != None and intent['tag'] == 'video':
      vid_res = scrape_video(query)
      vid_res.insert(0,"Refer the below Video")
      return {"template":4,"message": vid_res,"flow": "video","num":-1}

    else:
      print("Universal Scraping")
      res = scrape_text(query["message"])
      return res


      
    