import streamlit as st
import os
from dotenv import load_dotenv
from cloner import get_style_analysis, generate_proxy_response

load_dotenv()

st.set_page_config(page_title="Digital-Twin-Pro", page_icon="🎭", layout="wide")

# Custom CSS for Premium Look
st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stButton>button { background-color: #8b5cf6; color: white; border-radius: 8px; border: none; }
    .stTextArea>div>div>textarea { background-color: #1e293b; color: white; border: 1px solid #475569; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎭 Digital-Twin-Pro")
st.caption("Empowering your autonomous digital presence.")

if not os.getenv("OPENAI_API_KEY"):
    st.error("Please set your OPENAI_API_KEY in the .env file.")
    st.stop()

tab1, tab2 = st.tabs(["🧠 Train Style", "🤖 Digital Proxy"])

with tab1:
    st.header("1. Feed your Twin")
    st.info("Paste 3-5 examples of your writing (emails, tweets, or blogs) so your Twin can learn your voice.")
    
    samples = st.text_area("Writing Samples", height=300, placeholder="Example 1: Hey everyone, just pushed a new update...\nExample 2: Appreciate the feedback, will look into it...")
    
    if st.button("Analyze & Save Style"):
        if samples.strip():
            with st.spinner("Analyzing your linguistic DNA..."):
                style = get_style_analysis(samples)
                st.session_state['style_profile'] = style
                st.success("Style Profile Generated!")
                st.markdown(f"***Your Profile:***\n\n{style}")
        else:
            st.warning("Please provide samples first.")

with tab2:
    st.header("2. Put your Twin to work")
    
    if 'style_profile' not in st.session_state:
        st.warning("Please complete the 'Train Style' step first.")
    else:
        situation = st.text_input("Situation / Task", placeholder="e.g. Reply to this recruiter email politely but saying I'm not interested.")
        context = st.text_area("Additional Context (Optional)", placeholder="e.g. The recruiter is from Google, and I just started a new job.")
        
        if st.button("Generate Digital Response"):
            with st.spinner("Your Twin is thinking..."):
                response = generate_proxy_response(situation, st.session_state['style_profile'], context)
                st.subheader("Twin Response:")
                st.write(response)
                st.button("🔊 Play Voice (Coming Soon)", disabled=True)
