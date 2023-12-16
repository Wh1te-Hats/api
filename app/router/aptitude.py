from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.model import General, Course
from app.helper import read_json

from app.aptitude.generalApt.logicalReasoning import logical_aptitude
from app.aptitude.generalApt.verbalAbilityApt import verbal_ability_aptitude 
from app.aptitude.generalApt.verbalReasoningApt import verbal_reasoning_aptitude 
from app.aptitude.generalApt.arithmeticApt import arithematic_aptitude
from app.aptitude.generalApt.generalKnowledgeApt import aptitude as general_knowledge_aptitude
from app.aptitude.generalApt.nonVerbalReasoningApt import nonVerbal_aptitude

from app.aptitude.courseBased.engineering.chemical import chemical_aptitude 
from app.aptitude.courseBased.engineering.civil import civil_aptitude 
from app.aptitude.courseBased.engineering.cse import cse_aptitude
from app.aptitude.courseBased.engineering.ece import ece_aptitude
from app.aptitude.courseBased.engineering.eee import eee_aptitude
from app.aptitude.courseBased.engineering.mechanical import mechanical_aptitude

from app.aptitude.courseBased.medical.bioChemical import bio_chemical_aptitude
from app.aptitude.courseBased.medical.biotech import bio_tech_aptitude
from app.aptitude.courseBased.medical.microBiology import microbiology_aptitude


aptitude_router = APIRouter(tags=["aptitude test"])

@aptitude_router.post('/aptitude/general')
async def general_aptitude(data: General):
    
    if (data.topic).lower() == 'logical reasoning':
        response = logical_aptitude()
        
    if (data.topic).lower() == 'verbal ability':
        response = verbal_ability_aptitude()
        
    if (data.topic).lower() == 'verbal reasoning':
        response = verbal_reasoning_aptitude()
        
    if (data.topic).lower() == 'arithmetic':
        response = arithematic_aptitude()
        
    if (data.topic).lower() == 'general knowledge':
        response = general_knowledge_aptitude()
        
    if (data.topic).lower() == 'non verbal reasoning':
        response = nonVerbal_aptitude()

    return JSONResponse(content=response,media_type="application/json")

#REMOVE
import json
@aptitude_router.post('/aptitude/general/dummy')
def dummy(data: General):
    file_path = 'app/dumpy.json'
    with open(file_path, 'r') as json_file:
            data = json.load(json_file)
    return data

    # analytics(response,topic,data)

    return response

@aptitude_router.post('/aptitude/course/engineering')
async def course_aptitude(data: Course):
    if (data.subject).lower() == 'chemical':
        response = chemical_aptitude()
    if (data.subject).lower() == 'civil':
        response = civil_aptitude()
    if (data.subject).lower() == 'cse':
        response = cse_aptitude()
    if (data.subject).lower() == 'ece':
        response = ece_aptitude()
    if (data.subject).lower() == 'eee':
        response = eee_aptitude()
    if (data.subject).lower() == 'mechanical':
        response = mechanical_aptitude()
    return response


@aptitude_router.post('/aptitude/course/medical')
async def medical_aptitude(data: Course):
    if (data.subject).lower() == 'bio_chem':
        response = bio_chemical_aptitude()
    if (data.subject).lower() == 'bio_tech':
        response = bio_tech_aptitude()
    if (data.subject).lower() == 'micro_bio':
        response = microbiology_aptitude()

    return response