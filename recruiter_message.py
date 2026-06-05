import google.generativeai as genai

def generate_recruiter_message(resume_text, job_desc):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Write a short LinkedIn message to a recruiter.

Resume:
{resume_text}

Job Description:
{job_desc}

Keep it under 120 words.
"""

    response = model.generate_content(prompt)

    return response.text