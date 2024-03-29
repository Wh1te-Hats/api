from app.ml.skills import prediction
import pandas as pd
import pymongo


def growth_rate(skill):
    
    res = []
    
    res.append('Here are some top suggestions📈 for a career matching your skillset...👇')

    client = pymongo.MongoClient(
    "mongodb+srv://harshil:shanu123@pragati.oeap8sk.mongodb.net/test")
    mydb = client["pragati"]
    mycol = mydb["growth_rate"]

    filcol = mycol.find()
    print(skill)

    if type(skill) == list:
        pskills = skill
    elif "\n" in skill:
        pskills = list(skill.split("\n"))
    elif "," in skill:
        pskills = list(skill.split(","))
    elif len(skill.split()) == 1:
        pskills = skill.split()
    else:
        return {"message":"Please separate your skills with a comma or mention it one below the other.", "error": "SKILL ERROR"}
    
    print(pskills)
    li = prediction(pskills)
    if li == False:
        return {"message":"I'm sorry I could not find anything", "error": "SKILL NOT FOUND ERROR"}
    
    res.append(li)
    df = pd.DataFrame({'Careers': li})

    career = []


    for i in range(len(df)):
        for z in mycol.find():
            if  df.Careers[i].strip() == z['job_name'].strip():
                pct = z['job_growth']
                
            
                career.append({
                    "career_name":z['job_name'].strip(), 
                    "career_growth": z['job_growth'],
                    "career_description": z['job_description']
                    })

    

    return career