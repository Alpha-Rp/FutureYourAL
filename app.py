import streamlit as st
import re
import plotly.graph_objects as go
from modules.resume_parser import extract_text_from_pdf
from modules.pq_calculator import calculate_pq_with_growth, calculate_risk_reward
from modules.career_growth import predict_career_growth
from modules.team_synergy import generate_team_profile, extract_candidate_skills, calculate_synergy_score
from modules.growth_map import generate_growth_map
import os

# Load the CSS file
with open('style.css') as f:
    css = f.read()

# Apply the CSS styles
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


# Streamlit App Header
st.title("Future You Predictor")
st.subheader("Upload your resume to analyze potential and team compatibility.")

# File upload section
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    # Save the uploaded file temporarily
    with open(f"data/{uploaded_file.name}", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Extract relevant details (name, skills, experience) from the uploaded resume
    extracted_details = extract_text_from_pdf(f"data/{uploaded_file.name}")

    # Display the extracted details
    st.write("### Key Extracted Details:")
    st.markdown(f"**Name:** {extracted_details.get('Name', 'N/A')}")
    st.markdown(f"**Email:** {extracted_details.get('Email', 'N/A')}")
    st.markdown(f"**Phone:** {extracted_details.get('Phone', 'N/A')}")
    st.markdown(f"**Year(s) of Passing (YOP):** {extracted_details.get('Year of Passing (YOP)', 'N/A')}")
    st.markdown(f"**Skills:** {', '.join(extracted_details.get('Skills', []))}")

    # Combine all extracted details into a single string for PQ calculation
    resume_text = " ".join([str(value) if isinstance(value, str) else ", ".join(value) for value in extracted_details.values()])

    
    # Calculate the PQ Score
    skills_matched = len(extracted_details.get('Skills', []))
    years_of_experience = len(re.findall(r"\b\d+\s+years\b", resume_text))
    pq_results = calculate_pq_with_growth(resume_text, skills_matched, years_of_experience)

    # Display PQ Results
    st.write("### Potential Quotient (PQ) Analysis 🔮")
    st.write(f"**PQ Score:** {pq_results['PQ Score']}")
    st.write(f"- Skills Matched: {pq_results['Skills Matched']}")
    st.write(f"- Years of Experience: {pq_results['Years of Experience']}")
    st.write(f"- Certifications: {pq_results['Certifications']}")
    st.write(f"- Learning Speed: {pq_results['Learning Speed']}")
    st.write(f"- Adaptability: {pq_results['Adaptability']}")
    st.write(f"- Passion for Improvement: {pq_results['Passion for Improvement']}")

    # Visualize PQ Score
    fig_pq = go.Figure()
    fig_pq.add_trace(
        go.Indicator(
            mode="gauge+number",
            value=pq_results["PQ Score"],
            title={"text": "Potential Quotient (PQ)"},
            gauge={
                "axis": {"range": [0, 100]},
                "bar": {"color": "blue"},
                "steps": [
                    {"range": [0, 50], "color": "lightgray"},
                    {"range": [50, 75], "color": "yellow"},
                    {"range": [75, 100], "color": "green"},
                ],
            },
        )
    )
    st.plotly_chart(fig_pq)

    # Career Growth Prediction
    career_growth_prediction = predict_career_growth(resume_text)
    st.write("### 🌱 **Predicted Career Growth:**")
    st.markdown(f"**Growth Summary:**\n\n{career_growth_prediction}")

    # Risk-Reward Analysis
    risk_reward = calculate_risk_reward(pq_results["PQ Score"], pq_results["Skills Matched"], pq_results["Years of Experience"])
    st.write("### Risk-Reward Analysis 📊")
    st.write(risk_reward)

    # Growth Map using AI (GPT)
    growth_map = generate_growth_map(resume_text)
    st.write("### 📈 Growth Map for Applicants:")
    st.markdown(f"**Your Personalized Growth Plan:**\n\n{growth_map}")


    # Team Synergy Analysis
    candidate_skills = extract_candidate_skills(resume_text)
    team_profiles = generate_team_profile(num_features=len(candidate_skills))
    synergy_scores = calculate_synergy_score(candidate_skills, team_profiles)

    # Visualize Team Synergy
    team_labels = [f"Team {i+1}" for i in range(len(synergy_scores))]
    fig_synergy = go.Figure(
        [go.Bar(x=team_labels, y=synergy_scores, marker_color="skyblue")]
    )
    fig_synergy.update_layout(
        title="Team Synergy Scores 🤝",
        xaxis_title="Teams",
        yaxis_title="Synergy Score",
        yaxis=dict(range=[0, 1]),
    )
    st.plotly_chart(fig_synergy)

    # Display Synergy Scores as Text
    st.write("### Team Synergy Analysis (Text):")
    for i, score in enumerate(synergy_scores):
        st.write(f"Team {i+1} Synergy Score: {score:.2f}")