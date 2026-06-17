
import streamlit as st
from groq import Groq
from dotenv import load_dotenv
from streamlit_mic_recorder import mic_recorder
from gtts import gTTS
import tempfile
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
    page_title="AI Voice Assistant",
    page_icon="🎙️",
    layout="wide"
)

# =========================
# CSS
# =========================

st.markdown("""
<style>

/* Main Background */

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

/* Selectbox */

.stSelectbox div[data-baseweb="select"]{
    background:#1e293b !important;
    color:white !important;
    border-radius:12px !important;
}

/* Headings */

h1,h2,h3{
    color:white !important;
}

/* Text */

p{
    color:white !important;
}

/* Alert Box */

.stAlert{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.markdown("""
    <h2 style='text-align:center;color:white;'>
    🎙️ AI Voice Assistant
    </h2>
    """, unsafe_allow_html=True)

    st.markdown("---")

    st.success("🎤 Voice Input")
    st.info("🤖 AI Processing")
    st.warning("🔊 Voice Response")

    st.markdown("---")

    st.markdown("""
    ### 🚀 Features

    ✅ Speech To Text

    ✅ AI Conversation

    ✅ Text To Speech

    ✅ English & Hindi

    ✅ Conversation History

    ✅ Download Conversation

    """)

# =========================
# PAGE TITLE
# =========================

st.title("🎙️ Real AI Voice Assistant")
st.subheader("Speak → AI Understands → AI Responds 🔥")

# =========================
# LANGUAGE SELECTOR
# =========================

language = st.selectbox(
    "🌍 Select Language",
    ["English", "Hindi"]
)

# =========================
# VOICE RECORDER
# =========================

audio = mic_recorder(
    start_prompt="🎤 Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="voice"
)

if audio:

    st.audio(audio["bytes"])

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as f:

            f.write(audio["bytes"])
            audio_path = f.name

        # =========================
        # SPEECH TO TEXT
        # =========================

        with open(audio_path, "rb") as file:

            transcription = client.audio.transcriptions.create(
                file=file,
                model="whisper-large-v3"
            )

        text = transcription.text

        st.success("📝 You Said:")
        st.write(text)

        # =========================
        # AI RESPONSE
        # =========================

        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a helpful AI Voice Assistant.
                    Answer clearly and professionally.
                    """
                },
                {
                    "role": "user",
                    "content": text
                }
            ]
        )

        answer = completion.choices[0].message.content

        st.success("🤖 AI Response:")
        st.write(answer)

        # =========================
        # SAVE CHAT HISTORY
        # =========================

        st.session_state.history.append(
            {
                "question": text,
                "answer": answer
            }
        )

        # =========================
        # AI VOICE OUTPUT
        # =========================

        lang_code = "en"

        if language == "Hindi":
            lang_code = "hi"

        tts = gTTS(
            text=answer,
            lang=lang_code
        )

        audio_response = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        )

        tts.save(audio_response.name)

        st.success("🔊 AI Voice Response")

        st.audio(audio_response.name)

    except Exception as e:

        st.error(f"Error: {e}")

# =========================
# CHAT HISTORY
# =========================

if st.session_state.history:

    st.divider()

    st.subheader("📜 Conversation History")

    chat_text = ""

    for chat in reversed(st.session_state.history):

        st.markdown(f"""
        **🎤 You:** {chat['question']}

        **🤖 AI:** {chat['answer']}
        """)

        chat_text += f"You: {chat['question']}\n"
        chat_text += f"AI: {chat['answer']}\n\n"

    st.download_button(
        label="📥 Download Conversation",
        data=chat_text,
        file_name="voice_chat.txt",
        mime="text/plain"
    )
