import streamlit as st

st.set_page_config(
    page_title="My Profile & Calculator",
    page_icon="🧮",
    layout="centered"
)

# =========================
# MY PROFILE
# =========================

st.title("👤 Suvin's Profile")
st.write("Fill in your information below!")

name = st.text_input("👋 Name")
age = st.number_input("🎂 Age", min_value=1, max_value=100, step=1)
school = st.text_input("🏫 School")
subject = st.text_input("📚 Favorite Subject")
hobby = st.text_input("🎮 Favorite Hobby")

if st.button("✨ Create My Profile"):
    if name and school and subject and hobby:
        st.success("Profile created! 🎉")

        st.markdown("---")

        st.header(f"Hello! My name is {name}. 👋")
        st.write(f"🎂 I am **{age} years old**.")
        st.write(f"🏫 I go to **{school}**.")
        st.write(f"📚 My favorite subject is **{subject}**.")
        st.write(f"🎮 I enjoy **{hobby}**.")

        st.balloons()
    else:
        st.warning("⚠️ Please fill in all the fields!")


# =========================
# FULL CALCULATOR
# =========================

import re

st.markdown("---")
st.title("🧮 Calculator")


# -------------------------
# Calculator memory
# -------------------------

if "equation" not in st.session_state:
    st.session_state.equation = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""


# -------------------------
# Number button
# -------------------------

def number_pressed(number):

    st.session_state.equation += str(number)


# -------------------------
# Decimal button
# -------------------------

def decimal_pressed():

    # Don't add another decimal to the current number
    parts = re.split(r"[+\-×÷]", st.session_state.equation)

    current_number = parts[-1]

    if "." not in current_number:
        st.session_state.equation += "."


# -------------------------
# Operation button
# -------------------------

def operation_pressed(operation):

    equation = st.session_state.equation

    # Don't allow an operator as the first character
    if equation == "":
        return

    # Don't allow two operators next to each other
    if equation[-1] in "+-×÷":
        return

    st.session_state.equation += f" {operation} "


# -------------------------
# Calculate
# -------------------------

def calculate():

    equation = st.session_state.equation

    if equation == "":
        return

    # Don't calculate if equation ends with an operator
    if equation.strip()[-1] in "+-×÷":
        return

    try:

        # Convert calculator symbols to Python math symbols
        expression = equation.replace("×", "*")
        expression = expression.replace("÷", "/")

        # Only allow numbers and math operators
        if not re.fullmatch(r"[0-9+\-*/. ()]+", expression):
            st.session_state.answer = "Error"
            return

        # Calculate
        result = eval(expression, {"__builtins__": None}, {})

        # Remove .0 from whole numbers
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        st.session_state.answer = str(result)

    except ZeroDivisionError:

        st.session_state.answer = "Cannot divide by zero"

    except:

        st.session_state.answer = "Error"


# -------------------------
# Clear
# -------------------------

def clear_pressed():

    st.session_state.equation = ""
    st.session_state.answer = ""


# -------------------------
# Backspace
# -------------------------

def backspace_pressed():

    st.session_state.equation = st.session_state.equation[:-1]


# =========================
# CALCULATOR SCREEN
# =========================

st.markdown(
    f"""
    <div style="
        background-color: #222;
        color: #aaaaaa;
        padding: 18px;
        border-radius: 10px 10px 0px 0px;
        text-align: right;
        font-size: 28px;
        min-height: 40px;
        overflow-wrap: break-word;
    ">
        {st.session_state.equation}
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div style="
        background-color: #111;
        color: white;
        padding: 18px;
        border-radius: 0px 0px 10px 10px;
        text-align: right;
        font-size: 42px;
        font-weight: bold;
        min-height: 50px;
        margin-bottom: 15px;
    ">
        {st.session_state.answer}
    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# BUTTONS
# =========================

# -------------------------
# Row 1
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "C",
        use_container_width=True,
        on_click=clear_pressed
    )

with col2:
    st.button(
        "⌫",
        use_container_width=True,
        on_click=backspace_pressed
    )

with col3:
    st.button(
        ".",
        use_container_width=True,
        on_click=decimal_pressed
    )

with col4:
    st.button(
        "÷",
        use_container_width=True,
        on_click=operation_pressed,
        args=("÷",)
    )


# -------------------------
# Row 2
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "7",
        use_container_width=True,
        on_click=number_pressed,
        args=(7,)
    )

with col2:
    st.button(
        "8",
        use_container_width=True,
        on_click=number_pressed,
        args=(8,)
    )

with col3:
    st.button(
        "9",
        use_container_width=True,
        on_click=number_pressed,
        args=(9,)
    )

with col4:
    st.button(
        "×",
        use_container_width=True,
        on_click=operation_pressed,
        args=("×",)
    )


# -------------------------
# Row 3
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "4",
        use_container_width=True,
        on_click=number_pressed,
        args=(4,)
    )

with col2:
    st.button(
        "5",
        use_container_width=True,
        on_click=number_pressed,
        args=(5,)
    )

with col3:
    st.button(
        "6",
        use_container_width=True,
        on_click=number_pressed,
        args=(6,)
    )

with col4:
    st.button(
        "-",
        use_container_width=True,
        on_click=operation_pressed,
        args=("-",)
    )


# -------------------------
# Row 4
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "1",
        use_container_width=True,
        on_click=number_pressed,
        args=(1,)
    )

with col2:
    st.button(
        "2",
        use_container_width=True,
        on_click=number_pressed,
        args=(2,)
    )

with col3:
    st.button(
        "3",
        use_container_width=True,
        on_click=number_pressed,
        args=(3,)
    )

with col4:
    st.button(
        "+",
        use_container_width=True,
        on_click=operation_pressed,
        args=("+",)
    )


# -------------------------
# Row 5
# -------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.button(
        "0",
        use_container_width=True,
        on_click=number_pressed,
        args=(0,)
    )

with col2:
    st.write("")

with col3:
    st.button(
        "=",
        use_container_width=True,
        on_click=calculate
    )

with col4:
    st.write("")


 
# -------------------------
# Grade Calculator
# -------------------------   


import streamlit as st

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        margin-bottom: 30px;
    }

    .result-box {
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #ddd;
        margin-top: 15px;
        text-align: center;
    }

    .big-grade {
        font-size: 55px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# TITLE
# -----------------------------
st.markdown(
    '<div class="main-title">🎓 Grade Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Calculate your marks, percentage, grade and GPA</div>',
    unsafe_allow_html=True
)

# -----------------------------
# SESSION STATE
# -----------------------------
if "subjects" not in st.session_state:
    st.session_state.subjects = [
        {"name": "Mathematics", "marks": 0},
        {"name": "Science", "marks": 0},
        {"name": "English", "marks": 0},
    ]

if "calculated" not in st.session_state:
    st.session_state.calculated = False


# -----------------------------
# GRADE FUNCTION
# -----------------------------
def get_grade(mark):
    if mark >= 90:
        return "A+"
    elif mark >= 80:
        return "A"
    elif mark >= 70:
        return "B"
    elif mark >= 60:
        return "C"
    elif mark >= 50:
        return "D"
    else:
        return "F"


def get_gpa(mark):
    if mark >= 90:
        return 4.0
    elif mark >= 80:
        return 3.7
    elif mark >= 70:
        return 3.0
    elif mark >= 60:
        return 2.0
    elif mark >= 50:
        return 1.0
    else:
        return 0.0


# -----------------------------
# ADD SUBJECT
# -----------------------------
st.subheader("📚 Your Subjects")

for i, subject in enumerate(st.session_state.subjects):

    col1, col2 = st.columns([2, 1])

    with col1:
        st.session_state.subjects[i]["name"] = st.text_input(
            "Subject",
            value=subject["name"],
            key=f"subject_{i}"
        )

    with col2:
        st.session_state.subjects[i]["marks"] = st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            value=float(subject["marks"]),
            step=1.0,
            key=f"marks_{i}"
        )


# -----------------------------
# BUTTONS
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Add Subject", use_container_width=True):

        st.session_state.subjects.append(
            {
                "name": f"Subject {len(st.session_state.subjects) + 1}",
                "marks": 0
            }
        )

        st.rerun()

with col2:
    if st.button("🗑️ Reset", use_container_width=True):

        st.session_state.subjects = [
            {"name": "Mathematics", "marks": 0},
            {"name": "Science", "marks": 0},
            {"name": "English", "marks": 0},
        ]

        st.session_state.calculated = False
        st.rerun()


# -----------------------------
# CALCULATE
# -----------------------------
st.write("")

if st.button(
    "🎯 Calculate My Grade",
    use_container_width=True,
    type="primary"
):

    st.session_state.calculated = True


# -----------------------------
# RESULTS
# -----------------------------
if st.session_state.calculated:

    marks = [
        subject["marks"]
        for subject in st.session_state.subjects
    ]

    total = sum(marks)
    number_of_subjects = len(marks)

    maximum = number_of_subjects * 100

    percentage = (total / maximum) * 100
    average = total / number_of_subjects

    overall_grade = get_grade(average)
    gpa = sum(get_gpa(mark) for mark in marks) / number_of_subjects

    # -----------------------------
    # OVERALL RESULT
    # -----------------------------
    st.divider()

    st.subheader("📊 Your Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Marks",
            f"{total:.0f}/{maximum}"
        )

    with col2:
        st.metric(
            "Percentage",
            f"{percentage:.1f}%"
        )

    with col3:
        st.metric(
            "GPA",
            f"{gpa:.2f}/4.0"
        )

    # -----------------------------
    # OVERALL GRADE
    # -----------------------------
    st.markdown(
        f"""
        <div class="result-box">
            <div>Overall Grade</div>
            <div class="big-grade">{overall_grade}</div>
            <div>Average: {average:.1f}%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    # -----------------------------
    # PROGRESS BAR
    # -----------------------------
    st.write("📈 Overall Performance")

    st.progress(min(percentage / 100, 1.0))

    # -----------------------------
    # SUBJECT RESULTS
    # -----------------------------
    st.subheader("📚 Subject Results")

    for subject in st.session_state.subjects:

        name = subject["name"]
        mark = subject["marks"]

        grade = get_grade(mark)
        subject_gpa = get_gpa(mark)

        col1, col2, col3 = st.columns([2, 1, 1])

        with col1:
            st.write(f"**{name}**")

        with col2:
            st.write(f"{mark:.0f}/100")

        with col3:
            st.write(f"**{grade}**")

    # -----------------------------
    # MESSAGE
    # -----------------------------
    st.divider()

    if percentage >= 90:
        st.success("🏆 Outstanding! You're doing amazing!")

    elif percentage >= 80:
        st.success("🌟 Excellent work! Keep it up!")

    elif percentage >= 70:
        st.info("👍 Great job! You're on the right track!")

    elif percentage >= 60:
        st.warning("🙂 Good effort! A little more practice can improve your score.")

    elif percentage >= 50:
        st.warning("📚 You passed, but keep working to improve!")

    else:
        st.error("💪 Don't give up! Keep practicing and try again!")




    # ---------------------------------------------------------------------------------------------------------
    # NEW TASK
    # ---------------------------------------------------------------------------------------------------------

# -----------------------------
# PAGE SETTINGS
# -----------------------------
st.set_page_config(
    page_title="Quiz Master",
    page_icon="🧠",
    layout="centered"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

    .main-title {
        text-align: center;
        font-size: 45px;
        font-weight: 800;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #777;
        font-size: 18px;
        margin-bottom: 30px;
    }

    .question-card {
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #ddd;
        margin: 20px 0;
    }

    .question-number {
        font-size: 15px;
        color: #777;
        font-weight: 600;
    }

    .question-text {
        font-size: 25px;
        font-weight: 700;
        margin-top: 8px;
    }

    .score-box {
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        border: 1px solid #ddd;
        margin: 20px 0;
    }

    .score {
        font-size: 60px;
        font-weight: 800;
    }

</style>
""", unsafe_allow_html=True)


# -----------------------------
# SESSION STATE
# -----------------------------
if "page" not in st.session_state:
    st.session_state.page = "create"

if "questions" not in st.session_state:
    st.session_state.questions = []

if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "answers" not in st.session_state:
    st.session_state.answers = {}

if "quiz_finished" not in st.session_state:
    st.session_state.quiz_finished = False


# -----------------------------
# FUNCTIONS
# -----------------------------
def reset_quiz():

    st.session_state.page = "create"
    st.session_state.questions = []
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.quiz_finished = False


def start_quiz(questions):

    st.session_state.questions = questions
    st.session_state.current_question = 0
    st.session_state.answers = {}
    st.session_state.quiz_finished = False
    st.session_state.page = "play"


def finish_quiz():

    st.session_state.quiz_finished = True
    st.session_state.page = "result"


# -----------------------------
# CREATE QUIZ PAGE
# -----------------------------
if st.session_state.page == "create":

    st.markdown(
        '<div class="main-title">🧠 Quiz Master</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Create your own quiz and challenge yourself!</div>',
        unsafe_allow_html=True
    )

    st.subheader("⚙️ Quiz Setup")

    number_of_questions = st.number_input(
        "Number of questions",
        min_value=1,
        max_value=20,
        value=5,
        step=1
    )

    questions = []

    st.divider()

    # -------------------------
    # QUESTION CREATOR
    # -------------------------
    for i in range(int(number_of_questions)):

        st.markdown(f"### 📝 Question {i + 1}")

        question = st.text_input(
            "Question",
            placeholder="Example: What is the capital of France?",
            key=f"question_{i}"
        )

        col1, col2 = st.columns(2)

        with col1:

            choice_a = st.text_input(
                "🔵 Choice A",
                placeholder="Enter choice A",
                key=f"a_{i}"
            )

            choice_c = st.text_input(
                "🟢 Choice C",
                placeholder="Enter choice C",
                key=f"c_{i}"
            )

        with col2:

            choice_b = st.text_input(
                "🟡 Choice B",
                placeholder="Enter choice B",
                key=f"b_{i}"
            )

            choice_d = st.text_input(
                "🔴 Choice D",
                placeholder="Enter choice D",
                key=f"d_{i}"
            )

        correct = st.radio(
            "Correct answer",
            ["A", "B", "C", "D"],
            horizontal=True,
            key=f"correct_{i}"
        )

        questions.append({
            "question": question,
            "choices": {
                "A": choice_a,
                "B": choice_b,
                "C": choice_c,
                "D": choice_d
            },
            "correct": correct
        })

        st.divider()

    # -------------------------
    # START BUTTON
    # -------------------------
    if st.button(
        "🚀 Start Quiz",
        use_container_width=True,
        type="primary"
    ):

        valid = True

        for q in questions:

            if not q["question"].strip():
                valid = False

            for choice in q["choices"].values():

                if not choice.strip():
                    valid = False

        if not valid:

            st.error(
                "⚠️ Please fill in every question and all four choices."
            )

        else:

            start_quiz(questions)

            st.rerun()


# -----------------------------
# QUIZ PLAY PAGE
# -----------------------------
elif st.session_state.page == "play":

    questions = st.session_state.questions

    total_questions = len(questions)

    current = st.session_state.current_question

    question = questions[current]

    # -------------------------
    # HEADER
    # -------------------------
    st.markdown(
        '<div class="main-title">🎮 Quiz Time!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <div class="subtitle">
            Question {current + 1} of {total_questions}
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------
    # PROGRESS
    # -------------------------
    progress = (current + 1) / total_questions

    st.progress(progress)

    st.write("")

    # -------------------------
    # QUESTION CARD
    # -------------------------
    st.markdown(
        f"""
        <div class="question-card">

            <div class="question-number">
                QUESTION {current + 1}
            </div>

            <div class="question-text">
                {question["question"]}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------
    # ANSWERS
    # -------------------------
    previous_answer = st.session_state.answers.get(current)

    options = ["A", "B", "C", "D"]

    default_index = None

    if previous_answer in options:
        default_index = options.index(previous_answer)

    selected = st.radio(
        "Choose your answer:",
        options,
        format_func=lambda x: f"{x}. {question['choices'][x]}",
        index=default_index,
        key=f"play_answer_{current}"
    )

    st.write("")

    # -------------------------
    # NAVIGATION
    # -------------------------
    col1, col2 = st.columns(2)

    with col1:

        if current > 0:

            if st.button(
                "⬅️ Previous",
                use_container_width=True
            ):

                if selected:
                    st.session_state.answers[current] = selected

                st.session_state.current_question -= 1

                st.rerun()

    with col2:

        if current < total_questions - 1:

            if st.button(
                "Next ➡️",
                use_container_width=True,
                type="primary"
            ):

                if not selected:

                    st.warning("⚠️ Please choose an answer.")

                else:

                    st.session_state.answers[current] = selected

                    st.session_state.current_question += 1

                    st.rerun()

        else:

            if st.button(
                "🏆 Finish Quiz",
                use_container_width=True,
                type="primary"
            ):

                if not selected:

                    st.warning("⚠️ Please choose an answer.")

                else:

                    st.session_state.answers[current] = selected

                    finish_quiz()

                    st.rerun()

    st.write("")

    # -------------------------
    # QUESTION STATUS
    # -------------------------
    answered = len(st.session_state.answers)

    st.caption(
        f"📌 {answered} of {total_questions} questions answered"
    )


# -----------------------------
# RESULT PAGE
# -----------------------------
elif st.session_state.page == "result":

    questions = st.session_state.questions
    answers = st.session_state.answers

    total = len(questions)

    score = 0

    for i, question in enumerate(questions):

        if answers.get(i) == question["correct"]:
            score += 1

    percentage = (score / total) * 100

    # -------------------------
    # TITLE
    # -------------------------
    st.markdown(
        '<div class="main-title">🏆 Quiz Complete!</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">Here are your final results</div>',
        unsafe_allow_html=True
    )

    # -------------------------
    # SCORE
    # -------------------------
    st.markdown(
        f"""
        <div class="score-box">

            <div>Your Score</div>

            <div class="score">
                {score}/{total}
            </div>

            <div>
                {percentage:.0f}%
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.progress(percentage / 100)

    # -------------------------
    # FEEDBACK
    # -------------------------
    if percentage == 100:

        st.success("🏆 Perfect score! You're amazing!")

    elif percentage >= 80:

        st.success("🌟 Excellent work! Keep it up!")

    elif percentage >= 60:

        st.info("👍 Good job! You did well!")

    elif percentage >= 50:

        st.warning("🙂 Not bad! A little more practice will help.")

    else:

        st.error("💪 Keep practicing! You'll get better!")

    st.divider()

    # -------------------------
    # ANSWER REVIEW
    # -------------------------
    st.subheader("📋 Answer Review")

    for i, question in enumerate(questions):

        user_answer = answers.get(i)
        correct_answer = question["correct"]

        st.markdown(
            f"### Question {i + 1}"
        )

        st.write(question["question"])

        if user_answer == correct_answer:

            st.success(
                f"✅ Correct — {correct_answer}. "
                f"{question['choices'][correct_answer]}"
            )

        else:

            st.error(
                f"❌ Your answer: "
                f"{user_answer if user_answer else 'No answer'}"
            )

            st.info(
                f"✅ Correct answer: {correct_answer}. "
                f"{question['choices'][correct_answer]}"
            )

        st.divider()

    # -------------------------
    # NEW QUIZ
    # -------------------------
    if st.button(
        "🔄 Create New Quiz",
        use_container_width=True,
        type="primary"
    ):

        reset_quiz()

        st.rerun()
