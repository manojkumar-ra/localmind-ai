import streamlit as st
import requests

st.set_page_config(
    page_title="LocalMind AI",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=Syne:wght@400;700;800&display=swap');
    
    * { font-family: 'Space Grotesk', sans-serif; }
    
    .stApp {
        background: linear-gradient(145deg, #0a0a0a 0%, #111111 40%, #0f0a00 100%);
    }
    
    .header {
        text-align: center;
        padding: 50px 20px;
        background: linear-gradient(135deg, #0f0f0f, #1a1000);
        border-radius: 20px;
        border: 1px solid rgba(255,100,0,0.3);
        margin-bottom: 30px;
        position: relative;
        overflow: hidden;
    }
    
    .header::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, transparent, #ff6400, #ff9500, #ff6400, transparent);
    }
    
    .header::after {
        content: '';
        position: absolute;
        bottom: 0; left: 0; right: 0;
        height: 3px;
        background: linear-gradient(90deg, transparent, #ff6400, #ff9500, #ff6400, transparent);
    }
    
    .header h1 {
        font-family: 'Syne', sans-serif;
        color: #ffffff;
        font-size: 4em;
        font-weight: 800;
        letter-spacing: -2px;
        margin: 0;
    }
    
    .header h1 span {
        color: #ff6400;
        text-shadow: 0 0 30px rgba(255,100,0,0.5);
    }
    
    .header p {
        color: #cccccc;
        font-size: 1.1em;
        font-weight: 300;
        margin-top: 10px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .badge {
        display: inline-block;
        background: rgba(255,100,0,0.15);
        border: 1px solid rgba(255,100,0,0.4);
        color: #ff6400;
        padding: 5px 15px;
        border-radius: 50px;
        font-size: 0.8em;
        margin-top: 15px;
        letter-spacing: 2px;
        text-transform: uppercase;
    }
    
    .stChatMessage {
        background: rgba(255,255,255,0.02) !important;
        border: 1px solid rgba(255,255,255,0.06);
        border-left: 3px solid #ff6400;
        border-radius: 10px;
        padding: 5px;
        margin: 8px 0;
    }
    
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0a0a0a, #0f0800);
        border-right: 1px solid rgba(255,100,0,0.2);
    }
    
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    .sidebar-logo {
        text-align: center;
        padding: 25px 0;
        font-family: 'Syne', sans-serif;
        font-size: 1.8em;
        font-weight: 800;
        color: #ffffff !important;
        letter-spacing: -1px;
        border-bottom: 1px solid rgba(255,100,0,0.2);
        margin-bottom: 20px;
    }
    
    .sidebar-logo span { color: #ff6400 !important; }
    
    .stat-card {
        background: rgba(255,100,0,0.05);
        border: 1px solid rgba(255,100,0,0.15);
        border-radius: 10px;
        padding: 12px 15px;
        margin: 8px 0;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .stat-label {
        color: #ffffff !important;
        font-size: 0.85em;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    .stat-value {
        color: #ff6400 !important;
        font-weight: 700;
        font-size: 0.9em;
    }
    
    .feature-item {
        display: flex;
        align-items: center;
        padding: 10px 0;
        color: #ffffff !important;
        font-size: 0.9em;
        border-bottom: 1px solid rgba(255,255,255,0.04);
        letter-spacing: 0.5px;
    }
    
    .feature-dot {
        width: 6px;
        height: 6px;
        background: #ff6400;
        border-radius: 50%;
        margin-right: 10px;
        display: inline-block;
    }
    
    .stButton button {
        background: linear-gradient(135deg, #ff6400, #ff9500) !important;
        color: #000000 !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        padding: 12px !important;
        width: 100% !important;
        text-transform: uppercase !important;
    }
    
    .stChatInput input {
        background: rgba(255,255,255,0.03) !important;
        border: 1px solid rgba(255,100,0,0.2) !important;
        border-radius: 12px !important;
        color: #ffffff !important;
    }
    
    .section-title {
        color: #ff6400 !important;
        font-size: 0.75em !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-weight: 700 !important;
        margin: 20px 0 10px 0 !important;
    }
    
    .stSelectbox > div > div {
        background-color: #1a1000 !important;
        border: 1px solid rgba(255,100,0,0.3) !important;
        border-radius: 10px !important;
        color: #ffffff !important;
    }
    
    .stSelectbox > div > div > div {
        color: #ffffff !important;
    }
    
    .stSelectbox svg { fill: #ff6400 !important; }
    
    div[data-baseweb="popover"] {
        background-color: #1a1000 !important;
    }
    div[data-baseweb="menu"] {
        background-color: #1a1000 !important;
    }
    li[role="option"] {
        background-color: #1a1000 !important;
        color: #ffffff !important;
    }
    li[role="option"]:hover {
        background-color: #ff6400 !important;
        color: #000000 !important;
    }
    
    .stChatMessage p { color: #ffffff !important; }
    p, label, div { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="header">
        <h1>Local<span>Mind</span></h1>
        <p>Private AI Intelligence — 100% On Your Machine</p>
        <div class="badge">Offline • Secure • Free</div>
    </div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-logo">🧠 Local<span>Mind</span></div>', unsafe_allow_html=True)
    st.markdown('<p class="section-title">Model Config</p>', unsafe_allow_html=True)
    model = st.selectbox("AI Model", ["llama3.2", "mistral"])
    creativity = st.selectbox("Creativity Level", ["Low (0.3)", "Medium (0.7)", "High (1.0)"])
    temperature = 0.3 if "Low" in creativity else 1.0 if "High" in creativity else 0.7
    st.markdown('<p class="section-title">System Stats</p>', unsafe_allow_html=True)
    messages_count = len(st.session_state.get('messages', []))
    st.markdown(f"""
        <div class="stat-card">
            <span class="stat-label">Status</span>
            <span class="stat-value">Online</span>
        </div>
        <div class="stat-card">
            <span class="stat-label">Network</span>
            <span class="stat-value">Offline</span>
        </div>
        <div class="stat-card">
            <span class="stat-label">Messages</span>
            <span class="stat-value">{messages_count}</span>
        </div>
        <div class="stat-card">
            <span class="stat-label">Privacy</span>
            <span class="stat-value">Maximum</span>
        </div>
    """, unsafe_allow_html=True)
    st.markdown('<p class="section-title">Features</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-item"><span class="feature-dot"></span>No internet required</div>
        <div class="feature-item"><span class="feature-dot"></span>No API key needed</div>
        <div class="feature-item"><span class="feature-dot"></span>Data never leaves device</div>
        <div class="feature-item"><span class="feature-dot"></span>Powered by Ollama</div>
        <div class="feature-item"><span class="feature-dot"></span>Free forever</div>
    """, unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

prompt = st.chat_input("Ask LocalMind anything...")

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("LocalMind is thinking..."):
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={"model": model, "prompt": prompt, "stream": False,
                      "options": {"temperature": temperature}}
            )
            answer = response.json()["response"]
            st.write(answer)
            st.session_state.messages.append({"role": "assistant", "content": answer})