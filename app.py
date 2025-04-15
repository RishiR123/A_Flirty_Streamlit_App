import streamlit as st
import random


st.set_page_config(page_title="Do You Like Me? 💘", page_icon="😳", layout="centered")


flirts = [
    ("Are you made of copper and tellurium? Because you're Cu-Te 😘", "😍"),
    ("Are you French? Because Eiffel for you 🗼", "😚"),
    ("I’m no photographer, but I can picture us together 📸", "🥰"),
    ("If you were a vegetable, you'd be a cute-cumber 🥒", "😻"),
    ("You must be tired — you’ve been running through my mind all day 🏃‍♀️", "💖"),
    ("Your hand looks heavy—can I hold it for you? 🤝", "😉"),
    ("Do you have a name, or can I call you mine? 🫦", "💘"),
]

roasts = [
    ("No? Bro, your taste is broken 💀", "🤡"),
    ("Wow. Even the mirror avoids you 😶", "🪞"),
    ("You're the reason shampoo has instructions 😬", "🧼"),
    ("Rejecting me? Bold of you 😒", "🔥"),
    ("I’d agree with you, but then we’d both be wrong 😎", "💢"),
    ("Not even Google could find your standards 🙃", "📉"),
    ("Your WiFi signal has more stability than your decisions 🤖", "📶"),
]


if "said_yes" not in st.session_state:
    st.session_state.said_yes = False
if "mode" not in st.session_state:
    st.session_state.mode = None
if "line" not in st.session_state:
    st.session_state.line = ""
if "emoji" not in st.session_state:
    st.session_state.emoji = ""


st.markdown("<h1 style='text-align:center;'>Do you like me? 😳</h1>", unsafe_allow_html=True)


if st.session_state.line:
    color = "#ffe6f2" if st.session_state.mode == "flirt" else "#fff0f0"
    st.markdown(f"""
        <div style='background-color:{color}; padding: 25px; border-radius: 15px; margin-top: 30px; text-align: center; border: 2px dashed #ff66b3; font-size: 22px;'>
            {st.session_state.line}<br><br><span style='font-size: 60px;'>{st.session_state.emoji}</span>
        </div>
    """, unsafe_allow_html=True)


col1, col2 = st.columns(2)
with col1:
    if st.button("Yes 😍"):
        st.session_state.said_yes = True
        st.balloons()
with col2:
    if st.button("No 🙄"):
        if random.choice(["flirt", "roast"]) == "flirt":
            line, emoji = random.choice(flirts)
            st.session_state.mode = "flirt"
        else:
            line, emoji = random.choice(roasts)
            st.session_state.mode = "roast"
        st.session_state.line = line
        st.session_state.emoji = emoji
        st.rerun()


if st.session_state.said_yes:
    st.markdown("<h2 style='text-align:center; color: #ff3399;'>Yayyy! I knew it 💘</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align:center;'>💏 💞 🫶 🥳 💓</h1>", unsafe_allow_html=True)
    st.success("Now let’s go get biryani together or something 😌")

