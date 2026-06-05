import google.generativeai as genai

def generate_questions(resume_text, job_desc):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
You are an AI interviewer.

Resume:
{resume_text}

Job Description:
{job_desc}

Generate 10 interview questions.

Mix:
- Technical Questions
- Project Questions
- Behavioral Questions

Number them properly.
"""

    response = model.generate_content(prompt)

    return response.text