Future You Predictor

An AI-powered tool that analyzes resumes, predicts career growth, evaluates potential quotient (PQ), and provides personalized recommendations to enhance career prospects. This tool is designed to assist both HR professionals in shortlisting candidates and applicants in understanding their growth areas.

Table of Contents
Features
Tech Stack
How It Works
Installation
Usage
File Structure
Future Enhancements
Contributing
License

Features:

🔮 Potential Quotient (PQ) Analysis
Evaluates a candidate’s potential using:
Skills Matched: Identifies job-relevant skills.
Years of Experience: Captures career history.
Certifications: Recognizes professional certifications.
Learning Speed: Assesses advanced technical skills.
Adaptability: Evaluates cross-disciplinary potential.
Passion for Improvement: Looks for evidence of projects, volunteering, and growth.

📈 AI-Powered Growth Map
Uses OpenAI's GPT to generate a structured, personalized growth plan:
Missing skills to acquire.
Certifications to pursue.
Soft skills to improve.
Leadership potential and project recommendations.

🌱 Career Growth Prediction
Simulates career progression over the next three years.
Suggests potential job roles and areas for skill development.

📊 Risk-Reward Analysis
Categorizes candidates as:
Safe Candidates: High compatibility but lower growth potential.
High-Risk, High-Reward: Requires training but shows potential.
Balanced Candidates: A mix of current fit and growth potential.

🤝 Team Synergy Predictor
Analyzes how candidates align with existing team profiles based on:
Skills.
Personality traits.
Work style.

🚀 Interactive Visualizations
Gauge Charts: Visualize PQ scores.
Bar Charts: Display team synergy scores.
User-friendly interface built with Streamlit for real-time feedback.

Tech Stack :

Backend
Python (v3.10): Core programming language.
OpenAI API: GPT-4 for generating career insights and growth plans.
pdfplumber: Extracts resume data.
scikit-learn: Performs team synergy analysis using cosine similarity.
Frontend
Streamlit: Interactive UI for resume upload and feedback display.
Plotly: Visualizes PQ scores and synergy scores.
Libraries
NumPy, pandas: Data manipulation.
re (Regex): For parsing and extracting information.

How It Works

Upload Resume:

Users upload their resumes in PDF format.
Resume Parsing:

Extracts name, email, phone, skills, experience, and certifications using pdfplumber and regex.
Analysis & Insights:

PQ Analysis: Calculates a potential quotient score.
Growth Map: AI generates actionable recommendations for skill and career improvement.
Risk-Reward Analysis: Categorizes candidates based on their strengths and growth potential.
Team Synergy: Evaluates compatibility with existing teams.
Visualizations:

Displays insights as interactive charts and tables.
Installation
Step 1: Clone the Repository
bash
Copy code
git clone https://github.com/your-username/future-you-predictor.git
cd future-you-predictor
Step 2: Set Up a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
Step 3: Install Dependencies
bash
Copy code
pip install -r requirements.txt
Step 4: Run the Application
bash
Copy code
streamlit run app.py
Usage
Launch the application using Streamlit (http://localhost:8501).
Upload a resume in PDF format.
View:
Extracted Resume Details.
PQ Analysis and Career Growth Prediction.
Personalized Growth Map.
Risk-Reward Analysis.
Team Synergy Scores.
File Structure
bash
Copy code
future-you-predictor/
│
├── app.py                # Main application file
├── modules/              # Directory for logic modules
│   ├── pq_calculator.py  # PQ calculation logic
│   ├── resume_parser.py  # Resume parsing and extraction
│   ├── career_growth.py  # AI-based career growth prediction
│   ├── team_synergy.py   # Team synergy calculations
│   ├── growth_map.py     # AI-based growth map generation
│
├── data/                 # Temporary storage for uploaded files
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
Future Enhancements
Custom Job Descriptions: Analyze resumes against specific job requirements.
Real-Time Skill Matching: Provide industry-specific skill recommendations.
Gamified Growth Maps: Add interactive elements to growth plans for better engagement.
Contributing
We welcome contributions! Please fork the repository, create a feature branch, and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.