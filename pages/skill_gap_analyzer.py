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
    page_title="AI Skill Gap Analyzer",
    page_icon="📊",
    layout="wide"
)

# =========================
# CSS
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

/* Inputs */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"]{
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
    📊 AI Skill Gap Analyzer
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("🚀 Skill Analysis")
    st.info("📈 Career Growth")
    st.warning("🎯 Job Readiness")

    st.markdown("---")

    st.markdown("""
    ### Features

    ✅ Skill Gap Analysis

    ✅ Missing Skills

    ✅ Learning Roadmap

    ✅ Certifications

    ✅ ATS Keywords

    ✅ Interview Preparation
    """)

# =========================
# HEADER
# =========================

st.title("📊 AI Skill Gap Analyzer")

st.markdown("""
<p style="
text-align:center;
color:white;
font-size:22px;
margin-bottom:25px;
">
Analyze Missing Skills For Your Dream Job 🚀
</p>
""", unsafe_allow_html=True)

# =========================
# USER INPUT
# =========================

current_skills = st.text_area(
    "🛠️ Enter Your Current Skills",
    placeholder="Python, SQL, Excel, Power BI"
)

target_role = st.text_input(
    "🎯 Target Job Role",
    placeholder="Data Scientist"
)

experience = st.selectbox(
    "💼 Experience Level",
    [
        "Student",
        "Fresher",
        "1-2 Years",
        "3-5 Years",
        "5+ Years"
    ]
)

# =========================
# ANALYZE BUTTON
# =========================

if st.button(
    "🚀 Analyze Skill Gap",
    use_container_width=True
):

    if not current_skills or not target_role:

        st.warning(
            "⚠️ Please enter your skills and target role."
        )

    else:

        with st.spinner(
            "🤖 Analyzing Skills..."
        ):

            prompt = f"""

Analyze the following profile:

Current Skills:
{current_skills}

Target Job Role:
{target_role}

Experience Level:
{experience}

Provide:

# Current Strengths

# Missing Skills

# Technical Skills To Learn

# Soft Skills To Improve

# Recommended Certifications

# Learning Roadmap

# Project Ideas

# Interview Preparation Tips

# ATS Keywords Required

# Estimated Job Readiness Score (0-100)

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
                "✅ Skill Analysis Completed Successfully"
            )

            st.markdown(
                f"""
                <div class="result-box">
                    <h2>📊 Skill Gap Analysis Report</h2>
                    <hr>
                    {result.replace(chr(10), '<br>')}
                </div>
                """,
                unsafe_allow_html=True
            )