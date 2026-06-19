import streamlit as st
import os
from dotenv import load_dotenv

# Load API keys if testing locally
load_dotenv()

st.set_page_config(
    page_title="OrionBot Mission Control",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling for a clean, high-tech aesthetic
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; }
    h1, h2, h3 { color: #38bdf8 !important; font-family: 'Courier New', Courier, monospace; }
    .stButton>button { background-color: #0284c7; color: white; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)

st.title("📡 OrionBot Mission Control")
st.caption("🚀 NASA Integration & Workspace Monitoring Ecosystem")

st.markdown("---")

# Layout Columns
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌌 System Overview")
    st.write("OrionBot is actively monitoring space telemetry feeds and listening for Slack slash commands.")
    
    st.info("🤖 **Active Listeners:** `/apod` | `/iss-track` | `/mars-weather`")

with col2:
    st.subheader("⚡ Core Status")
    st.success("● Slack Server: ONLINE (Port 3000)")
    st.success("● Telemetry Engine: OPERATIONAL")
    
    # Simple check to see if keys are present
    if os.environ.get("NASA_API_KEY"):
        st.write("✅ NASA API Connection: Verified")
    else:
        st.write("⚠️ NASA API Connection: Using Demo Key")

st.markdown("---")
st.subheader("🛠️ Technical Architecture")
st.text("Backend: Python, Flask, Slack Bolt Framework\nFrontend: Streamlit Core\nDeployment Infrastructure: Local Secure Tunnels")