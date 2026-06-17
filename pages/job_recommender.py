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
    page_title="AI Job Recommender",
    page_icon="💼",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* Main Background */
.stApp{
    background:linear-gradient(135deg,#0f172a,#1e293b) !important;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0f172a,#1e293b) !important;
    border-right:1px solid #334155;
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* Labels */
label{
    color:#e2e8f0 !important;
    font-size:17px !important;
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
    color:#94a3b8 !important;
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

/* Button */
.stButton > button{
    width:100%;
    height:55px;
    border:none;
    border-radius:12px;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    font-size:18px;
    font-weight:bold;
    margin-top:10px;
}

.stButton > button:hover{
    background:linear-gradient(90deg,#1d4ed8,#6d28d9);
    transform:scale(1.01);
}

/* Main Heading */
h1{
    color:white !important;
    text-align:center;
    font-size:48px;
    font-weight:800;
}

/* Subheading */
p{
    color:#e2e8f0 !important;
}

/* Metrics */
[data-testid="metric-container"]{
    background:#1e293b !important;
    padding:15px;
    border-radius:15px;
    border:1px solid #334155;
    box-shadow:0px 5px 15px rgba(0,0,0,0.3);
}

[data-testid="metric-container"] *{
    color:white !important;
}

/* Alerts */
.stAlert{
    border-radius:12px;
}

/* Info box */
.stInfo{
    background:#1e3a5f !important;
    color:white !important;
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.title("💼 AI Job Recommender")

st.markdown("""
<p style="
text-align:center;
color:#94a3b8;
font-size:20px;
margin-bottom:30px;
">
Find the Best Career Opportunities with AI 🚀
</p>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("""
    <h2 style='color:white;text-align:center;'>
    💼 AI Career Advisor
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("🚀 Career Planning")
    st.info("💼 Job Recommendations")
    st.warning("📈 Skill Analysis")

    st.markdown("---")

    st.markdown("""
    ### 🎯 Features

    ✅ Best Job Roles

    ✅ Salary Insights

    ✅ Missing Skills

    ✅ Career Roadmap

    ✅ Certifications

    ✅ Interview Tips

    ✅ Future Scope
    """)

# =========================
# INPUTS
# =========================

col1, col2 = st.columns(2)

with col1:

    skills = st.text_area(
        "🛠️ Enter Your Skills",
        placeholder="Python, SQL, Power BI, Machine Learning"
    )

    career_goal = st.text_input(
        "🎯 Career Goal",
        placeholder="Data Scientist"
    )

with col2:

    experience = st.selectbox(
        "💼 Experience Level",
        [
            "Fresher",
            "1-2 Years",
            "3-5 Years",
            "5+ Years"
        ]
    )

    st.info(
        "💡 Enter accurate skills for better recommendations."
    )

# =========================
# BUTTON
# =========================

if st.button(
    "🚀 Find Best Jobs",
    use_container_width=True
):

    if not skills or not career_goal:

        st.warning(
            "⚠️ Please enter skills and career goal."
        )

    else:

        with st.spinner(
            "🤖 Finding Best Career Opportunities..."
        ):

            prompt = f"""
You are an expert career advisor. Analyze this profile and give detailed recommendations.

Skills: {skills}
Career Goal: {career_goal}
Experience: {experience}

Provide a detailed response with these sections:

## 🎯 Best Job Roles
## 💰 Salary Range
## ✅ Required Skills
## ❌ Missing Skills
## 🗺️ Career Roadmap
## 📜 Recommended Certifications
## 📚 Best Learning Resources
## 🎤 Interview Preparation Tips
## 🔮 Future Scope
## 🛠️ Top Projects To Build
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
            "✅ Career Analysis Completed Successfully!"
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "💼 Experience",
                experience
            )

        with col2:
            st.metric(
                "🎯 Goal",
                career_goal
            )

        with col3:
            st.metric(
                "🤖 AI Status",
                "Active ✅"
            )

        st.markdown(
            f"""
            <div class="result-box">
                <h2>💼 Career Recommendation Report</h2>
                <hr>
                {result.replace(chr(10), '<br>')}
            </div>
            """,
            unsafe_allow_html=True
        )