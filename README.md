# 📰 Fake News Detector - Machine Learning NLP Project

A powerful **Fake News Detector** that uses machine learning and natural language processing to identify whether a news article is **REAL** or **FAKE**.

✅ Trained on the **WELFake dataset**  
✅ Achieved **96% accuracy** using **TF-IDF + PassiveAggressiveClassifier**  
✅ Deployed as a **Streamlit Web App** for real-time detection

---

## 🌐 Live Demo

🚀 **Streamlit App**: [https://rukum_maurya.streamlit.app](https://rukum-maurya-fake-news-detector-app-jjtb2e.streamlit.app/)  
🔗 **GitHub Repo**: [https://github.com/Rukum-Maurya/fake-news-detector](https://github.com/Rukum-Maurya/fake-news-detector)

---

## 📌 Project Highlights

- 🧠 Built using **PassiveAggressiveClassifier**
- 📊 Feature extraction with **TF-IDF Vectorizer**
- 📁 Real-world dataset: **WELFake (news + social media content)**
- 🚀 Interactive front-end with **Streamlit**
- 💾 Model and vectorizer saved using **Joblib**

---

## 🗂️ Folder Structure

```
fake-news-detector/
├── data/                     # WELFake_Dataset.csv
├── model/                    # Saved model + vectorizer
├── notebooks/                # EDA, training
│   └── fake_news_detector.ipynb
├── app.py                    # Streamlit application
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## 📈 Model Performance

| Metric     | Value   |
|------------|---------|
| Accuracy   | 96%     |
| Precision  | 96%     |
| Recall     | 97%     |
| F1-score   | 96%     |

### 🔢 Confusion Matrix

|                 | Predicted Real | Predicted Fake |
|-----------------|----------------|----------------|
| **Actual Real** | 6701           | 309            |
| **Actual Fake** | 248            | 7161           |

---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Rukum-Maurya/fake-news-detector.git
cd fake-news-detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

Then visit: [http://localhost:8501](http://localhost:8501)

---

## 🔍 Sample Predictions

| News Article Snippet                                                                                      | Prediction |
|------------------------------------------------------------------------------------------------------------|------------|
| "Obama’s attorney general says more gun control is needed after shooting in Orlando."                     | ✅ Real     |
| "BREAKING: Clinton caught on secret mic admitting fake polls during campaign!"                            | ❌ Fake     |
| "CDC releases updated COVID-19 travel guidelines for vaccinated travelers."                               | ✅ Real     |
| "Newly found alien signals confirm Area 51 conspiracy, says top Pentagon insider."                        | ❌ Fake     |

---

## ⚙️ Tech Stack

- Python
- Pandas, Scikit-learn
- TF-IDF (NLP)
- PassiveAggressiveClassifier
- Streamlit
- Joblib
- GitHub

---

## 👨‍💻 About Me

**Rukum Maurya**  
🎓 Student @ Amrita Vishwa Vidyapeetham  
🔗 [LinkedIn](https://www.linkedin.com/in/rukum-maurya) • [GitHub](https://github.com/Rukum-Maurya)

---

## 🤝 Let’s Connect!

I'm building a full machine learning portfolio with real-world, deployable apps.  
Feel free to collaborate, give feedback, or connect with me on projects and internships.


