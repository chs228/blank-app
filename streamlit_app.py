import streamlit as st
import PyPDF2
import random
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
        "What are Python decorators?",
        "Explain the difference between deep copy and shallow copy in Python.",
        "How does Python manage memory?",
        "What is the Global Interpreter Lock (GIL)?",
        "Explain list comprehensions in Python.",
        "What are Python's key data types?",
        "How do you handle exceptions in Python?",
        "What are Python's built-in data structures?",
        "Explain the use of 'self' in Python classes.",
        "What is the difference between @staticmethod and @classmethod?",
        "How do you manage packages and environments in Python?",
        "What are Python's iterators and generators?",
        "Explain multithreading and multiprocessing in Python.",
        "What are Python's lambda functions?",
        "How does Python handle garbage collection?",
        # Add more up to 50
    ],
    "Machine Learning": [
        "What is overfitting, and how can you prevent it?",
        "Explain the difference between supervised and unsupervised learning.",
        "What are the main assumptions of linear regression?",
        "What is gradient descent?",
        "Explain the concept of feature engineering.",
        "What are common performance metrics for classification problems?",
        "What is cross-validation, and why is it important?",
        "Explain the bias-variance tradeoff.",
        "What is a confusion matrix?",
        "What are ensemble methods in machine learning?",
        "What is a support vector machine (SVM)?",
        "How do decision trees work?",
        "What is the purpose of the k-nearest neighbors algorithm?",
        "What is unsupervised clustering?",
        "How does principal component analysis (PCA) work?",
        # Add more up to 50
    ],
    "C": [
        "What are pointers in C?",
        "Explain the difference between 'malloc' and 'calloc'.",
        "What is a null pointer?",
        "How does memory allocation work in C?",
        "What is the difference between 'struct' and 'union' in C?",
        "What is a segmentation fault?",
        "Explain the use of header files in C.",
        "What is recursion in C?",
        "What are storage classes in C?",
        "What is the difference between '++i' and 'i++'?",
        "What is the function of the 'static' keyword in C?",
        "How does a stack differ from a heap in C?",
        "What is the role of macros in C?",
        "What are bitwise operators in C?",
        "How do you handle strings in C?",
        # Add more up to 50
    ],
    "Behavioral Questions": [
        "Can you describe a time you worked in a team to achieve a goal?",
        "How do you handle conflict in the workplace?",
        "What is your greatest strength, and how has it helped you in your career?",
        "Tell me about a time you failed and how you handled it.",
        "How do you prioritize tasks when faced with multiple deadlines?",
        "What motivates you to perform well at work?",
        "Can you give an example of a time you went above and beyond?",
        "How do you handle feedback from colleagues or supervisors?",
        "Describe a time you had to learn something quickly.",
        "What are your long-term career goals?",
        # Add more up to 50
    ],
    "Java": [
        "What is the difference between JDK, JRE, and JVM?",
        "Explain the concept of OOP in Java.",
        "What is the difference between 'equals()' and '==' in Java?",
        "What is garbage collection in Java?",
        "What are Java's access modifiers?",
        "What is multithreading in Java?",
        "What is the difference between 'ArrayList' and 'LinkedList'?",
        "What are Java annotations?",
        "What is the difference between 'String', 'StringBuilder', and 'StringBuffer'?",
        "Explain exception handling in Java.",
        "What is the purpose of the 'final' keyword in Java?",
        "What is the Java Stream API?",
        "What is the role of the 'synchronized' keyword in Java?",
        "What is method overloading and method overriding in Java?",
        "How does the Java Virtual Machine (JVM) work?",
        # Add more up to 50
    ],
    "DSA": [
        "What are the key differences between arrays and linked lists?",
        "Explain the concept of binary search.",
        "What is a stack, and where is it used?",
        "What is a queue, and how does it differ from a stack?",
        "Explain the concept of hash tables.",
        "What is a binary tree?",
        "What is the difference between BFS and DFS?",
        "What is a heap data structure?",
        "What is the time complexity of quicksort?",
        "Explain dynamic programming with an example.",
        "What is a graph, and how is it represented?",
        "What is a trie, and where is it used?",
        "What is the time complexity of binary search?",
        "How do you reverse a linked list?",
        "What is a circular linked list?",
        # Add more up to 50
    ],
    "Data Science": [
        "What is the CRISP-DM framework?",
        "What are the key differences between supervised and unsupervised learning?",
        "What is data wrangling?",
        "What are common data visualization techniques?",
        "Explain the concept of dimensionality reduction.",
        "What is the difference between regression and classification?",
        "What is A/B testing in data science?",
        "What are the steps to preprocess data?",
        "What is feature selection?",
        "Explain the difference between data normalization and standardization.",
        "What is the role of statistical hypothesis testing in data science?",
        "How do you handle missing data in a dataset?",
        "What is cross-validation, and why is it important?",
        "What are outliers, and how do you handle them?",
        "Explain the concept of bagging and boosting.",
        # Add more up to 50
    ],
    "AI": [
        "What is artificial intelligence?",
        "Explain the Turing Test.",
        "What is natural language processing (NLP)?",
        "What are expert systems?",
        "What is the difference between weak AI and strong AI?",
        "Explain reinforcement learning.",
        "What is the role of neural networks in AI?",
        "What is a chatbot, and how does it work?",
        "What are common challenges in AI development?",
        "Explain ethical concerns related to AI.",
        "What is transfer learning?",
        "What are generative adversarial networks (GANs)?",
        "How does computer vision work?",
        "What is the importance of data in AI models?",
        "What is explainability in AI?",
        # Add more up to 50
    ],
    "Cyber Security": [
        "What is the CIA triad in cybersecurity?",
        "What is a firewall, and how does it work?",
        "Explain the difference between symmetric and asymmetric encryption.",
        "What is a DDoS attack?",
        "What is two-factor authentication?",
        "What is phishing, and how can it be prevented?",
        "What is the role of penetration testing in cybersecurity?",
        "What is the difference between a virus and a worm?",
        "What is the purpose of a VPN?",
        "Explain the concept of zero trust security.",
        "What is a security incident response plan?",
        "How does blockchain enhance cybersecurity?",
        "What are the common types of malware?",
        "How do you secure APIs?",
        "What are OWASP Top 10 vulnerabilities?",
        # Add more up to 50
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

            # Check if the question is an MCQ
            if 'Options' in question and 'Answer' in question:
                options = question['Options'].split(';')
                correct_answer = question['Answer']
                answer = st.radio(f"Choose an answer for Q{i+1}:", options)
                user_responses.append((answer, correct_answer))
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

# Required packages:
# streamlit==1.26.0
# PyPDF2==3.0.0
# pandas==1.5.3
# scikit-learn==1.2.0
