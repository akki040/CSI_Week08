import streamlit as st
import pandas as pd
import joblib
from together_api import ask_together_ai  # Make sure this file is in the same folder

# Load the trained ML model
model = joblib.load("loan_approval_model.joblib")

# Load feature names
with open("model_features.txt", "r") as f:
    feature_names = f.read().splitlines()

# System message to guide Together AI
system_context = (
    "You are an expert Machine Learning assistant. You help explain, debug, and answer questions "
    "related to a machine learning model used for loan approval prediction. Use clear, concise language. "
    "If user asks about model behavior, predictions, or performance, explain in a helpful way."
)

# Streamlit Page Config
st.set_page_config(page_title="Loan Approval Chat Assistant", layout="wide")
st.markdown("<h1 style='text-align: center;'>🤖 Loan Approval Prediction Chatbot</h1>", unsafe_allow_html=True)

# ========== Sidebar: User Input ==========
st.sidebar.header("📊 Enter Applicant Data")

input_data = {}
for feature in feature_names:
    input_data[feature] = st.sidebar.text_input(f"{feature}:")

if st.sidebar.button("Predict Loan Approval"):
    if all(value.strip() != "" for value in input_data.values()):
        try:
            input_df = pd.DataFrame([input_data])
            prediction = model.predict(input_df)[0]
            st.sidebar.success(f"✅ Prediction: {prediction}")
        except Exception as e:
            st.sidebar.error(f"❌ Prediction Error: {e}")
    else:
        st.sidebar.warning("⚠️ Please fill in all input fields.")

# ========== Chat Interface ==========
st.markdown("---")
st.markdown("### 💬 Ask questions about the model:")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="user_input")

if st.button("Send"):
    if user_input.strip():
        # Append user's question
        st.session_state.chat_history.append(("user", user_input))
        with st.spinner("Thinking..."):
            try:
                ai_response = ask_together_ai(system_context, user_input)
            except Exception as e:
                ai_response = f"❌ Error: {e}"
            st.session_state.chat_history.append(("ai", ai_response))

# ========== Display Chat History ==========
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(
            f"""
            <div style='text-align: right; background-color:#dcf8c6; color:black; padding:10px;
                        border-radius:12px; margin:6px 0;'>
                <b>You:</b> {message}
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <div style='text-align: left; background-color:#f1f0f0; color:black; padding:10px;
                        border-radius:12px; margin:6px 0;'>
                <b>AI:</b> {message}
            </div>
            """, unsafe_allow_html=True)
