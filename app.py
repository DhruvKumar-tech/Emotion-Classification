import streamlit as st
import pickle
import numpy as np
from wordcloud import WordCloud
import base64

# -------------------- Page Config (MUST BE FIRST) --------------------
st.set_page_config(page_title="Emotion Classifier", layout="centered")

# -------------------- Load Model Files --------------------
@st.cache_resource
def load_files():
    model = pickle.load(open("model_lr.pkl", "rb"))
    tfidf = pickle.load(open("tfidf.pkl", "rb"))
    emotions = pickle.load(open("emotions.pkl", "rb"))
    return model, tfidf, emotions

model, tfidf, emotions = load_files()

# -------------------- Function: Generate Background WordCloud --------------------
def set_wordcloud_bg(text):

    wc = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    wc.to_file("bg.png")

    with open("bg.png", "rb") as f:
        data = f.read()

    encoded = base64.b64encode(data).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            opacity: 0.95;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -------------------- Title --------------------
st.title("🧠 Emotion Classification App")
st.markdown("Detect emotions from text using Machine Learning")

# -------------------- Prediction Function (SINGLE OUTPUT) --------------------
def predict_emotion(text):
    vec = tfidf.transform([text])
    probs = model.predict_proba(vec)[0]

    top_idx = np.argmax(probs)

    emotion = emotions[top_idx]
    confidence = probs[top_idx] * 100

    return emotion, confidence

# -------------------- User Input --------------------
user_input = st.text_area("✍️ Enter your text here:")

# -------------------- Prediction --------------------
if st.button("🔍 Predict Emotion"):

    if user_input.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        emotion, confidence = predict_emotion(user_input)

        # ✅ Set background word cloud
        set_wordcloud_bg(user_input)

        st.subheader("🎯 Predicted Emotion")
        st.success(f"{emotion} ({confidence:.2f}%)")

        st.progress(int(confidence))

# -------------------- Footer --------------------
st.markdown("---")
st.markdown(
    "<p style='font-size:12px; color:gray;'>"
    "⚠️ Disclaimer: This application is developed strictly for academic and demonstration purposes only. "
    "The predictions may not always be accurate and should not be used for real-world decision-making."
    "</p>",
    unsafe_allow_html=True
)