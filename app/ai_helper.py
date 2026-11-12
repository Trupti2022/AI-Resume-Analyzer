from ollama import chat

def generate_feedback(resume_text, job_description):

    prompt = f"""
    Compare this resume with the job description.

    Resume:
    {resume_text}

    Job Description:
    {job_description}

    Give:

    1. Strengths
    2. Missing Skills
    3. Resume Improvement Suggestions

    Keep the answer concise.
    """

    response = chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]