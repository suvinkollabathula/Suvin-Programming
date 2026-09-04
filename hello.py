import streamlit as st
import re

# =========================================================
# PAGE SETTINGS
# =========================================================

st.set_page_config(
    page_title="My Profile & Calculator",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# =========================================================
# MOBILE CSS
# =========================================================

st.markdown("""
<style>

    /* Remove extra top space */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
        max-width: 500px;
    }

    /* Make buttons large and easy to touch */
    div.stButton > button {
        width: 100%;
        height: 65px;
        font-size: 25px;
        font-weight: bold;
        border-radius: 15px;
        margin: 3px 0;
    }

    /* Calculator display */
    .calculator-screen {
        background-color: #111111;
        color: white;
        border-radius: 18px;
        padding: 20px;
        margin-bottom: 15px;
        min-height: 110px;
        text-align: right;
        overflow-wrap: break-word;
    }

    .equation {
        color: #aaaaaa;
        font-size: 22px;
        min-height: 30px;
    }

    .answer {
        color: white;
        font-size: 42px;
        font-weight: bold;
        min-height: 55px;
    }

    /* Profile card */
    .profile-card {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 18px;
        margin-top: 15px;
        line-height: 1.8;
    }

    /* Mobile spacing */
    @media (max-width: 600px) {

        .block-container {
            padding-left: 12px;
            padding-right: 12px;
        }

        div.stButton > button {
            height: 62px;
            font-size: 23px;
        }

        .answer {
            font-size: 36px;
        }

        .equation {
            font-size: 19px;
        }
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# MY PROFILE
# =========================================================

st.title("👤 My Profile")
st.caption("Create your personalized profile!")

name = st.text_input(
    "👋 Name",
    placeholder="Enter your name"
)

age = st.number_input(
    "🎂 Age",
    min_value=1,
    max_value=100,
    value=14,
    step=1
)

school = st.text_input(
    "🏫 School",
    placeholder="Enter your school"
)

subject = st.text_input(
    "📚 Favorite Subject",
    placeholder="e.g. Science"
)

hobby = st.text_input(
    "🎮 Favorite Hobby",
    placeholder="e.g. Basketball"
)

if st.button(
    "✨ Create My Profile",
    use_container_width=True
):

    if name and school and subject and hobby:

        st.success("Profile created! 🎉")

        st.markdown(
            f"""
            <div class="profile-card">

            <h2>Hello! I'm {name} 👋</h2>

            🎂 I am <b>{age} years old</b>.<br>

            🏫 I go to <b>{school}</b>.<br>

            📚 My favorite subject is <b>{subject}</b>.<br>

            🎮 I enjoy <b>{hobby}</b>.

            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    else:

        st.warning(
            "⚠️ Please fill in all the fields!"
        )


# =========================================================
# CALCULATOR
# =========================================================

st.markdown("---")

st.title("🧮 Calculator")


# =========================================================
# CALCULATOR MEMORY
# =========================================================

if "equation" not in st.session_state:
    st.session_state.equation = ""

if "answer" not in st.session_state:
    st.session_state.answer = ""


# =========================================================
# CALCULATOR FUNCTIONS
# =========================================================

def number_pressed(number):

    st.session_state.equation += str(number)


def decimal_pressed():

    equation = st.session_state.equation

    # Split equation into numbers
    parts = re.split(r"[+\-×÷]", equation)

    current_number = parts[-1]

    # Only allow one decimal per number
    if "." not in current_number:
        st.session_state.equation += "."


def operation_pressed(operation):

    equation = st.session_state.equation

    if not equation:
        return

    # Don't allow two operators together
    if equation.strip()[-1] in "+-×÷":
        return

    st.session_state.equation += f" {operation} "


def clear_pressed():

    st.session_state.equation = ""
    st.session_state.answer = ""


def backspace_pressed():

    st.session_state.equation = (
        st.session_state.equation[:-1]
    )


def calculate():

    equation = st.session_state.equation

    if not equation:
        return

    # Don't calculate incomplete equation
    if equation.strip()[-1] in "+-×÷":
        return

    try:

        # Convert calculator symbols
        expression = equation.replace("×", "*")
        expression = expression.replace("÷", "/")

        # Security check
        if not re.fullmatch(
            r"[0-9+\-*/. ()]+",
            expression
        ):
            st.session_state.answer = "Error"
            return

        # Calculate
        result = eval(
            expression,
            {"__builtins__": None},
            {}
        )

        # Make whole numbers look nicer
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        st.session_state.answer = str(result)

    except ZeroDivisionError:

        st.session_state.answer = "Cannot divide by zero"

    except:

        st.session_state.answer = "Error"


# =========================================================
# CALCULATOR DISPLAY
# =========================================================

st.markdown(
    f"""
    <div class="calculator-screen">

        <div class="equation">
            {st.session_state.equation}
        </div>

        <div class="answer">
            {st.session_state.answer}
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CALCULATOR BUTTONS
# =========================================================


# ---------------------------------------------------------
# ROW 1: CLEAR / BACKSPACE / DECIMAL / DIVIDE
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# ROW 2: 7 8 9 ×
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# ROW 3: 4 5 6 -
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# ROW 4: 1 2 3 +
# ---------------------------------------------------------

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


# ---------------------------------------------------------
# ROW 5: 0 / =
# ---------------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.button(
        "0",
        use_container_width=True,
        on_click=number_pressed,
        args=(0,)
    )

with col2:
    pass

with col3:

    st.button(
        "=",
        use_container_width=True,
        on_click=calculate
    )

with col4:
    pass


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption(
    "📱 My Profile & Calculator • Made with Streamlit"
)
