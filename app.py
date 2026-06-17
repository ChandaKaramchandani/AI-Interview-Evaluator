# # =========================
# 🧠 AI GURU FINAL VERSION
# =========================

import streamlit as st
from groq import Groq
import pdfplumber
from docx import Document
from dotenv import load_dotenv
from fpdf import FPDF
import os

# =========================
# PAGE CONFIG (TOP PAR)
# =========================

st.set_page_config(
    page_title="AI Guru",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# LOAD ENV
# =========================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# =========================
# SESSION STATE
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_feature" not in st.session_state:
    st.session_state.selected_feature = "🏠 Dashboard"

FEATURES = [
    "🏠 Dashboard",
    "🤖 AI Chat",
    "📄 Resume Analyzer",
    "📚 Study Assistant",
    "✨ Prompt Generator",
    "🎯 Career Guidance",
    "🎤 Mock Interview"
]

# =========================
# PDF FUNCTION
# =========================

def create_pdf(text, filename):

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    clean_text = text.encode(
        "latin-1",
        "replace"
    ).decode("latin-1")

    pdf.multi_cell(
        0,
        10,
        clean_text
    )

    pdf.output(filename)
# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>

/* =========================
   AI GURU PRO THEME
========================= */

.stApp{
    background:linear-gradient(
        135deg,
        #0f172a 0%,
        #111827 50%,
        #1e293b 100%
    );
}

/* =========================
   REMOVE ALL WHITE BOXES
========================= */

.main .block-container{
    background:transparent !important;
    padding-top:2rem;
}

[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stVerticalBlock"],
[data-testid="stMarkdownContainer"],
[data-testid="stContainer"],
[data-testid="element-container"],
section.main{
    background:transparent !important;
}

/* =========================
   AI GURU MAIN HEADING
========================= */

h1{
    font-size:52px !important;
    font-weight:900 !important;
    text-align:center !important;

    background:linear-gradient(
        90deg,
        #60a5fa,
        #8b5cf6,
        #22c55e
    );

    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;

    letter-spacing:2px;

    margin-bottom:10px;
}

h2{
    color:white !important;
    font-size:28px !important;
    font-weight:700 !important;
}

h3{
    color:white !important;
    font-size:22px !important;
    font-weight:600 !important;
}

h4{
    color:white !important;
    font-size:18px !important;
    font-weight:600 !important;
}

/* =========================
   SIDEBAR
========================= */

[data-testid="stSidebar"]{
    background:linear-gradient(
        180deg,
        #1e293b,
        #0f172a
    );
}

[data-testid="stSidebar"] *{
    color:white !important;
}

/* =========================
   TEXT
========================= */

p,
span,
li,
label,
small,
div{
    color:#e2e8f0 !important;
}

/* =========================
   INPUTS
========================= */

.stTextInput input,
.stTextArea textarea{

    background:#111827 !important;
    color:white !important;

    border:1px solid #334155 !important;
    border-radius:12px !important;
}

.stTextInput input:focus,
.stTextArea textarea:focus{

    border:1px solid #60a5fa !important;

    box-shadow:0 0 12px rgba(
        96,165,250,.45
    );
}

input::placeholder,
textarea::placeholder{
    color:#94a3b8 !important;
}

/* =========================
   SELECTBOX
========================= */

div[data-baseweb="select"] > div{

    background:#111827 !important;
    color:white !important;

    border:1px solid #334155 !important;
    border-radius:12px !important;
}

div[data-baseweb="select"] span{
    color:white !important;
}

div[role="listbox"]{

    background:#111827 !important;
    border:1px solid #334155 !important;
}

div[role="option"]{
    background:#111827 !important;
    color:white !important;
}

div[role="option"]:hover{
    background:#1e293b !important;
}

/* =========================
   BUTTONS
========================= */

.stButton > button{

    width:100%;

    background:linear-gradient(
        90deg,
        #2563eb,
        #7c3aed
    );

    color:white !important;

    border:none;
    border-radius:12px;

    font-weight:600;

    transition:.3s;
}

.stButton > button:hover{

    transform:translateY(-4px);

    box-shadow:0px 15px 30px rgba(
        37,99,235,.40
    );
}

/* =========================
   DOWNLOAD BUTTON
========================= */

[data-testid="stDownloadButton"] button{

    width:100%;

    background:#111827 !important;

    color:black !important;

    border:1px solid #475569 !important;

    border-radius:12px !important;
}

[data-testid="stDownloadButton"] button:hover{

    background:#2563eb !important;

    border-color:#2563eb !important;
}

/* =========================
   CHAT BOX
========================= */

.chat-box{

    background:#111827 !important;

    padding:25px;

    border-radius:20px;

    border:1px solid #334155;

    margin-bottom:15px;

    transition:.3s;
}

.chat-box:hover{

    transform:translateY(-5px);

    border-color:#22c55e;

    box-shadow:0px 15px 30px rgba(
        34,197,94,.25
    );
}

.chat-box *{
    color:white !important;
}

/* =========================
   RESULT BOX
========================= */

.result-box{

    background:#111827 !important;

    padding:25px;

    border-radius:20px;

    border:1px solid #334155;

    margin-top:15px;

    transition:.3s;
}

.result-box:hover{

    transform:translateY(-5px);

    border-color:#8b5cf6;

    box-shadow:0px 15px 30px rgba(
        139,92,246,.25
    );
}

.result-box *{
    color:white !important;
}

/* =========================
   MAIN BOX
========================= */

.main-box{

    background:#111827 !important;

    padding:25px;

    border-radius:20px;

    border:1px solid #334155;

    margin-bottom:15px;

    transition:.3s;
}

.main-box:hover{

    transform:translateY(-5px);

    border-color:#60a5fa;

    box-shadow:0px 15px 30px rgba(
        96,165,250,.25
    );
}

.main-box *{
    color:white !important;
}

/* =========================
   FILE UPLOADER
========================= */

[data-testid="stFileUploader"]{

    background:#111827 !important;

    border:1px solid #334155 !important;

    border-radius:15px !important;

    padding:15px !important;
}

[data-testid="stFileUploader"] *{
    color:white !important;
}

/* =========================
   EXPANDER
========================= */

[data-testid="stExpander"]{

    background:#111827 !important;

    border:1px solid #334155 !important;

    border-radius:15px !important;
}

[data-testid="stExpander"] *{
    color:white !important;
}

/* =========================
   METRICS
========================= */

[data-testid="metric-container"]{

    background:#111827 !important;

    border:1px solid #334155;

    border-radius:15px;

    padding:15px;
}

[data-testid="metric-container"] *{
    color:white !important;
}

/* =========================
   CODE BLOCKS
========================= */

pre,
code,
.stCodeBlock{

    background:#111827 !important;

    color:white !important;

    border:1px solid #334155 !important;

    border-radius:12px !important;
}

/* =========================
   ALERTS
========================= */

.stAlert{
    border-radius:12px;
}

/* =========================
   MARKDOWN
========================= */

.stMarkdown,
.stMarkdown *{
    color:white !important;
}
/* =========================
   ULTRA DARK SELECTBOX FIX
========================= */

/* Main Select Box */

.stSelectbox > div > div{
    background:#111827 !important;
    color:white !important;
    border:1px solid #334155 !important;
    border-radius:12px !important;
}

/* Selected Value */

.stSelectbox div[data-baseweb="select"] *{
    color:white !important;
}

/* Dropdown Popup */

div[data-baseweb="popover"]{
    background:#111827 !important;
    border:1px solid #334155 !important;
}

/* Menu */

div[data-baseweb="menu"]{
    background:#111827 !important;
    border:1px solid #334155 !important;
}

/* List */

ul[role="listbox"]{
    background:#111827 !important;
}

/* Options */

li[role="option"]{
    background:#111827 !important;
    color:white !important;
}

/* Hover */

li[role="option"]:hover{
    background:#1e293b !important;
    color:white !important;
}

/* Selected Option */

li[aria-selected="true"]{
    background:#2563eb !important;
    color:white !important;
}

/* Force Text White */

div[data-baseweb="popover"] *,
div[data-baseweb="menu"] *,
ul[role="listbox"] *,
li[role="option"] *{
    color:white !important;
}

/* Scrollbar */

div[data-baseweb="popover"] ::-webkit-scrollbar{
    width:8px;
}

div[data-baseweb="popover"] ::-webkit-scrollbar-track{
    background:#111827;
}

div[data-baseweb="popover"] ::-webkit-scrollbar-thumb{
    background:#334155;
    border-radius:10px;
}

/* SVG Arrow */

.stSelectbox svg{
    fill:white !important;
}
</style>
""", unsafe_allow_html=True)


# =========================
# HOME / DASHBOARD
# =========================
if st.session_state.selected_feature == "🏠 Dashboard":
    st.markdown("""
<h1>🧠 AI GURU</h1>

<p style="
text-align:center;
font-size:20px;
font-weight:600;
background:linear-gradient(90deg,#60a5fa,#8b5cf6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
margin-top:-10px;
margin-bottom:30px;
">
Study • Career • Resume • Interview • AI Assistant
</p>
""", unsafe_allow_html=True)

    st.markdown("## 🚀 AI Guru Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="chat-box">
        <h3>🤖 AI Chat Assistant</h3>
        <p>Ask questions and get instant AI answers.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🤖 AI Chat", use_container_width=True):
            st.session_state.selected_feature = "🤖 AI Chat"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="chat-box">
        <h3>📄 Resume Analyzer</h3>
        <p>Upload resume and get ATS analysis.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📄 Resume Analyzer", use_container_width=True):
            st.session_state.selected_feature = "📄 Resume Analyzer"
            st.rerun()

    with col3:
        st.markdown("""
        <div class="chat-box">
        <h3>📚 Study Assistant</h3>
        <p>Generate notes, summaries and quizzes.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("📚 Study Assistant", use_container_width=True):
            st.session_state.selected_feature = "📚 Study Assistant"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class="chat-box">
        <h3>✨ Prompt Generator</h3>
        <p>Create professional AI prompts.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("✨ Prompt Generator", use_container_width=True):
            st.session_state.selected_feature = "✨ Prompt Generator"
            st.rerun()

    with col5:
        st.markdown("""
        <div class="chat-box">
        <h3>🎯 Career Guidance</h3>
        <p>Get career roadmaps and guidance.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🎯 Career Guidance", use_container_width=True):
            st.session_state.selected_feature = "🎯 Career Guidance"
            st.rerun()

    with col6:
        st.markdown("""
        <div class="chat-box">
        <h3>🎤 Mock Interview</h3>
        <p>Practice interviews with AI.</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🎤 Mock Interview", use_container_width=True):
            st.session_state.selected_feature = "🎤 Mock Interview"
            st.rerun()

    st.markdown("---")

    st.markdown("""
    <div class="result-box">

    <h2>🎯 About AI Guru</h2>

    <p>
    AI Guru helps students and professionals with:
    </p>

    ✅ Resume Analysis <br><br>
    ✅ Study Notes <br><br>
    ✅ Career Roadmaps <br><br>
    ✅ AI Chat <br><br>
    ✅ Mock Interviews <br><br>
    ✅ Prompt Engineering

    </div>
    """, unsafe_allow_html=True)
# AI CHAT
# =========================
elif st.session_state.selected_feature == "🤖 AI Chat":

    st.header("🤖 AI Chat Assistant")

    # Back Button
    if st.button("⬅️ Back to Dashboard", use_container_width=True, key="chat_back"):
        st.session_state.selected_feature = "🏠 Dashboard"
        st.rerun()

    st.markdown("""
    <div class="result-box">
    <h3>💡 Ask Anything</h3>
    <p>
    Coding • Career • Resume • AI • Study • Projects • Interview Preparation
    </p>
    </div>
    """, unsafe_allow_html=True)

    user_input = st.text_area(
        "✍️ Enter Your Question",
        height=150,
        placeholder="Example: Create a Python project roadmap..."
    )

    col1, col2 = st.columns(2)

    with col1:
        send_btn = st.button(
            "🚀 Generate Answer",
            use_container_width=True
        )

    with col2:
        clear_btn = st.button(
            "🗑️ Clear Chat",
            use_container_width=True
        )

    if clear_btn:
        st.session_state.messages = []
        st.rerun()

    if send_btn:

        if not user_input:
            st.warning("⚠️ Please enter a question first.")

        else:

            with st.spinner("🤖 AI Guru is thinking..."):

                try:

                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "system",
                                "content": """
                                Give clean text answers only.
                                Do not use HTML.
                                Do not use code blocks unless asked.
                                """
                            },
                            {
                                "role": "user",
                                "content": user_input
                            }
                        ]
                    )

                    response = completion.choices[0].message.content

                    st.session_state.messages.append(
                        {
                            "question": user_input,
                            "answer": response
                        }
                    )

                    st.rerun()

                except Exception as e:
                    st.error(f"❌ Error: {e}")
    # =========================
    # CHAT HISTORY
    # =========================

    if len(st.session_state.messages) > 0:

        st.markdown("## 💬 Chat History")

        for chat in reversed(st.session_state.messages):

            st.markdown("### 👤 You")
            st.write(chat["question"])

            st.markdown("### 🤖 AI Guru")
            st.write(chat["answer"])

            st.divider()

    else:

        st.info("💡 Start a conversation with AI Guru.")
    

# =========================
# RESUME ANALYZER
# =========================

elif st.session_state.selected_feature == "📄 Resume Analyzer":

    # Back Button
    if st.button("⬅️ Back to Dashboard", use_container_width=True, key="resume_back"):
        st.session_state.selected_feature = "🏠 Dashboard"
        st.rerun()

    st.header("📄 AI Resume Analyzer")

    st.markdown("""
    <div class="result-box">
        <h3>🚀 Upload Your Resume</h3>
        <p>
        Get ATS Score, Missing Skills, Keywords,
        Career Suggestions and Interview Tips.
        </p>
    </div>
    """, unsafe_allow_html=True)

    file = st.file_uploader(
        "📎 Upload Resume",
        type=["pdf", "docx"]
    )

    if file:

        st.success("✅ Resume Uploaded Successfully")

        resume_text = ""

        if file.type == "application/pdf":

            with pdfplumber.open(file) as pdf:

                for page in pdf.pages:

                    text = page.extract_text()

                    if text:
                        resume_text += text + "\n"

        else:

            doc = Document(file)

            for para in doc.paragraphs:
                resume_text += para.text + "\n"

        with st.expander("📄 Resume Preview"):

            st.text_area(
                "Resume Content",
                resume_text[:5000],
                height=300
            )

        analyze = st.button(
            "🚀 Analyze Resume",
            use_container_width=True
        )

        if analyze:

            with st.spinner("🤖 AI Guru is analyzing your resume..."):

                prompt = f"""
You are an expert ATS Resume Reviewer.

Analyze the following resume professionally.

Give response in this format:

# 📊 ATS Score (Out of 100)

# 💼 Best Job Roles

# 🚀 Strengths

# ❌ Missing Skills

# 🔑 Important ATS Keywords

# 📚 Recommended Certifications

# 🛠 Recommended Projects

# 🎤 Interview Preparation Tips

# 📈 Final Recommendations

Resume:

{resume_text}
"""

                try:

                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    analysis = completion.choices[0].message.content

                    create_pdf(
                        analysis,
                        "resume_report.pdf"
                    )

                    st.markdown("""
                    <div class="result-box">
                        <h2>📊 Resume Analysis Report</h2>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(analysis)

                    with open(
                        "resume_report.pdf",
                        "rb"
                    ) as pdf_file:

                        st.download_button(
                            label="📥 Download Resume Report",
                            data=pdf_file,
                            file_name="resume_report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                except Exception as e:

                    st.error(f"❌ Error: {e}")


# =========================
# STUDY ASSISTANT
# =========================
# =========================
# STUDY ASSISTANT
# =========================
elif st.session_state.selected_feature == "📚 Study Assistant":

    if st.button(
        "⬅️ Back to Dashboard",
        use_container_width=True,
        key="study_back"
    ):
        st.session_state.selected_feature = "🏠 Dashboard"
        st.rerun()

    st.header("📚 AI Study Assistant")

    st.markdown("""
    <div class="result-box">
        <h3>📖 Smart Study Notes Generator</h3>
        <p>
        Generate detailed notes, examples, interview questions,
        quizzes and revision notes instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

    topic = st.text_input(
        "📚 Enter Study Topic",
        placeholder="Example: Python, Machine Learning, DBMS",
        key="study_topic"
    )

    generate_notes = st.button(
        "🚀 Generate Notes",
        use_container_width=True,
        key="study_generate_notes"
    )

    if generate_notes:

        if not topic:

            st.warning("⚠️ Please enter a topic.")

        else:

            with st.spinner("🤖 AI Guru is creating notes..."):

                prompt = f"""
Create professional study notes on:

{topic}

Format:

# 📖 Introduction

# 🎯 Important Concepts

# 🔑 Key Points

# 🌍 Real World Examples

# 💼 Interview Questions

# 📝 Quiz Questions

# ⚡ Quick Revision Notes

# 📚 Summary
"""

                try:

                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    notes = completion.choices[0].message.content

                    create_pdf(
                        notes,
                        "study_notes.pdf"
                    )

                    st.markdown("""
                    <div class="result-box">
                        <h2>📚 Generated Study Notes</h2>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="chat-box">
                        {notes.replace(chr(10), "<br>")}
                    </div>
                    """, unsafe_allow_html=True)

                    with open(
                        "study_notes.pdf",
                        "rb"
                    ) as pdf_file:

                        st.download_button(
                            label="📥 Download Notes PDF",
                            data=pdf_file,
                            file_name="study_notes.pdf",
                            mime="application/pdf",
                            use_container_width=True,
                            key="study_download_pdf"
                        )

                except Exception as e:

                    st.error(f"❌ Error: {e}")
                    
# =========================
# PROMPT GENERATOR
# =========================
# =========================
# PROMPT GENERATOR
# =========================
# =========================
# PROMPT GENERATOR
# =========================

elif st.session_state.selected_feature == "✨ Prompt Generator":

    if st.button(
        "⬅️ Back to Dashboard",
        use_container_width=True,
        key="prompt_back"
    ):
        st.session_state.selected_feature = "🏠 Dashboard"
        st.rerun()

    st.markdown("""
    <h1>✨ AI Prompt Generator</h1>
    <p style='text-align:center;color:#94a3b8;'>
    Create Powerful AI Prompts For ChatGPT, Marketing, Coding & Content Creation
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="result-box">
        <h3>🚀 Professional Prompt Generator</h3>
        <p>
        Generate powerful AI prompts for ChatGPT,
        Content Creation, Coding, Marketing,
        Business, Study and Social Media.
        </p>
    </div>
    """, unsafe_allow_html=True)

    prompt_type = st.selectbox(
        "🎯 Select Prompt Type",
        [
            "ChatGPT Prompt",
            "Coding Prompt",
            "Blog Writing",
            "YouTube Script",
            "Instagram Caption",
            "LinkedIn Post",
            "Marketing Prompt",
            "Business Prompt",
            "Study Prompt",
            "AI Image Prompt"
        ],
        key="prompt_type"
    )

    topic = st.text_input(
        "✍️ Enter Topic",
        placeholder="Example: Python, AI, Fitness, Business",
        key="prompt_topic"
    )

    generate_prompt = st.button(
        "🚀 Generate Prompt",
        use_container_width=True,
        key="generate_prompt_btn"
    )

    if generate_prompt:

        if not topic:

            st.warning("⚠️ Please enter a topic.")

        else:

            with st.spinner("🤖 AI Guru is creating prompt..."):

                prompt = f"""
You are an expert Prompt Engineer.

Create a high-quality {prompt_type}.

Topic:
{topic}

Requirements:

1. Detailed Prompt
2. Professional Structure
3. Clear Instructions
4. Actionable Output
5. Ready To Copy & Use

Generate ONLY the final prompt.
"""

                try:

                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    generated_prompt = (
                        completion.choices[0]
                        .message.content
                    )

                    create_pdf(
                        generated_prompt,
                        "prompt_generator_report.pdf"
                    )

                    st.markdown("""
                    <div class="result-box">
                        <h2>✨ Generated Prompt</h2>
                    </div>
                    """, unsafe_allow_html=True)

                    st.markdown(f"""
                    <div class="chat-box">
                    {generated_prompt.replace(chr(10), "<br>")}
                    </div>
                    """, unsafe_allow_html=True)

                    with open(
                        "prompt_generator_report.pdf",
                        "rb"
                    ) as pdf_file:

                        st.download_button(
                            label="📥 Download Prompt PDF",
                            data=pdf_file,
                            file_name="prompt_generator_report.pdf",
                            mime="application/pdf",
                            use_container_width=True,
                            key="prompt_pdf_download"
                        )

                except Exception as e:

                    st.error(f"❌ Error: {e}")

# =========================
# CAREER GUIDANCE
# =========================
elif st.session_state.selected_feature == "🎯 Career Guidance":

    # Back Button
    if st.button("⬅️ Back to Dashboard", use_container_width=True, key="career_back"):
        st.session_state.selected_feature = "🏠 Dashboard"
        st.rerun()

    st.header("🎯 AI Career Guidance")

    st.markdown("""
    <div class="result-box">
    <h3>🚀 AI Career Roadmap Generator</h3>
    <p>
    Get complete career guidance, learning roadmap,
    certifications, salary insights and interview preparation.
    </p>
    </div>
    """, unsafe_allow_html=True)

    career = st.text_input(
        "🎯 Enter Career Goal",
        placeholder="Example: Data Scientist, AI Engineer, Full Stack Developer"
    )

    generate_roadmap = st.button(
        "🚀 Generate Career Roadmap",
        use_container_width=True
    )

    if generate_roadmap:

        if not career:

            st.warning("⚠️ Please enter a career goal.")

        else:

            with st.spinner("🤖 AI Guru is building your roadmap..."):

                prompt = f"""
Create a professional career roadmap for:

{career}

Format:

# 🎯 Career Overview
# 🛠 Required Skills
# 📚 Learning Roadmap
# 📜 Recommended Certifications
# 💻 Best Projects
# 🏢 Internship Strategy
# 💰 Salary Expectations
# 🎤 Interview Preparation
# 🚀 Future Scope
# 📅 Action Plan (30-60-90 Days)
"""

                try:

                    completion = client.chat.completions.create(
                        model="llama-3.1-8b-instant",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    roadmap = completion.choices[0].message.content

                except Exception as e:

                    st.error(f"❌ Error: {e}")
                    st.stop()

                create_pdf(
                    roadmap,
                    "career_roadmap.pdf"
                )

                st.markdown("""
                <div class="result-box">
                <h2>🎯 Career Roadmap Report</h2>
                </div>
                """, unsafe_allow_html=True)

                st.markdown(f"""
                <div class="chat-box">
                {roadmap.replace(chr(10), '<br>')}
                </div>
                """, unsafe_allow_html=True)

                with open(
                    "career_roadmap.pdf",
                    "rb"
                ) as pdf_file:

                    st.download_button(
                        label="📥 Download Career Roadmap PDF",
                        data=pdf_file,
                        file_name="career_roadmap.pdf",
                        mime="application/pdf",
                        use_container_width=True
                    )


# =========================
# MOCK INTERVIEW
# =========================
elif st.session_state.selected_feature == "🎤 Mock Interview":

    # Back Button
    if st.button("⬅️ Back to Dashboard", use_container_width=True, key="mock_back"):
        st.session_state.selected_feature = "🏠 Dashboard"
        st.rerun()

    st.header("🎤 AI Mock Interview")

    st.markdown("""
    <div class="result-box">
    <h3>🚀 AI Interview Preparation</h3>
    <p>
    Practice technical and HR interviews with AI-generated
    questions, answers, mistakes, and confidence tips.
    </p>
    </div>
    """, unsafe_allow_html=True)

    role = st.selectbox(
        "💼 Select Interview Role",
        [
            "Python Developer",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Data Scientist",
            "AI Engineer",
            "HR Interview"
        ]
    )

    difficulty = st.selectbox(
        "📊 Select Difficulty",
        [
            "Beginner",
            "Intermediate",
            "Advanced"
        ]
    )

    start_interview = st.button(
        "🚀 Start Mock Interview",
        use_container_width=True
    )

    if start_interview:

        with st.spinner("🤖 AI Guru is preparing your interview..."):

            prompt = f"""
Create a professional mock interview.

Role: {role}

Difficulty: {difficulty}

Format:

# 🎤 Interview Questions

# ✅ Sample Answers

# ❌ Common Mistakes

# 👨‍💼 HR Expectations

# 💡 Confidence Tips

# 🚀 Final Interview Advice
"""

            try:

                completion = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                interview = completion.choices[0].message.content

            except Exception as e:

                st.error(f"❌ Error: {e}")
                st.stop()

            create_pdf(
                interview,
                "mock_interview_report.pdf"
            )

            st.markdown("""
            <div class="result-box">
            <h2>🎤 Mock Interview Report</h2>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="chat-box">
            {interview.replace(chr(10), '<br>')}
            </div>
            """, unsafe_allow_html=True)

            with open(
                "mock_interview_report.pdf",
                "rb"
            ) as pdf_file:

                st.download_button(
                    label="📥 Download Interview Report PDF",
                    data=pdf_file,
                    file_name="mock_interview_report.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )

