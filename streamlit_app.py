import streamlit as st
import PyPDF2
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extended dataset of interview questions with 50 questions per topic
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
        # Add more up to 50
    ],
    "R": [
        "What are R's main data structures?",
        "Explain the use of the 'apply' family of functions in R.",
        "What are data frames in R?",
        "How do you handle missing values in R?",
        "Explain the difference between 'rbind' and 'cbind'.",
        "What is ggplot2 used for in R?",
        "How do you import data into R?",
        "What are factors in R?",
        "Explain the use of the 'dplyr' package in R.",
        "What is the difference between 'lapply' and 'sapply'?",
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
        # Add more up to 50
    ],
    "C++": [
        "What are classes and objects in C++?",
        "Explain the concept of inheritance in C++.",
        "What is polymorphism in C++?",
        "What are virtual functions in C++?",
        "Explain the use of templates in C++.",
        "What is the difference between 'new' and 'malloc' in C++?",
        "What are friend functions in C++?",
        "What is the Standard Template Library (STL)?",
        "What are smart pointers in C++?",
        "What is a destructor in C++?",
        # Add more up to 50
    ],
    "Java": [
        "What is the difference between JDK, JRE, and JVM?",
        "Explain the concept of OOP in Java.",
        "What is the difference between 'equals()' and '==" in Java?",
        "What is garbage collection in Java?",
        "What are Java's access modifiers?",
        "What is multithreading in Java?",
        "What is the difference between 'ArrayList' and 'LinkedList'?",
        "What are Java annotations?",
        "What is the difference between 'String', 'StringBuilder', and 'StringBuffer'?",
        "Explain exception handling in Java.",
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

# Required packages:
# streamlit==1.26.0
# PyPDF2==3.0.0
# scikit-learn==1
