import streamlit as st
import PyPDF2
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to load the question bank from CSV
def load_question_bank(csv_file):
    df = pd.read_csv(csv_file)
    question_bank = {}
    for topic in df['Topic'].unique():
        question_bank[topic] = df[df['Topic'] == topic].to_dict(orient='records')
    return question_bank

# Load the question bank
QUESTION_BANK = {
    "Python": [
        {
            "Question": "What are Python decorators?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "What is the difference between deep copy and shallow copy in Python?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "Which of the following is a Python data type?",
            "Options": "Integer;String;Boolean;None",  # MCQ with options
            "Answer": "String"
        },
        {
            "Question": "What is the Global Interpreter Lock (GIL)?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "Machine Learning": [
        {
            "Question": "What is overfitting, and how can you prevent it?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "Which of the following is an example of supervised learning?",
            "Options": "Clustering;Classification;Dimensionality reduction;Association rule mining",  # MCQ with options
            "Answer": "Classification"
        },
        {
            "Question": "What is gradient descent?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "Java": [
        {
            "Question": "What is the difference between JDK, JRE, and JVM?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "Which of the following is a correct statement in Java?",
            "Options": "Java is a programming language;Java is a scripting language;Java is used for front-end development;Java is used for machine learning",  # MCQ with options
            "Answer": "Java is a programming language"
        },
        {
            "Question": "What is garbage collection in Java?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "Behavioral Questions": [
        {
            "Question": "Can you describe a time you worked in a team to achieve a goal?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "What motivates you to perform well at work?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "DSA": [
        {
            "Question": "What are the key differences between arrays and linked lists?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "What is the time complexity of quicksort?",
            "Options": "O(n^2);O(n log n);O(log n);O(n)",  # MCQ with options
            "Answer": "O(n log n)"
        },
        {
            "Question": "What is a graph, and how is it represented?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "Data Science": [
        {
            "Question": "What is A/B testing in data science?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "Which of the following is a supervised learning algorithm?",
            "Options": "Decision Trees;K-Means;KNN;DBSCAN",  # MCQ with options
            "Answer": "Decision Trees"
        },
        {
            "Question": "What is data wrangling?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "AI": [
        {
            "Question": "What is artificial intelligence?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "Which of the following is an example of supervised learning?",
            "Options": "Reinforcement Learning;Supervised Learning;Unsupervised Learning;Deep Learning",  # MCQ with options
            "Answer": "Supervised Learning"
        },
        {
            "Question": "What is natural language processing (NLP)?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ],
    "Cyber Security": [
        {
            "Question": "What is the CIA triad in cybersecurity?",
            "Options": None,  # Open-ended question
            "Answer": None
        },
        {
            "Question": "Which of the following is a type of encryption?",
            "Options": "Symmetric;Asymmetric;RSA;AES",  # MCQ with options
            "Answer": "AES"
        },
        {
            "Question": "What is a firewall, and how does it work?",
            "Options": None,  # Open-ended question
            "Answer": None
        }
    ]
}

# Function to extract text from the uploaded PDF resume
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Function to extract skills from the resume text
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
            for q in QUESTION_BANK[skill]:
                questions.append(q)
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
            st.write(f"**Q{i+1}: {question['Question']}**")

            # Check if the question has options (MCQ)
            if question["Options"]:
                options = question["Options"].split(';')
                answer = st.radio(f"Choose an answer for Q{i+1}:", options)
                user_responses.append((answer, question['Answer']))
            else:
                response = st.text_area(f"Your Answer to Q{i+1}:", key=f"response_{i}")
                user_responses.append(response)

        if st.button("Submit Answers"):
            st.write("### Feedback on Your Responses:")
            for i, response in enumerate(user_responses):
                if isinstance(response, tuple):  # MCQ case
                    answer, correct_answer = response
                    if answer == correct_answer:
                        st.success(f"Q{i+1}: Correct! Your answer is {answer}.")
                    else:
                        st.warning(f"Q{i+1}: Incorrect. The correct answer is {correct_answer}.")
                else:  # Text response case
                    if response.strip():
                        # Simple feedback based on response length and keywords
                        vectorizer = CountVectorizer().fit_transform([questions[i]['Question'], response])
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

