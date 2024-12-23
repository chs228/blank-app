import streamlit as st
import PyPDF2
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset of interview questions
QUESTION_BANK = {
    "Python": [
        "What are Python decorators?",
        "Explain the difference between deep copy and shallow copy in Python.",
        "How does Python manage memory?",
    ],
    "Machine Learning": [
        "What is overfitting, and how can you prevent it?",
        "Explain the difference between supervised and unsupervised learning.",
        "What are the main assumptions of linear regression?",
    ],
    "SQL": [
        "What is the difference between INNER JOIN and OUTER JOIN?",
        "How would you optimize a slow SQL query?",
        "What is normalization, and why is it important?",
    ],
    "Communication": [
        "Can you describe a time when you resolved a conflict in a team?",
        "How would you explain a technical concept to someone without a technical background?",
        "Tell me about a time you worked under pressure to meet a deadline.",
    ],
}

# Function to extract text from the uploaded PDF resume
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract skills from the resume text (basic implementation)
def extract_skills(resume_text):
    skills = []
    keywords = list(QUESTION_BANK.keys())
    for keyword in keywords:
        if keyword.lower() in resume_text.lower():
            skills.append(keyword)
    return skills

# Function to simulate chatbot interview
def ask_questions(skills):
    questions = []
    for skill in skills:
        if skill in QUESTION_BANK:
            questions.append(random.choice(QUESTION_BANK[skill]))
    return questions

# Streamlit UI
st.title("Job Interview Preparation Chatbot")

st.sidebar.header("Upload Your Resume")
resume_file = st.sidebar.file_uploader("Upload your resume (PDF format only)", type=["pdf"])

if resume_file:
    st.sidebar.success("Resume uploaded successfully!")
    resume_text = extract_text_from_pdf(resume_file)

    # Extract skills from the resume
    skills = extract_skills(resume_text)

    if skills:
        st.write("### Skills Identified from Your Resume:")
        st.write(", ".join(skills))

        # Ask questions dynamically based on skills
        st.write("### Interview Questions:")
        questions = ask_questions(skills)

        user_responses = []
        for i, question in enumerate(questions):
            st.write(f"**Q{i+1}: {question}**")
            response = st.text_area(f"Your Answer to Q{i+1}:", key=f"response_{i}")
            user_responses.append(response)

        if st.button("Submit Answers"):
            st.write("### Feedback on Your Responses:")
            for i, response in enumerate(user_responses):
                if response.strip():
                    # Simple feedback based on response length and keywords
                    vectorizer = CountVectorizer().fit_transform([questions[i], response])
                    vectors = vectorizer.toarray()
                    similarity = cosine_similarity(vectors)[0, 1]

                    if similarity > 0.5:
                        st.success(f"Great answer for Q{i+1}! Your response is relevant.")
                    else:
                        st.warning(f"Q{i+1}: Your response could be improved. Consider addressing key points directly.")
                else:
                    st.error(f"Q{i+1}: No answer provided.")
    else:
        st.error("No skills identified from your resume. Please ensure your resume highlights your technical and soft skills.")
else:
    st.sidebar.info("Please upload your resume to get started.")
