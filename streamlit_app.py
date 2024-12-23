import streamlit as st
import PyPDF2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
{
    "Python": [
        {
            "Question": "Which of the following is a Python data type?",
            "Options": "Integer;String;Boolean;None",
            "Answer": "String"
        },
        {
            "Question": "Which of the following is used to define a method in Python?",
            "Options": "def;function;method;procedure",
            "Answer": "def"
        },
        {
            "Question": "What is the output of `print(10 / 3)` in Python?",
            "Options": "3;3.33;3.0;4",
            "Answer": "3.3333333333333335"
        },
        {
            "Question": "What does the `len()` function do in Python?",
            "Options": "Returns the length of an object;Checks if the object is empty;Returns the data type of an object;Compares two objects",
            "Answer": "Returns the length of an object"
        },
        {
            "Question": "Which of the following is used to import a module in Python?",
            "Options": "include;import;using;require",
            "Answer": "import"
        },
        {
            "Question": "What is the purpose of the `self` keyword in Python?",
            "Options": "To refer to the instance of the class;To call another method in the class;To define a class variable;To reference an external module",
            "Answer": "To refer to the instance of the class"
        },
        {
            "Question": "Which of the following is a valid way to create a dictionary in Python?",
            "Options": "dict = {};dict = []{};dict = set{};dict = (){}",
            "Answer": "dict = {}"
        },
        {
            "Question": "What is the default value of a boolean variable in Python?",
            "Options": "True;False;0;null",
            "Answer": "False"
        },
        {
            "Question": "Which of the following is used to handle exceptions in Python?",
            "Options": "try-catch;except-finally;do-catch;throw-catch",
            "Answer": "except-finally"
        },
        {
            "Question": "Which method is used to compare two strings in Python?",
            "Options": "==;compareTo;equals;match",
            "Answer": "=="
        },
        {
            "Question": "Which of the following is used to add an element to a list in Python?",
            "Options": "add();insert();append();push()",
            "Answer": "append()"
        },
        {
            "Question": "What is the output of `print(3 * 4)` in Python?",
            "Options": "12;34;14;Error",
            "Answer": "12"
        },
        {
            "Question": "Which of the following is used to define a class in Python?",
            "Options": "class;struct;def;module",
            "Answer": "class"
        },
        {
            "Question": "Which of the following is the correct way to create an object in Python?",
            "Options": "object = new Object();obj = Object();obj = new Object();obj = Object()",
            "Answer": "obj = Object()"
        },
        {
            "Question": "What is the correct syntax to create a set in Python?",
            "Options": "set = ();set = []{};set = {}{};set = ()",
            "Answer": "set = {}"
        },
        {
            "Question": "What is the output of `print(10 // 3)` in Python?",
            "Options": "3;3.33;3.0;10",
            "Answer": "3"
        },
        {
            "Question": "Which of the following is used to declare a variable in Python?",
            "Options": "let;var;int;None",
            "Answer": "None"
        },
        {
            "Question": "Which of the following data types is NOT mutable in Python?",
            "Options": "List;Set;Tuple;Dictionary",
            "Answer": "Tuple"
        },
        {
            "Question": "What is the output of `print(\"Hello\" * 3)` in Python?",
            "Options": "HelloHelloHello;Hello3;3Hello;Error",
            "Answer": "HelloHelloHello"
        },
        {
            "Question": "Which of the following is used to get the type of an object in Python?",
            "Options": "type();class();object();gettype()",
            "Answer": "type()"
        },
        {
            "Question": "What is the correct syntax to define a function in Python?",
            "Options": "def function_name():;function function_name();def;function",
            "Answer": "def function_name():"
        },
        {
            "Question": "Which of the following is a valid way to create a set in Python?",
            "Options": "set = []{};set = {}{};set = set();set = {}",
            "Answer": "set = set()"
        },
        {
            "Question": "Which of the following is a valid list operation in Python?",
            "Options": "append();add();insert();create()",
            "Answer": "append()"
        }
    ],
    "Java": [
        {
            "Question": "Which of the following is the correct way to declare a variable in Java?",
            "Options": "int x = 10;let x = 10;var x = 10;x = 10",
            "Answer": "int x = 10"
        },
        {
            "Question": "What is the default value of a boolean variable in Java?",
            "Options": "True;False;0;null",
            "Answer": "False"
        },
        {
            "Question": "Which of the following is used to define a method in Java?",
            "Options": "function;def;void;method",
            "Answer": "void"
        },
        {
            "Question": "Which of the following is NOT a valid data type in Java?",
            "Options": "int;double;boolean;text",
            "Answer": "text"
        },
        {
            "Question": "Which of the following is used to handle exceptions in Java?",
            "Options": "try-catch;catch-finally;do-catch;throw-catch",
            "Answer": "try-catch"
        },
        {
            "Question": "What is the purpose of the `final` keyword in Java?",
            "Options": "To define constants;To create a subclass;To create an interface;To initialize variables",
            "Answer": "To define constants"
        },
        {
            "Question": "Which of the following is the correct way to create an object in Java?",
            "Options": "object = new Object();Object obj = new Object();obj = new Object();new Object();",
            "Answer": "Object obj = new Object();"
        },
        {
            "Question": "Which method is used to compare two strings in Java?",
            "Options": "==;compareTo;equals;match",
            "Answer": "equals"
        },
        {
            "Question": "What is the size of an `int` in Java?",
            "Options": "16 bytes;32 bytes;64 bytes;8 bytes",
            "Answer": "32 bytes"
        },
        {
            "Question": "What does the `static` keyword mean in Java?",
            "Options": "The variable is shared among all instances of the class;The method is private;The variable is local to a method;The class is abstract",
            "Answer": "The variable is shared among all instances of the class"
        },
        {
            "Question": "What is the superclass of every class in Java?",
            "Options": "Object;Class;Super;Exception",
            "Answer": "Object"
        },
        {
            "Question": "Which of the following methods is used to obtain the length of an array in Java?",
            "Options": "length;size;length();size()",
            "Answer": "length"
        },
        {
            "Question": "Which of the following is a valid identifier in Java?",
            "Options": "int 1x;int $x;int &x;int x$",
            "Answer": "int $x"
        },
        {
            "Question": "Which collection class in Java allows elements to be accessed by index?",
            "Options": "ArrayList;HashSet;HashMap;LinkedList",
            "Answer": "ArrayList"
        },
        {
            "Question": "What is the correct syntax for calling a method in Java?",
            "Options": "methodName();method();methodName;method(){}",
            "Answer": "method();"
        },
        {
            "Question": "Which of the following is used to import a class in Java?",
            "Options": "import;include;use;importFrom",
            "Answer": "import"
        },
        {
            "Question": "Which of the following is an access modifier in Java?",
            "Options": "public;default;static;final",
            "Answer": "public"
        },
        {
            "Question": "Which of the following classes is used to handle input from the user in Java?",
            "Options": "Scanner;InputStream;BufferedReader;Console",
            "Answer": "Scanner"
        },
        {
            "Question": "What is the output of `System.out.println(10 / 3)` in Java?",
            "Options": "3;3.33;3.0;10",
            "Answer": "3"
        },
        {
            "Question": "Which of the following is NOT a valid constructor in Java?",
            "Options": "public MyClass();private MyClass();MyClass();MyClass(int x)",
            "Answer": "MyClass();"
        },
        {
            "Question": "Which method is used to find the square root of a number in Java?",
            "Options": "sqrt();Math.sqrt();sqrt;Math.pow()",
            "Answer": "Math.sqrt()"
        },
        {
            "Question": "Which of the following is used to create a thread in Java?",
            "Options": "Thread.run();Thread.start();Thread.create();Thread.new()",
            "Answer": "Thread.start()"
        },
        {
            "Question": "Which of the following is a wrapper class in Java?",
            "Options": "String;Integer;Character;Double",
            "Answer": "Integer"
        }
    ],
    "C": [
        {
            "Question": "Which of the following is the correct syntax to declare a variable in C?",
            "Options": "int x = 10;let x = 10;var x = 10;x = 10",
            "Answer": "int x = 10"
        },
        {
            "Question": "Which of the following is used to get the size of a data type in C?",
            "Options": "sizeof;length;sizeofof;typeSize",
            "Answer": "sizeof"
        },
        {
            "Question": "Which data type is used to store a character in C?",
            "Options": "int;char;string;double",
            "Answer": "char"
        },
        {
            "Question": "What is the default value of an uninitialized integer variable in C?",
            "Options": "0;undefined;null;random",
            "Answer": "undefined"
        },
        {
            "Question": "Which of the following is a valid comment in C?",
            "Options": "//This is a comment;#This is a comment;<!-- This is a comment -->;*/This is a comment*/",
            "Answer": "//This is a comment"
        },
        {
            "Question": "Which operator is used for logical AND in C?",
            "Options": "&&;&;|;AND",
            "Answer": "&&"
        },
        {
            "Question": "What is the correct way to include a standard library in C?",
            "Options": "#include <stdio.h>;import <stdio.h>;using namespace <stdio.h>;import <stdio>",
            "Answer": "#include <stdio.h>"
        },
        {
            "Question": "Which of the following is used to declare a pointer in C?",
            "Options": "int* ptr;ptr* int;int ptr*;ptr int*",
            "Answer": "int* ptr"
        },
        {
            "Question": "Which function is used to read a string from user input in C?",
            "Options": "scanf;gets;read;fgets",
            "Answer": "gets"
        },
        {
            "Question": "Which of the following functions is used to print output in C?",
            "Options": "print;echo;printf;output",
            "Answer": "printf"
        },
        {
            "Question": "What is the size of a pointer in C?",
            "Options": "4 bytes;8 bytes;16 bytes;It depends on the system",
            "Answer": "It depends on the system"
        },
        {
            "Question": "Which of the following data types is used for floating-point numbers in C?",
            "Options": "int;float;double;char",
            "Answer": "float"
        },
        {
            "Question": "Which of the following is the correct way to define a function in C?",
            "Options": "void func();function(){};def func();func(){}",
            "Answer": "void func();"
        },
        {
            "Question": "What is the correct syntax for an if statement in C?",
            "Options": "if (condition) {};if condition {};;if (condition);if condition;",
            "Answer": "if (condition) {}"
        },
        {
            "Question": "What does the `break` statement do in C?",
            "Options": "Exits the loop;Skips to the next iteration;Halts the program;Exits the function",
            "Answer": "Exits the loop"
        },
        {
            "Question": "Which of the following is the correct way to declare a constant in C?",
            "Options": "const int x = 10;int const x = 10;#define x 10;constant int x = 10",
            "Answer": "const int x = 10"
        },
        {
            "Question": "Which of the following is used to allocate memory dynamically in C?",
            "Options": "malloc;new;alloc;resize",
            "Answer": "malloc"
        },
        {
            "Question": "What is the output of the following C code: `printf(\"%d\", 5 + 3);`?",
            "Options": "5;8;53;Error",
            "Answer": "8"
        },
        {
            "Question": "Which of the following is NOT a valid loop type in C?",
            "Options": "while;for;repeat;do-while",
            "Answer": "repeat"
        },
        {
            "Question": "What is the correct syntax for a switch case statement in C?",
            "Options": "switch(expression) {case x:;switch(x) {};;case x:;}switch(x) {case;}",
            "Answer": "switch(expression) {case x:;}"
        },
        {
            "Question": "Which of the following is used to return a value from a function in C?",
            "Options": "return;exit;finish;end",
            "Answer": "return"
        },
        {
            "Question": "What is the correct syntax to declare an array in C?",
            "Options": "int arr[10];arr[10];int arr;array[] = {1,2,3};",
            "Answer": "int arr[10];"
        }
    ],
    "Behavioral Questions": [
        {
            "Question": "Tell me about a time you overcame a difficult challenge.",
            "Options": "Talk about a project;Discuss your skills;Focus on teamwork;Discuss a personal challenge",
            "Answer": "Talk about a project"
        },
        {
            "Question": "How do you handle conflict with a colleague?",
            "Options": "Avoid it;Argue and defend my point;Try to understand their point of view and find common ground;Stay quiet",
            "Answer": "Try to understand their point of view and find common ground"
        },
        {
            "Question": "Describe a situation where you had to work under pressure.",
            "Options": "Talk about deadlines;Focus on your time management;Mention stress management;Discuss multitasking",
            "Answer": "Talk about deadlines"
        },
        {
            "Question": "What is your greatest strength?",
            "Options": "Leadership;Time management;Problem-solving;Teamwork",
            "Answer": "Problem-solving"
        },
        {
            "Question": "Where do you see yourself in five years?",
            "Options": "A leadership role;Growing professionally;In the same position;Continuously learning and improving",
            "Answer": "Continuously learning and improving"
        },
        {
            "Question": "How do you prioritize tasks?",
            "Options": "By importance;By deadline;By difficulty;I don't prioritize",
            "Answer": "By importance"
        },
        {
            "Question": "How do you deal with constructive criticism?",
            "Options": "Accept it positively;Defend yourself;Ignore it;Feel offended",
            "Answer": "Accept it positively"
        },
        {
            "Question": "Give me an example of a time you worked on a team.",
            "Options": "Discuss collaboration;Talk about leadership;Focus on teamwork skills;Describe a solo project",
            "Answer": "Discuss collaboration"
        },
        {
            "Question": "What motivates you to perform well?",
            "Options": "Financial rewards;Personal growth;Recognition from peers;Challenge",
            "Answer": "Personal growth"
        },
        {
            "Question": "Describe a time when you had to learn a new skill quickly.",
            "Options": "Mention a course;Discuss an on-the-job experience;Talk about a personal project;Explain a technical skill",
            "Answer": "Discuss an on-the-job experience"
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

# Function to distribute questions equally among identified skills
def distribute_questions_equally(skills):
    total_questions = len(skills)
    all_questions = []
    for skill in skills:
        questions = QUESTION_BANK[skill]
        all_questions.extend(questions)
    return all_questions[:total_questions]

# Function to visualize progress
def visualize_progress(user_responses, questions):
    question_counts = {}
    for i, response in enumerate(user_responses):
        if isinstance(response, tuple):  # MCQ case
            answer, correct_answer = response
            if answer == correct_answer:
                question_counts[questions[i]['Question']] = "Correct"
            else:
                question_counts[questions[i]['Question']] = "Incorrect"
        else:  # Text response case
            if response.strip():
                vectorizer = CountVectorizer().fit_transform([questions[i]['Question'], response])
                vectors = vectorizer.toarray()
                similarity = cosine_similarity(vectors)[0, 1]
                if similarity > 0.5:
                    question_counts[questions[i]['Question']] = "Correct"
                else:
                    question_counts[questions[i]['Question']] = "Incorrect"
            else:
                question_counts[questions[i]['Question']] = "No Answer"

    # Visualization
    data = pd.DataFrame(list(question_counts.items()), columns=["Question", "Status"])
    plt.figure(figsize=(10, 6))
    sns.countplot(x="Status", data=data)
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

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

        # Distribute questions equally among skills
        questions = distribute_questions_equally(skills)

        st.write("### Interview Questions:")
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
                        vectorizer = CountVectorizer().fit_transform([questions[i]['Question'], response])
                        vectors = vectorizer.toarray()
                        similarity = cosine_similarity(vectors)[0, 1]
                        if similarity > 0.5:
                            st.success(f"Great answer for Q{i+1}! Your response is relevant.")
                        else:
                            st.warning(f"Q{i+1}: Your response could be improved. Consider addressing key points directly.")
                    else:
                        st.error(f"Q{i+1}: No answer provided.")

            # Show performance visualization
            st.write("### Your Performance Visualization:")
            visualize_progress(user_responses, questions)

            # Retry or Upload a New Resume
            if st.button("Retry with the Same Resume"):
                st.experimental_rerun()

            if st.button("Try a Different Resume"):
                st.session_state.clear()
                st.experimental_rerun()

    else:
        st.error("No skills identified from your resume. Please ensure your resume highlights your technical and soft skills.")
else:
    st.sidebar.info("Please upload your resume to get started.")
