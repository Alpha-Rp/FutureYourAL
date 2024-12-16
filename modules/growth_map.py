import openai

# Set your OpenAI API key here
openai.api_key = "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"  # Replace with your actual API key

def generate_growth_map(resume_text):
    """
    Generates a personalized growth plan for the candidate based on resume text using GPT.
    :param resume_text: Text extracted from the resume.
    :return: Growth map as a string in a well-structured format.
    """
    prompt = f"""
    Based on the following resume text, generate a personalized growth map for the applicant. The growth map should include:
    1. Missing skills the applicant should focus on.
    2. Recommended certifications that would enhance their qualifications.
    3. Suggestions for soft skills the applicant can improve.
    4. Recommendations for gaining more experience (e.g., projects, volunteering).
    5. Any leadership or managerial skills the applicant should develop for future roles.

    The growth map should be in a **structured format** with **headings** and **bullet points** to make it clear and easy for HR to read.

    Resume Text:
    {resume_text}

    Return the growth map in a well-organized format with the above sections.
    """

    try:
        # Use the OpenAI API to generate the growth map with a newer model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a career advisor providing concise predictions."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,  # Limit the output length
            temperature=0.7,  # Control the randomness
        )

        # Get the generated growth map
        growth_map = response['choices'][0]['message']['content'].strip()

        return growth_map
    except Exception as e:
        return f"Error generating growth map: {str(e)}"
