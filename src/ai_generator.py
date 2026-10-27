import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_tailored_bullet_points(job_description, current_experience):
    prompt = f"""
    You are an expert career coach and resume writer. 
    Tailor the following experience bullet points to match the provided job description. 
    Highlight relevant keywords, metrics, and achievements.

    Job Description:
    {job_description}

    Current Experience:
    {current_experience}

    Provide 3-4 professional, action-oriented resume bullet points.
    """
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content