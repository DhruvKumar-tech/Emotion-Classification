# Emotion Classification
This application is used to predict the emotion from the text

# 🧠 Emotion Classification Web App

A Machine Learning-powered web application that detects **human emotions from text input** using Natural Language Processing (NLP). Built with **Streamlit**, this app provides real-time predictions along with a dynamic **word cloud background visualization**.

---

## 🚀 Live Application

👉 **Try the app here:**
🔗 [https://emotion-classification-zxymqlfgimh4p7jq2uinja.streamlit.app/(https://emotion-classification-zxymqlfgimh4p7jq2uinja.streamlit.app/)

---

## 📌 Features

* 🎯 Predicts **emotion from user input text**
* ⚡ Fast and lightweight ML model
* 📊 Displays **confidence score**
* 🎨 Dynamic **word cloud background** based on input text
* 🧑‍💻 Simple and interactive UI using Streamlit
* ☁️ Deployed on Streamlit Cloud

---

## 🛠️ Tech Stack

* **Frontend/UI:** Streamlit
* **Machine Learning:** Scikit-learn
* **Programming Language:** Python
* **Libraries Used:**

  * NumPy
  * Scikit-learn
  * WordCloud
  * Pillow

---

## 🧠 How It Works

1. User enters text in the input box
2. Text is transformed using **TF-IDF Vectorizer**
3. Pre-trained **Logistic Regression model** predicts probabilities
4. Highest probability emotion is selected
5. Confidence score is displayed
6. A **word cloud background** is generated dynamically

---

## 📂 Project Structure

```
├── app.py                # Main Streamlit application
├── model_lr.pkl         # Trained ML model
├── tfidf.pkl            # TF-IDF vectorizer
├── emotions.pkl         # Emotion labels
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/emotion-classifier.git
cd emotion-classifier
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the app

```bash
streamlit run app.py
```

---

## 📊 Example Inputs

| Input Text                    | Predicted Emotion |
| ----------------------------- | ----------------- |
| "I am very happy today!"      | Joy 😊            |
| "I feel so sad and alone."    | Sadness 😢        |
| "This makes me really angry!" | Anger 😡          |
| "I am scared of the results." | Fear 😨           |

---

## ⚠️ Disclaimer

This application is developed strictly for **academic and demonstration purposes only**.
The predictions may not always be accurate and should not be used for real-world decision-making.

---

## 👨‍💻 Author

**Dhruv Kumar**

If you want, I can also:

* Add **badges (GitHub, Streamlit, Python)**
* Write a **resume project description**
* Optimize it for **portfolio/LinkedIn**

Just tell me 👍
