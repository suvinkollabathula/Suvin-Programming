import streamlit as st

st.set_page_config(
    page_title="My Profile & Calculator",
    page_icon="🧮",
    layout="centered"
)

# =========================
# MY PROFILE
# =========================

st.title("👤 My Profile")
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