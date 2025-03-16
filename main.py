import streamlit as st  # Streamlit library for creating web-based applications
import time  # Time module for adding delays in execution

# Set up the page configuration with a title, icon, and layout
st.set_page_config(page_title="Python MCQs Quiz", page_icon="🐍", layout="centered")

# Add custom CSS styling for better UI appearance
st.markdown("""
    <style>
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
            width: 100%;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        .question-card {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# Display the quiz title
st.markdown("<div class='title'>🐍 Python MCQs Quiz</div>", unsafe_allow_html=True)

# Define the quiz questions with options and correct answers
questions = [
    {"question": "What is the output of print(2 ** 3)?", "options": ["6", "8", "9", "4"], "answer": "8"},
    {"question": "Which of the following is a valid variable name in Python?", "options": ["2var", "_var", "var-name", "var name"], "answer": "_var"},
    {"question": "Which keyword is used to define a function in Python?", "options": ["define", "def", "func", "function"], "answer": "def"},
    {"question": "What does the 'len()' function return?", "options": ["Number of elements in a list", "Last element of a list", "First element of a list", "Sum of elements in a list"], "answer": "Number of elements in a list"},
    {"question": "Which of the following data types is immutable in Python?", "options": ["List", "Dictionary", "Tuple", "Set"], "answer": "Tuple"},
    {"question": "Which loop is used for iterating over a sequence in Python?", "options": ["for loop", "while loop", "do-while loop", "repeat loop"], "answer": "for loop"},
    {"question": "What is the output of type([])?", "options": ["list", "tuple", "dictionary", "set"], "answer": "list"},
    {"question": "Which method is used to remove the last item from a list?", "options": ["remove()", "pop()", "delete()", "discard()"], "answer": "pop()"},
    {"question": "What is the correct way to create a dictionary in Python?", "options": ["{key1: value1, key2: value2}", "[key1, value1, key2, value2]", "(key1: value1, key2: value2)", "<key1: value1, key2: value2>"], "answer": "{key1: value1, key2: value2}"},
    {"question": "Which function is used to get user input in Python?", "options": ["input()", "scan()", "read()", "get()"], "answer": "input()"},
    {"question": "What is the output of print(3 * 'abc')?", "options": ["abcabcabc", "abc abc abc", "Error", "3abc"], "answer": "abcabcabc"},
    {"question": "Which of the following is used to define a block of code in Python?", "options": ["Curly braces {}", "Parentheses ()", "Indentation", "Square brackets []"], "answer": "Indentation"},
    {"question": "Which function is used to open a file in Python?", "options": ["open()", "read()", "write()", "file()"], "answer": "open()"},
    {"question": "What does the 'pass' statement do in Python?", "options": ["Skips the current iteration", "Does nothing", "Exits the loop", "Raises an error"], "answer": "Does nothing"},
    {"question": "Which of the following is used to handle exceptions in Python?", "options": ["try-except", "if-else", "for-while", "switch-case"], "answer": "try-except"}
]

# Initialize session state variables if not already set
if "score" not in st.session_state:
    st.session_state.score = 0  
if "question_index" not in st.session_state:
    st.session_state.question_index = 0  

# Check if the quiz is complete
if st.session_state.question_index >= len(questions):
    st.markdown(f"### 🎉 Congratulations! You have completed the quiz! Your Score: {st.session_state.score}/{len(questions)}")
    st.balloons()
    if st.session_state.score > 0:
        st.markdown("### 🌟 Keep pushing forward! 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill")
    st.stop()  

# Display quiz progress as a progress bar
progress = (st.session_state.question_index + 1) / len(questions)
st.progress(progress)

# Get the current question based on the session index
question = questions[st.session_state.question_index]
st.markdown(f"<div class='question-card'><h2>{question['question']}</h2></div>", unsafe_allow_html=True)

# Create radio buttons for answer selection
selected_option = st.radio("Select your answer:", question["options"], key="answer")

# Handle answer submission when the button is clicked
if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.balloons()
        st.session_state.score += 1  
    else:
        st.error(f"❌ Incorrect! The correct answer is {question['answer']}")
    time.sleep(2)  
    st.session_state.question_index += 1  
    st.rerun()

    st.divider()
        
st.markdown(
            """
            <div style='text-align: center;'>
            <p>Python MCQs Quiz is a collection of multiple choice questions (MCQs) on Python programming language.</p>
            <p>Built with ❤️ by <a href="https://github.com/sadiqkhan7777">Sadiq Khan</a> Using streamlit</p>
            </div>
            """,
            unsafe_allow_html=True
        )