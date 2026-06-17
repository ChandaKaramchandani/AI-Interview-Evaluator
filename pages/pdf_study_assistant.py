import streamlit as st
from groq import Groq
from dotenv import load_dotenv
import pdfplumber
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
    page_title="PDF Study Assistant",
    page_icon="📄",
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

/* Upload Box */

[data-testid="stFileUploader"]{
    background:#1e293b;
    padding:15px;
    border-radius:15px;
}

/* Text Area */

.stTextArea textarea{
    background:#1e293b !important;
    color:white !important;
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

/* Result Card */

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
    📄 PDF Study Assistant
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("📚 Smart Notes")
    st.info("📝 PDF Summary")
    st.warning("🎯 Interview Questions")

    st.markdown("---")

    st.markdown("""
    ### 🚀 Features

    ✅ PDF Summary

    ✅ Important Topics

    ✅ Key Points

    ✅ Revision Notes

    ✅ MCQ Quiz

    ✅ Interview Questions
    """)

# =========================
# HEADER
# =========================

st.title("📄 PDF Study Assistant")

st.markdown("""
<p style="
text-align:center;
color:white;
font-size:22px;
margin-bottom:20px;
">
Upload PDF & Generate Smart Notes 🚀
</p>
""", unsafe_allow_html=True)

# =========================
# FILE UPLOAD
# =========================

uploaded_file = st.file_uploader(
    "📎 Upload PDF File",
    type=["pdf"]
)

# =========================
# PDF PROCESSING
# =========================

if uploaded_file:

    pdf_text = ""

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            text = page.extract_text()

            if text:
                pdf_text += text

    st.success("✅ PDF Uploaded Successfully")

    st.text_area(
        "📄 PDF Preview",
        pdf_text[:3000],
        height=250
    )

    # =========================
    # GENERATE STUDY MATERIAL
    # =========================

    if st.button(
        "🚀 Generate Study Material",
        use_container_width=True
    ):

        with st.spinner(
            "🤖 AI is analyzing PDF..."
        ):

            prompt = f"""

Analyze this PDF content.

Generate:

# Summary

# Important Topics

# Key Points

# Revision Notes

# 5 MCQ Quiz Questions

# Important Interview Questions

PDF Content:

{pdf_text[:10000]}

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
                "✅ Study Material Generated Successfully"
            )

            st.markdown(
                f"""
                <div class="result-box">
                    <h2>📚 Generated Study Material</h2>
                    <hr>
                    {result.replace(chr(10), '<br>')}
                </div>
                """,
                unsafe_allow_html=True
            )