import streamlit as st
import random

st.set_page_config(
    page_title="Grammar Heroes!",
    page_icon="🌟",
    layout="centered"
)

# ---------------- QUESTIONS ----------------

QUESTIONS = [
    {
        "sentence": "The cat ____ on the sofa.",
        "options": ["sit", "sits"],
        "answer": "sits",
        "explanation": "One cat = singular, so we add 's' to the verb."
    },

    {
        "sentence": "The dogs ____ in the park.",
        "options": ["runs", "run"],
        "answer": "run",
        "explanation": "More than one dog = plural, so we use 'run'."
    },

    {
        "sentence": "My brother ____ soccer every day.",
        "options": ["play", "plays"],
        "answer": "plays",
        "explanation": "One brother = singular, so we use 'plays'."
    },

    {
        "sentence": "The birds ____ in the sky.",
        "options": ["fly", "flies"],
        "answer": "fly",
        "explanation": "Many birds = plural, so we use 'fly'."
    },

    {
        "sentence": "The teacher ____ a story.",
        "options": ["tell", "tells"],
        "answer": "tells",
        "explanation": "One teacher = singular, so we use 'tells'."
    },

    {
        "sentence": "The monkeys ____ bananas.",
        "options": ["likes", "like"],
        "answer": "like",
        "explanation": "Many monkeys = plural, so we use 'like'."
    },

    {
        "sentence": "Dad ____ coffee every morning.",
        "options": ["drink", "drinks"],
        "answer": "drinks",
        "explanation": "One dad = singular, so we use 'drinks'."
    },

    {
        "sentence": "The children ____ to school.",
        "options": ["walk", "walks"],
        "answer": "walk",
        "explanation": "Children means many people, so we use 'walk'."
    },

    {
        "sentence": "The fish ____ in the pond.",
        "options": ["swim", "swims"],
        "answer": "swim",
        "explanation": "Fish here means many fish, so we use 'swim'."
    },

    {
        "sentence": "My sister ____ very fast.",
        "options": ["run", "runs"],
        "answer": "runs",
        "explanation": "One sister = singular, so we use 'runs'."
    }
]

# ---------------- SESSION STATE ----------------

if "score" not in st.session_state:
    st.session_state.score = 0

if "question_number" not in st.session_state:
    st.session_state.question_number = 1

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(QUESTIONS)

if "answered" not in st.session_state:
    st.session_state.answered = False

if "result" not in st.session_state:
    st.session_state.result = None

# ---------------- STYLING ----------------

st.markdown("""
<style>

.stApp{
background: linear-gradient(180deg,#8be9fd,#ffd166);
}

.title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#ff006e;
}

.subtitle{
text-align:center;
font-size:22px;
color:#073b4c;
}

.score-box{
background:#06d6a0;
padding:15px;
border-radius:20px;
text-align:center;
font-size:28px;
font-weight:bold;
color:white;
}

.question-box{
background:white;
padding:25px;
border-radius:20px;
font-size:30px;
font-weight:bold;
text-align:center;
}

.big-feedback{
font-size:28px;
font-weight:bold;
text-align:center;
}

.explanation{
background:#fff3cd;
padding:15px;
border-radius:15px;
font-size:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown('<div class="title">🌟 Grammar Heroes 🌟</div>',
            unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">Choose the correct verb and become a Grammar Superhero!</div>',
    unsafe_allow_html=True
)

st.write("")

st.markdown(
    f'<div class="score-box">🏆 Score: {st.session_state.score}</div>',
    unsafe_allow_html=True
)

st.write("")

# ---------------- QUESTION ----------------

q = st.session_state.current_question

st.markdown(
    f'<div class="question-box">Question {st.session_state.question_number}<br><br>{q["sentence"]}</div>',
    unsafe_allow_html=True
)

st.write("")

choice = st.radio(
    "👇 Pick your answer:",
    q["options"],
    key=f"radio_{st.session_state.question_number}"
)

# ---------------- SUBMIT ----------------

if not st.session_state.answered:

    if st.button("🚀 Check My Answer", use_container_width=True):

        st.session_state.answered = True

        if choice == q["answer"]:
            st.session_state.score += 10
            st.session_state.result = True
        else:
            st.session_state.result = False

        st.rerun()

# ---------------- FEEDBACK ----------------

if st.session_state.answered:

    if st.session_state.result:

        st.balloons()

        st.markdown(
            '<div class="big-feedback">🎉 Correct! Amazing job!</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            '<div class="big-feedback">😃 Nice try!</div>',
            unsafe_allow_html=True
        )

        st.write(
            f"✅ The correct answer is: **{q['answer']}**"
        )

    st.write("")

    st.markdown(
        f'<div class="explanation">💡 {q["explanation"]}</div>',
        unsafe_allow_html=True
    )

    st.write("")

    if st.session_state.score >= 80:
        st.success("🏅 WOW! You are a Grammar Master!")

    elif st.session_state.score >= 50:
        st.success("🌈 Great work! Keep going!")

    elif st.session_state.score >= 20:
        st.success("⭐ You're getting stronger!")

    st.write("")

    if st.button("➡️ Next Question", use_container_width=True):

        st.session_state.question_number += 1
        st.session_state.current_question = random.choice(QUESTIONS)
        st.session_state.answered = False
        st.session_state.result = None

        st.rerun()

# ---------------- FOOTER ----------------

st.write("")
st.write("---")

st.info("""
🦸 Grammar Tip:

Singular (1 person, animal or thing)
👉 usually uses verbs ending with **s**

Examples:

🐱 The cat sits.

👦 Ben runs.

Plural (2 or more)
👉 usually uses verbs without **s**

Examples:

🐶 The dogs run.

👧👦 The children walk.
""")
