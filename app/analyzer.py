from app.skills import SKILLS

def analyze_resume(job_description, resume_skills):

    required_skills = []

    for skill in SKILLS:
        if skill.lower() in job_description.lower():
            required_skills.append(skill)

    matched = []
    missing = []

    for skill in required_skills:
        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (
        len(matched) / len(required_skills) * 100
        if required_skills
        else 0
    )

    return {
        "required_skills": required_skills,
        "score": round(score, 2),
        "matched": matched,
        "missing": missing
    }
def get_grade(score):

    if score >= 90:
        return "Excellent", "Strong fit for the role"

    elif score >= 75:
        return "Good", "Good match with minor gaps"

    elif score >= 50:
        return "Average", "Relevant profile but needs improvement"

    else:
        return "Needs Improvement", "Several key requirements are missing"