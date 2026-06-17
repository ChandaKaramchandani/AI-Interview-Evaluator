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
    page_title="AI Interview Evaluator",
    page_icon="🎯",
    layout="wide"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b
    );
}

/* SIDEBAR */

[data-testid="stSidebar"]{
    background:#0f172a !important;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* REMOVE WHITE STREAMLIT CONTAINERS */

div[data-testid="stVerticalBlock"]{
    background:transparent !important;
}

div[data-testid="stMarkdownContainer"]{
    background:transparent !important;
}

[data-testid="stContainer"]{
    background:transparent !important;
}

/* Labels */

label{
    color:white !important;
    font-size:18px !important;
    font-weight:bold !important;
}

/* Text Input */

.stTextInput input{
    background:#1e293b !important;
    color:white !important;
    border:1px solid #475569 !important;
    border-radius:12px !important;
}

/* Text Area */

.stTextArea textarea{
    background:#1e293b !important;
    color:white !important;
    border:1px solid #475569 !important;
    border-radius:12px !important;
}

/* Placeholder */

input::placeholder,
textarea::placeholder{
    color:#cbd5e1 !important;
}

/* MAIN BOX */

.main-box{
    background:#1e293b !important;
    color:white !important;
    padding:25px;
    border-radius:20px;
    border:1px solid #334155;
    box-shadow:0px 10px 30px rgba(0,0,0,0.25);
    margin-bottom:20px;
    transition:0.3s;
}

.main-box *{
    color:white !important;
}

.main-box:hover{
    transform:translateY(-5px);
    border:1px solid #60a5fa;
    box-shadow:0px 15px 35px rgba(37,99,235,.35);
}

/* RESULT BOX */

.result-box{
    background:linear-gradient(135deg,#0f172a,#1e293b) !important;
    color:#f1f5f9 !important;
    padding:35px;
    border-radius:18px;
    margin-top:20px;
    border:1px solid #334155;
    box-shadow:0 10px 25px rgba(0,0,0,0.5);
    line-height:2;
    font-size:16px;
    transition:0.3s;
}

.result-box:hover{
    transform:translateY(-5px);
    border:1px solid #8b5cf6;
    box-shadow:0px 15px 35px rgba(124,58,237,.35);
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

/* CHAT BOX */

.chat-box{
    background:#1e293b !important;
    color:white !important;
    padding:25px;
    border-radius:20px;
    border:1px solid #334155;
    transition:0.3s;
}

.chat-box:hover{
    transform:translateY(-5px);
    border:1px solid #22c55e;
    box-shadow:0px 15px 35px rgba(34,197,94,.30);
}

.chat-box *{
    color:white !important;
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
    color:white !important;
    font-size:18px;
    font-weight:bold;
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-3px);
    box-shadow:0px 10px 25px rgba(37,99,235,.45);
}

/* Main Heading */

h1{
    color:white !important;
    text-align:center;
    font-size:50px;
    font-weight:700;
}

/* Headings */

h2,h3,h4,h5,h6{
    color:white !important;
}

/* Text */

p,
span,
li{
    color:white !important;
}

/* Metrics */

[data-testid="metric-container"]{
    background:#1e293b !important;
    color:white !important;
    padding:15px;
    border-radius:15px;
    border:1px solid #334155;
    box-shadow:0px 5px 15px rgba(0,0,0,0.15);
}

[data-testid="metric-container"] *{
    color:white !important;
}

/* File Uploader */

[data-testid="stFileUploader"]{
    background:#1e293b !important;
    border:1px solid #334155 !important;
    border-radius:15px !important;
}

/* Expander */

.streamlit-expanderHeader{
    color:white !important;
}

.streamlit-expanderContent{
    background:#1e293b !important;
    color:white !important;
}

/* Alerts */

.stAlert{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<h1>
🎯 AI Interview Evaluator
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style="
text-align:center;
color:white;
font-size:22px;
margin-bottom:30px;
">
Evaluate Your Interview Answers Like a Real HR 🚀
</p>
""", unsafe_allow_html=True)

# =========================
# INPUTS
# =========================

col1, col2 = st.columns(2)

with col1:

    job_role = st.text_input(
        "💼 Job Role",
        placeholder="Python Developer"
    )

    question = st.text_area(
        "❓ Interview Question",
        placeholder="What is Python?"
    )

with col2:

    answer = st.text_area(
        "✍️ Your Answer",
        placeholder="Write your answer here...",
        height=220
    )

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("""
    <div style="
        background:#1e293b;
        padding:20px;
        border-radius:15px;
        text-align:center;
        margin-bottom:15px;
    ">
        <h2 style="color:white;">
        🎯 AI HR Assistant
        </h2>
        <p style="color:#cbd5e1;">
        Smart Interview Evaluation System
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("💼 Interview Practice")
    st.success("🤖 AI Evaluation")
    st.success("📈 Skill Improvement")

    st.markdown("---")

    st.markdown("""
    <h3 style="color:white;">
    🚀 Features
    </h3>

    <p style="color:white;">
    ✅ Technical Analysis<br><br>
    ✅ Communication Score<br><br>
    ✅ HR Feedback<br><br>
    ✅ Improved Answer<br><br>
    ✅ Confidence Score<br><br>
    ✅ Interview Readiness
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("""
    <h3 style="color:white;">
    📊 Evaluation Metrics
    </h3>

    <p style="color:white;">
    🎯 Overall Score<br><br>
    💡 Technical Accuracy<br><br>
    🗣 Communication Skills<br><br>
    🚀 Confidence Level<br><br>
    📈 Final Recommendation
    </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.info("🤖 Powered by Groq AI")

# =========================
# BUTTON
# =========================

if st.button("🚀 Evaluate Answer"):

    if not job_role or not question or not answer:

        st.warning("⚠️ Please fill all fields.")

    else:

        with st.spinner(
            "🤖 AI HR is evaluating your answer..."
        ):

            prompt = f"""

Act as a professional interviewer.

Job Role:
{job_role}

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate and provide:

# Overall Score (/10)

# Technical Accuracy Score

# Communication Score

# Confidence Score

# Strengths

# Weaknesses

# Missing Points

# Improved Answer Example

# HR Feedback

# Final Recommendation

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
                "✅ Evaluation Completed Successfully"
            )

            # =========================
            # SMART EVALUATION CARD
            # =========================

            st.markdown("""
            <div class="main-box">

            <h2>🚀 Smart Interview Evaluation</h2>

            ✅ Technical Analysis<br><br>
            ✅ Communication Score<br><br>
            ✅ HR Feedback<br><br>
            ✅ Improved Answer<br><br>
            ✅ Confidence Evaluation<br><br>
            ✅ Interview Readiness Score

            </div>
            """, unsafe_allow_html=True)

            # =========================
            # METRICS
            # =========================

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "🎯 Evaluation",
                    "Completed"
                )

            with col2:
                st.metric(
                    "💼 Role",
                    job_role
                )

            with col3:
                st.metric(
                    "🤖 AI HR",
                    "Active"
                )

            # =========================
            # RESULT BOX
            # =========================

            st.markdown(
                f"""
                <div class="result-box">
                    <h2>🎯 Interview Evaluation Report</h2>
                    <hr>
                    {result.replace(chr(10), '<br>')}
                </div>
                """,
                unsafe_allow_html=True
            )