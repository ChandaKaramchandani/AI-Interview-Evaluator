import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import os

# =========================
# LOAD ENV
# =========================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="AI Quiz Generator",
    page_icon="📝",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background:linear-gradient(
        135deg,
        #020617,
        #0f172a,
        #1e293b
    );
}

/* Sidebar */

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #111827,
        #1e1b4b,
        #312e81
    );
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* Labels */

label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* Input */

.stTextInput input{
    background:#1e293b !important;
    color:white !important;
    border:1px solid #475569 !important;
    border-radius:12px !important;
}

/* Button */

.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );
    color:white;
    font-size:18px;
    font-weight:bold;
}

/* Result Box */

.result-box{
    background:linear-gradient(135deg,#0f172a,#1e293b);
    color:#f1f5f9 !important;
    padding:35px;
    border-radius:18px;
    margin-top:20px;
    border:1px solid #334155;
    box-shadow:0 10px 25px rgba(0,0,0,0.5);
    line-height:2;
    font-size:16px;
}

.result-box h1,
.result-box h2,
.result-box h3,
.result-box h4,
.result-box h5,
.result-box h6{
    color:#60a5fa !important;
    margin-top:20px;
}

.result-box p,
.result-box li,
.result-box span{
    color:#e2e8f0 !important;
}

.result-box strong{
    color:#fbbf24 !important;
}

.result-box hr{
    border:none;
    height:1px;
    background:#334155;
    margin:15px 0;
}

h1{
    color:white !important;
    text-align:center;
}

p{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("""
    <h2 style='text-align:center;color:white;'>
    📝 AI Quiz Generator
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("📚 Smart Quiz")
    st.info("🎯 Topic Based Questions")
    st.warning("🧠 AI Learning")

    st.markdown("---")

    st.markdown("""
    ### 🚀 Features

    ✅ 10 MCQs

    ✅ Correct Answers

    ✅ Explanations

    ✅ Topic Based Quiz

    ✅ Interview Preparation

    ✅ Quick Revision
    """)

# =========================
# HEADER
# =========================

st.title("📝 AI Quiz Generator")

st.markdown("""
<p style="
text-align:center;
color:white;
font-size:22px;
margin-bottom:20px;
">
Generate Professional AI Powered Quizzes 🚀
</p>
""", unsafe_allow_html=True)

# =========================
# INPUT
# =========================

topic = st.text_input(
    "📚 Enter Quiz Topic",
    placeholder="Python, Machine Learning, DBMS"
)

# =========================
# GENERATE QUIZ
# =========================

if st.button(
    "🚀 Generate Quiz",
    use_container_width=True
):

    if not topic:

        st.warning(
            "⚠️ Please enter a topic."
        )

    else:

        with st.spinner(
            "🤖 AI is creating quiz..."
        ):

            prompt = f"""

Create a professional quiz on:

{topic}

Include:

# 10 MCQs

# 4 Options Each

# Correct Answers

# Short Explanation

"""

            try:

                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role":"user",
                            "content":prompt
                        }
                    ]
                )

                result = completion.choices[0].message.content

            except Exception as e:

                st.error(f"❌ Error: {e}")
                st.stop()

            st.success(
                "✅ Quiz Generated Successfully"
            )

            st.markdown(
                f"""
                <div class="result-box">
                    <h2>📝 Generated Quiz</h2>
                    <hr>
                    {result.replace(chr(10), '<br>')}
                </div>
                """,
                unsafe_allow_html=True
            )