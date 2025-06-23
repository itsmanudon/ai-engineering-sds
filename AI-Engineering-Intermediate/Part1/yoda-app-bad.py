import streamlit as st
import random

# --- List of Yoda Quotes ---
YODA_QUOTES = [
    "Do or do not. There is no try.",
    "The greatest teacher, failure is.",
    "You must unlearn what you have learned.",
    "Train yourself to let go of everything you fear to lose.",
    "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
    "When you look at the dark side, careful you must be. For the dark side looks back.",
    "Pass on what you have learned.",
    "In a dark place we find ourselves, and a little more knowledge lights our way.",
    "Much to learn, you still have.",
    "Named must your fear be before banish it you can.",
    "Truly wonderful, the mind of a child is.",
    "Difficult to see. Always in motion is the future.",
    "Adventure. Excitement. A Jedi craves not these things.",
    "Always pass on what you have learned.",
    "A Jedi uses the Force for knowledge and defense, never for attack.",
]

# --- App Styling ---
st.set_page_config(page_title="Yoda Quote Generator", page_icon="🟢", layout="centered")

def yoda_style(text):
    return f"""
    <div style="
        background: #202a44;
        border-radius: 18px;
        padding: 30px 35px;
        margin: 25px 0 10px 0;
        color: #9efb64;
        font-size: 2rem;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        box-shadow: 0 0 20px 4px #3f883d44;
        text-align: center;
    ">
        <span style="font-weight:500; letter-spacing:1px;">{text}</span>
    </div>
    """

with st.container():
    st.markdown(
        """
        <h1 style='text-align:center; color:#9efb64; font-size:3rem; margin-bottom: 10px;'>🟢 Random Yoda Quote</h1>
        <p style='text-align:center; color:#b5fcba; font-size:1.2rem;'>Click the button and discover wisdom from Master Yoda.</p>
        """,
        unsafe_allow_html=True
    )

    # stateful button, so a new quote stays until the next click
    if 'quote' not in st.session_state:
        st.session_state.quote = "Click the button, you must!"

    if st.button("Generate Quote ⭐", use_container_width=True):
        st.session_state.quote = random.choice(YODA_QUOTES)

    st.markdown(yoda_style(st.session_state.quote), unsafe_allow_html=True)

    st.markdown(
        """
        <div style="text-align:center; font-size: 0.95rem; color:#bbbbbb; margin-top: 40px;">
        May the Force be with you.<br>
        <span style="font-size: 1.4em;">🌌</span>
        </div>
        """,
        unsafe_allow_html=True
    )