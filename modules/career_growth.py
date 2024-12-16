import openai

# Set your OpenAI API key here
openai.api_key = "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"  # Replace with your actual key

def predict_career_growth(resume_text):
    """
    Predicts career growth based on the resume text using GPT.
    :param resume_text: Text extracted from the resume.
    :return: Predicted career growth as a string.
    """
    prompt = (
        "Analyze the following resume and predict career growth for the next 3 years in a concise manner. "
        "Provide role suggestions, expected contributions, and skill improvements in a clear, brief format:\n\n"
        f"Resume: {resume_text}\n\n"
        "Return the response in bullet points or short sentences, focusing on the most important aspects of future growth."
    )
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Or "gpt-4" if available
            messages=[
                {"role": "system", "content": "You are a career advisor providing concise career predictions."},
                {"role": "user", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error in generating career growth prediction: {e}"


def simulate_career_growth(resume_text, role="Data Scientist"):
    """
    Simulates career progression for a candidate based on their resume and specific role.
    :param resume_text: Text extracted from the resume.
    :param role: The role for which the simulation is being made (default: "Data Scientist").
    :return: A string describing the simulation outcome.
    """
    # Example role-specific simulation
    if role.lower() == "data scientist":
        if "machine learning" in resume_text.lower():
            return (
                "The candidate is well-equipped to scale AI projects and could take on leadership roles in AI research "
                "within 2 years. They will be instrumental in driving innovation and adapting to new technologies."
            )
        else:
            return (
                "The candidate would need to gain more hands-on experience with machine learning. With the right training, "
                "they could grow into a strong Data Scientist, contributing to AI initiatives within 1-2 years."
            )
    elif role.lower() == "software engineer":
        return (
            "The candidate has a strong foundation in coding, but additional experience in system design and architecture "
            "will be crucial for advancing to senior engineering roles. After 1 year of mentorship, they could lead key projects."
        )
    else:
        return "Career simulation is not available for this role."

