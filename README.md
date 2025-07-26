


# 🤖 Loan Approval Prediction Chatbot (with Together AI Integration)

This project is a **Streamlit-based web application** that predicts whether a loan application will be approved using a machine learning model. It also features a **ChatGPT-style AI assistant**, powered by Together AI, to explain predictions, answer model-related questions, and help users understand the decision-making process.

---

## 🔧 Features

- 🧠 **Loan Prediction**: Fill in applicant info and get an instant approval/rejection prediction.
- 💬 **Chat with AI**: Ask questions like "Why was this application rejected?" or "Which feature is most important?"
- 🌈 **Clean UI**: Chat-style layout mimics ChatGPT for intuitive interaction.
- 🔐 **Hybrid Setup**: Model runs locally; AI queries use the Together.ai API.

---

## 🌐 Live Demo

Try the app live here:  
🔗 [https://csiweek08-lrzuy5sck7vwe8cby7np5y.streamlit.app/](https://csiweek08-lrzuy5sck7vwe8cby7np5y.streamlit.app/)

---

## 📂 Project Structure



loan-approval-chatbot/
- app.py                  # Main Streamlit app
- together\_api.py         # Together AI API helper
-  loan\_approval\_model.joblib  # Trained ML model
- model.txt      # Feature names used during model training
-  requirements.txt        # Required Python packages
-   EADME.md               # Project overview and setup guide



### 1. Clone the Repository

```bash
git clone https://github.com/your-username/loan-approval-chatbot.git
cd loan-approval-chatbot
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Add Your Together AI API Key

Edit `together_api.py` and replace:

```python
headers = {
    "Authorization": "Bearer YOUR_TOGETHER_API_KEY"
}
```

You can get your API key from [Together.ai](https://platform.together.xyz/).

### 4. Run the App

```bash
streamlit run app.py
```

---

## 💬 Sample Questions to Ask the AI

Here are some example questions you can ask the AI assistant:

* Why did the model predict this loan would be rejected?
* Which features are most important in this prediction?
* How does Credit\_History affect the loan approval?
* Can this model be biased?
* What is the accuracy of the model?
* What are the possible values for Self\_Employed?
* What kind of data preprocessing was done?

---

## 📌 Requirements

* Python 3.8 to 3.11
* Internet connection (for AI chat)
* See `requirements.txt` for full dependencies

---

## 💡 Credits

* Built with [Streamlit](https://streamlit.io/), [Scikit-learn](https://scikit-learn.org/), and [Together AI](https://platform.together.xyz/).
* Developed as part of a machine learning + AI assistant demo project.

---

