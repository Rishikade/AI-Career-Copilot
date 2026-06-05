import google.generativeai as genai

def generate_cover_letter(resume_text, job_desc):

    model = genai.GenerativeModel("gemini-2.5-flash")

    prompt = f"""
Write a professional cover letter.

Resume:
{resume_text}

Job Description:
{job_desc}

Keep it 250-300 words.
"""

    response = model.generate_content(prompt)

    return response.text