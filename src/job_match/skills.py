import json

def load_skills_db(path="data/skills_db.json"):
    with open(path,'r') as f:
        data = json.load(f)
    return data["skills"]

def extract_skills(text, skills_db):
    skill_set = set()
    for skill in skills_db:
        if skill in text:
            skill_set.add(skill)
    return skill_set

def get_skill_gap(resume_skills,jd_skills):
    #matches - intersection
    matched_skills = resume_skills & jd_skills

    #missing = difference
    missing_skills = jd_skills - resume_skills

    return matched_skills,missing_skills