import google.generativeai as genai

# Paste your Gemini API key below
API_KEY = "YOUR_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def analyze_resume(resume_text, job_desc):

    prompt = f"""
You are an expert recruiter.

Resume:
{resume_text}

Job Description:
{job_desc}

Provide:
1. Resume Strengths
2. Resume Weaknesses
3. ATS Improvement Suggestions
4. Interview Readiness Score out of 10

Keep the answer concise.
"""

    response = model.generate_content(prompt)

    return response.text