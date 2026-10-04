import streamlit as st

from resume_parser import extract_text
from skill_matcher import extract_skills


# Page configuration
st.set_page_config(
    page_title="AI Resume Screening System",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("AI Resume Screening System")

st.write(
    "Analyze resumes and match candidates with a job description."
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Home",
        "Resume Screening",
        "Analytics"
    ]
)

# Home page
if page == "Home":

    st.header("Welcome")

    st.write(
        """
        This app helps recruiters analyze resumes
        and identify candidates based on job requirements.
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(" Resumes", 0)

    with col2:
        st.metric("Candidates", 0)

    with col3:
        st.metric(" Average Score", "0%")


# Resume Screening page
elif page == "Resume Screening":

    st.header(" Resume Screening")

    st.subheader("Job Description")

    job_description = st.text_area(
        "Enter the job description:",
        height=200,
        placeholder="""
Example:

We are looking for a Python Developer.

Required skills:
Python, SQL, Django, Flask, Pandas, AWS and Git.
"""
    )

    st.subheader("Upload Resumes")

    uploaded_files = st.file_uploader(
        "Upload PDF or DOCX resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button(" Analyze Resumes"):

        if not job_description.strip():

            st.warning(
                "Please enter a job description."
            )

        elif not uploaded_files:

            st.warning(
                "Please upload at least one resume."
            )

        else:

            st.success(
                f"{len(uploaded_files)} resume(s) uploaded successfully!"
            )

            # Extract required skills only once
            required_skills = extract_skills(job_description)

            st.write("### Required Skills")

            if required_skills:
                st.info(", ".join(required_skills))
            else:
                st.warning(
                    "No recognized skills found in the job description."
                )

            # Process every uploaded resume
            for file in uploaded_files:

                st.write("---")

                st.subheader(f"{file.name}")

                # Extract resume text
                resume_text = extract_text(file)

                if not resume_text.strip():

                    st.warning(
                        "No text could be extracted from this resume."
                    )

                    continue

                # Display extracted text
                st.text_area(
                    "Extracted Resume Text",
                    resume_text,
                    height=250,
                    key=f"text_{file.name}"
                )

                # Extract skills from resume
                resume_skills = extract_skills(resume_text)

                # Find matching skills
                matched_skills = list(
                    set(resume_skills) & set(required_skills)
                )

                # Find missing skills
                missing_skills = list(
                    set(required_skills) - set(resume_skills)
                )

                # Calculate match score
                if required_skills:

                    match_score = (
                        len(matched_skills)
                        / len(required_skills)
                    ) * 100

                else:

                    match_score = 0

                st.subheader("Screening Result")

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "Match Score",
                        f"{match_score:.2f}%"
                    )

                with col2:

                    st.metric(
                        "Matched Skills",
                        len(matched_skills)
                    )

                with col3:

                    st.metric(
                        "Missing Skills",
                        len(missing_skills)
                    )

                st.write("### Matched Skills")

                if matched_skills:

                    st.success(
                        ", ".join(matched_skills)
                    )

                else:

                    st.info(
                        "No matching skills found."
                    )

                st.write("### Missing Skills")

                if missing_skills:

                    st.error(
                        ", ".join(missing_skills)
                    )

                else:

                    st.success(
                        "No missing skills!"
                    )


# Analytics page
elif page == "Analytics":

    st.header("Analytics")

    st.info(
        "Analytics will appear here after resume screening."
    )
