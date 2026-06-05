def calculate_ats_score(resume_text, job_desc):

    skills = [
        "python",
        "sql",
        "machine learning",
        "deep learning",
        "tensorflow",
        "streamlit",
        "nlp",
        "rag",
        "llm",
        "opencv",
        "docker",
        "aws",
        "fastapi"
    ]

    matched_skills = []
    missing_skills = []

    for skill in skills:

        if skill.lower() in job_desc.lower():

            if skill.lower() in resume_text.lower():
                matched_skills.append(skill)

            else:
                missing_skills.append(skill)

    total = len(matched_skills) + len(missing_skills)

    if total == 0:
        score = 100
    else:
        score = int((len(matched_skills) / total) * 100)

    return score, matched_skills, missing_skills