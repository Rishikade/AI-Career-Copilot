import streamlit as st

from resume_parser import extract_resume_text
from ats_score import calculate_ats_score
from gemini_helper import analyze_resume
from interview_generator import generate_questions
from cover_letter import generate_cover_letter
from recruiter_message import generate_recruiter_message

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.title("🚀 AI Career Copilot")

    st.write("AI Powered Resume Analyzer")

    st.write("---")

    st.write("Features")

    st.write("✅ ATS Score")
    st.write("✅ Skill Gap Analysis")
    st.write("✅ Recruiter Review")
    st.write("✅ Interview Questions")
    st.write("✅ Cover Letter")
    st.write("✅ Recruiter Message")

    st.write("---")

    st.write("Built by Rishika De")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("🚀 AI Career Copilot")

st.markdown("""
### Land Your Dream AI Job Faster

Upload your Resume and Job Description to get:

- ATS Score
- Skill Gap Analysis
- AI Recruiter Feedback
- Interview Questions
- Cover Letter
- Recruiter Outreach Message
""")

st.divider()

# ---------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    resume = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with col2:

    job_desc = st.text_area(
        "💼 Paste Job Description",
        height=250
    )

# ---------------------------------------------------
# ANALYZE
# ---------------------------------------------------

if st.button("🚀 Analyze Resume"):

    if resume is None:

        st.error("Please upload a resume.")
        st.stop()

    if job_desc.strip() == "":

        st.error("Please paste a job description.")
        st.stop()

    try:

        # -----------------------------------------
        # RESUME EXTRACTION
        # -----------------------------------------

        resume_text = extract_resume_text(resume)

        st.success("Resume uploaded successfully!")

        # -----------------------------------------
        # ATS SCORE
        # -----------------------------------------

        score, matched, missing = calculate_ats_score(
            resume_text,
            job_desc
        )

        st.subheader("📊 ATS Score")

        st.progress(score / 100)

        st.metric(
            "Resume Match",
            f"{score}%"
        )

        if score >= 70:
            st.balloons()

        # -----------------------------------------
        # SKILLS
        # -----------------------------------------

        col3, col4 = st.columns(2)

        with col3:

            st.subheader("✅ Matched Skills")

            if matched:

                for skill in matched:
                    st.success(skill)

            else:
                st.write("No matched skills found.")

        with col4:

            st.subheader("❌ Missing Skills")

            if missing:

                for skill in missing:
                    st.error(skill)

            else:
                st.write("No missing skills found.")

        # -----------------------------------------
        # RESUME TEXT
        # -----------------------------------------

        with st.expander("📄 View Extracted Resume"):

            st.write(resume_text)

        # -----------------------------------------
        # AI REVIEW
        # -----------------------------------------

        st.subheader("🤖 AI Recruiter Review")

        with st.spinner("Analyzing..."):

            review = analyze_resume(
                resume_text,
                job_desc
            )

        st.info(review)

        # -----------------------------------------
        # INTERVIEW QUESTIONS
        # -----------------------------------------

        st.subheader("🎤 AI Interview Questions")

        with st.spinner("Generating Questions..."):

            questions = generate_questions(
                resume_text,
                job_desc
            )

        st.code(questions)

        # -----------------------------------------
        # COVER LETTER
        # -----------------------------------------

        st.subheader("📄 AI Cover Letter")

        with st.spinner("Generating Cover Letter..."):

            cover_letter = generate_cover_letter(
                resume_text,
                job_desc
            )

        st.text_area(
            "Generated Cover Letter",
            cover_letter,
            height=350
        )

        # -----------------------------------------
        # RECRUITER MESSAGE
        # -----------------------------------------

        st.subheader("📧 Recruiter Outreach Message")

        with st.spinner("Generating Recruiter Message..."):

            recruiter_msg = generate_recruiter_message(
                resume_text,
                job_desc
            )

        st.text_area(
            "LinkedIn / Email Message",
            recruiter_msg,
            height=180
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )