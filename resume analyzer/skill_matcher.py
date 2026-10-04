#skill_matcher.py
#skills that our system can recognize
import re
SKILLS=['python','SQL','Artificial Intelligence',
        'machine learning','deep learning','streamlit',
        'c','c++','javascript','flask','django','html','css',
        'tensorflow','pandas','numpy','aws','docker','github',
        'excel','tableau','powerbi','nlp']
def extract_skills(text):
    text=text.lower()
    found_skills=[]
    for skill in SKILLS:
        if re.search(r"\b" + re.escape(skill)+r"\b",text):
            found_skills.append(skill)
    return found_skills



    
