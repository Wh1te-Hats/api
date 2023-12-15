from fastapi import APIRouter

from app.model import General, Course
from app.helper import read_json

from app.aptitude.generalApt.logicalReasoning import logical_aptitude
from app.aptitude.generalApt.verbalAbilityApt import aptitude as verbal_ability_aptitude
from app.aptitude.generalApt.verbalReasoningApt import aptitude as verbal_reasoning_aptitude
from app.aptitude.generalApt.arithmeticApt import aptitude as arithmetic_aptitude
from app.aptitude.generalApt.generalKnowledgeApt import aptitude as general_knowledge_aptitude
from app.aptitude.generalApt.verbalReasoningApt import aptitude as non_verbal_reasoning_aptitude

from app.aptitude.courseBased.engineering.chemical import aptitude as chemical_aptitude
from app.aptitude.courseBased.engineering.civil import aptitude as civil_aptitude
from app.aptitude.courseBased.engineering.cse import aptitude as cse_aptitude
from app.aptitude.courseBased.engineering.ece import aptitude as ece_aptitude
from app.aptitude.courseBased.engineering.eee import aptitude as eee_aptitude
from app.aptitude.courseBased.engineering.mechanical import aptitude as mechanical_aptitude

from app.aptitude.courseBased.medical.bioChemical import aptitude as bio_chem_aptitude
from app.aptitude.courseBased.medical.biotech import aptitude as bio_tech_aptitude
from app.aptitude.courseBased.medical.microBiology import aptitude as micro_bio_aptitude


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
        response = arithmetic_aptitude()
        
    if (data.topic).lower() == 'general knowledge':
        response = general_knowledge_aptitude()
        
    if (data.topic).lower() == 'non verbal reasoning':
        response = non_verbal_reasoning_aptitude()

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
        response = bio_chem_aptitude()
    if (data.subject).lower() == 'bio_tech':
        response = bio_tech_aptitude()
    if (data.subject).lower() == 'micro_bio':
        response = micro_bio_aptitude()

    return response