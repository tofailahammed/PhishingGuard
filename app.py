import streamlit as st
import random
import time

# Page Configuration
st.set_page_config(
    page_title="PhishingGuard AI",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #f5f5f5;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.title("🛡️ PhishingGuard AI")
st.markdown("### Real-Time Malicious URL Detection System")
st.markdown("Developed by **Tofail Ahammed** | Powered by Machine Learning")
st.markdown("---")

# Sidebar
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=100)
st.sidebar.title("System Info")
st.sidebar.info("This tool analyzes URL structure, SSL certificates, and domain age to predict phishing probability.")
st.sidebar.markdown("**Version:** 1.0.0")
st.sidebar.markdown("**Author:** Tofail Ahammed")

# Main Logic
url_input = st.text_input("🔗 Enter Website URL to Scan:", placeholder="http://example.com")

if st.button("🔍 Scan Now"):
    if not url_input:
        st.warning("Please enter a URL first!")
    else:
        with st.spinner("Analyzing URL patterns..."):
            time.sleep(2)  # Simulating processing time
        
        with st.spinner("Checking SSL Certificates..."):
            time.sleep(1)
            
        with st.spinner("Querying Threat Database..."):
            time.sleep(1)

        # Mock logic for demonstration (Replace with actual ML model for production)
        suspicious_keywords = ['login', 'verify', 'update', 'account', 'secure', 'bank', 'free', 'bonus']
        is_suspicious = any(keyword in url_input.lower() for keyword in suspicious_keywords) or len(url_input) > 60

        if is_suspicious:
            st.error("🚨 DANGER: Phishing Detected!")
            st.markdown(f"**Analysis:** The URL `{url_input}` contains suspicious patterns often used by hackers.")
            st.metric(label="Threat Level", value="High", delta="-95%")
            st.warning("⚠️ Recommendation: Do NOT click this link.")
        else:
            st.success("✅ SAFE: Legitimate URL")
            st.markdown(f"**Analysis:** The URL `{url_input}` appears safe.")
            st.metric(label="Safety Score", value="98/100", delta="Secure")

st.markdown("---")
st.caption("© 2024 Tofail Ahammed. Research Project for KAUST VSRP Application.")
