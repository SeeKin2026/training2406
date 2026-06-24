import streamlit as st
import random

st.set_page_config(
    page_title="🚀 Grammar Space Invaders",
    page_icon="👾",
    layout="wide"
)

# ------------------ QUESTIONS ------------------

QUESTIONS = [

    {"sentence":"The cat ____ on the sofa.",
     "correct":"sits",
     "wrong":"sit",
     "explanation":"One cat = singular, so we add s."},

    {"sentence":"The dogs ____ in the park.",
     "correct":"run",
     "wrong":"runs",
     "explanation":"Many dogs = plural, so we do not add s."},

    {"sentence":"My sister ____ every morning.",
     "correct":"runs",
     "wrong":"run",
     "explanation":"One sister = singular, so we use runs."},

    {"sentence":"The birds ____ in the sky.",
     "correct":"fly",
     "wrong":"flies",
     "explanation":"Many birds = plural, so we use fly."},

    {"sentence":"Dad ____ coffee.",
     "correct":"drinks",
     "wrong":"drink",
     "explanation":"One dad = singular, so we use drinks."},

    {"sentence":"The children ____ to school.",
     "correct":"walk",
     "wrong":"walks",
     "explanation":"Children means many people, so we use walk."},

    {"sentence":"The monkey ____ bananas.",
     "correct":"likes",
     "wrong":"like",
     "explanation":"One monkey = singular, so we use likes."},

    {"sentence":"The fish ____ together.",
     "correct":"swim",
     "wrong":"swims",
     "explanation":"Many fish = plural, so we use swim."}
]

# ------------------ SESSION STATE ------------------

if "score" not in st.session_state:
    st.session_state.score = 0

if "health" not in st.session_state:
    st.session_state.health = 3

if "level" not in st.session_state:
    st.session_state.level = 1

if "question" not in st.session_state:
    st.session_state.question = random.choice(QUESTIONS)

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "answered" not in st.session_state:
    st.session_state.answered = False

# ------------------ STYLING ------------------

st.markdown("""
<style>

.stApp{
background:linear-gradient(180deg,#020024,#090979,#00d4ff);
}

.bigtitle{
text-align:center;
font-size:50px;
font-weight:bold;
color:#FFD700;
}

.panel{
background:#14213d;
padding:15px;
border-radius:20px;
color:white;
font-size:24px;
text-align:center;
}

.question{
background:#ffffff;
padding:25px;
border-radius:20px;
font-size:30px;
font-weight:bold;
text-align:center;
}

.feedback{
background:#fff3cd;
padding:15px;
border-radius:15px;
font-size:22px;
}

.alien{
font-size:90px;
text-align:center;
}

.ship{
font-size:100px;
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ------------------ HEADER ------------------

st.markdown(
'<div class="bigtitle">🚀 Grammar Space Invaders 👾</div>',
unsafe_allow_html=True
)

st.write("")

col1,col2,col3=st.columns(3)

with col1:
    st.markdown(
    f'<div class="panel">⭐ Score<br>{st.session_state.score}</div>',
    unsafe_allow_html=True
    )

with col2:
    st.markdown(
    f'<div class="panel">❤️ Health<br>{st.session_state.health}</div>',
    unsafe_allow_html=True
    )

with col3:
    st.markdown(
    f'<div class="panel">🏆 Level<br>{st.session_state.level}</div>',
    unsafe_allow_html=True
    )

st.write("")

# ------------------ GAME OVER ------------------

if st.session_state.health <= 0:

    st.error("👾 GAME OVER!")

    st.subheader(f"Final Score: {st.session_state.score}")

    if st.button("🔄 Play Again"):

        st.session_state.score=0
        st.session_state.health=3
        st.session_state.level=1
        st.session_state.question=random.choice(QUESTIONS)
        st.session_state.feedback=""
        st.session_state.answered=False

        st.rerun()

    st.stop()

# ------------------ ALIEN ------------------

st.markdown(
'<div class="alien">👾</div>',
unsafe_allow_html=True
)

q=st.session_state.question

st.markdown(
f'<div class="question">{q["sentence"]}</div>',
unsafe_allow_html=True
)

st.write("")

answers=[q["correct"],q["wrong"]]

random.shuffle(answers)

left,right=st.columns(2)

# ------------------ SHOOT BUTTONS ------------------

if not st.session_state.answered:

    with left:

        if st.button(f"🔫 Shoot {answers[0]}",
                     use_container_width=True):

            selected=answers[0]

            st.session_state.answered=True

            if selected==q["correct"]:

                st.session_state.score +=10

                st.session_state.feedback=(
                    f"🎉 Alien destroyed!\n\n💡 {q['explanation']}"
                )

            else:

                st.session_state.health -=1

                st.session_state.feedback=(
                    f"😃 Oops!\n\nCorrect answer: {q['correct']}\n\n💡 {q['explanation']}"
                )

            st.rerun()

    with right:

        if st.button(f"🔫 Shoot {answers[1]}",
                     use_container_width=True):

            selected=answers[1]

            st.session_state.answered=True

            if selected==q["correct"]:

                st.session_state.score +=10

                st.session_state.feedback=(
                    f"🎉 Alien destroyed!\n\n💡 {q['explanation']}"
                )

            else:

                st.session_state.health -=1

                st.session_state.feedback=(
                    f"😃 Oops!\n\nCorrect answer: {q['correct']}\n\n💡 {q['explanation']}"
                )

            st.rerun()

# ------------------ FEEDBACK ------------------

if st.session_state.answered:

    st.markdown(
    f'<div class="feedback">{st.session_state.feedback}</div>',
    unsafe_allow_html=True
    )

    if st.session_state.score > 0 and st.session_state.score % 30 == 0:
        st.session_state.level += 1
        st.balloons()

    st.write("")

    st.markdown(
    '<div class="ship">🚀</div>',
    unsafe_allow_html=True
    )

    if st.button("➡️ Next Alien"):

        st.session_state.question=random.choice(QUESTIONS)

        st.session_state.feedback=""

        st.session_state.answered=False

        st.rerun()

# ------------------ INSTRUCTIONS ------------------

st.write("---")

st.info("""

🎮 HOW TO PLAY

👾 Aliens are attacking Earth.

🚀 Read the sentence.

🔫 Shoot the correct verb.

⭐ Correct answer = +10 points

❤️ Wrong answer = lose 1 health

🏆 Every 30 points = Level Up

Destroy as many aliens as you can!

""")
