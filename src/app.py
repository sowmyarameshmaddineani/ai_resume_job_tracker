import streamlit as st
from job_tracker import init_db, add_application, get_applications
from ai_generator import generate_tailored_bullet_points
from pdf_generator import generate_pdf

# Initialize database
init_db()

st.title("📄 AI-Assisted Resume Builder & Job Tracker")

tab1, tab2 = st.tabs(["AI Resume Builder", "Job Tracker"])

with tab1:
    st.header("Tailor Your Resume with AI")
    job_desc = st.text_area("Paste Job Description Here:")
    raw_exp = st.text_area("Paste Your Experience / Project Summary:")
    
    if st.button("Generate Tailored Content"):
        if job_desc and raw_exp:
            with st.spinner("Generating tailored bullet points..."):
                result = generate_tailored_bullet_points(job_desc, raw_exp)
                st.session_state['tailored_result'] = result
        else:
            st.warning("Please fill in both fields.")
            
    if 'tailored_result' in st.session_state:
        st.subheader("Optimized Resume Bullet Points:")
        st.write(st.session_state['tailored_result'])
        
        # PDF Generation & Download
        pdf_buffer = generate_pdf(st.session_state['tailored_result'])
        st.download_button(
            label="📥 Download Resume Bullet Points as PDF",
            data=pdf_buffer,
            file_name="tailored_resume_bullet_points.pdf",
            mime="application/pdf"
        )

with tab2:
    st.header("Job Application Tracker")
    
    with st.form("job_form"):
        company = st.text_input("Company Name")
        role = st.text_input("Job Title / Role")
        status = st.selectbox("Status", ["Wishlist", "Applied", "Interviewing", "Offered", "Rejected"])
        date_applied = st.date_input("Date Applied")
        notes = st.text_area("Notes")
        submit = st.form_submit_button("Add Application")
        
        if submit and company and role:
            add_application(company, role, status, str(date_applied), notes)
            st.success(f"Added application for {company}!")
            
    st.subheader("Your Applications")
    df = get_applications()
    st.dataframe(df)