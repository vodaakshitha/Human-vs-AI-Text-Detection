# Human-vs-AI-Text-Detection
NLP-based web application for detecting AI-generated text using BERT, Random Forest, Flask, and SHAP.
#  AI-Text-Detection

An AI-powered web application that detects whether a given text is **Human-written** or **AI-generated** using advanced **Natural Language Processing (NLP)** and **Transformer-based Deep Learning** models.

---

##  Overview

With the rapid advancement of Large Language Models (LLMs) such as ChatGPT, Gemini, and Claude, distinguishing AI-generated text from human-written content has become increasingly challenging.

This project provides a web-based solution that classifies text as **Human-written** or **AI-generated** using BERT-based models, ensemble learning, and Explainable AI techniques.

---

##  Features

- Detects AI-generated and human-written text
- Fine-tuned BERT sequence classification
- BERT + Random Forest ensemble model
- Real-time text prediction
- Interactive Flask web application
- Dashboard for monitoring predictions
- SHAP-based Explainable AI (XAI)
- Multilingual language detection
- Confidence score visualization

---

##  Tech Stack

- Python
- Flask
- Dash
- Hugging Face Transformers
- BERT
- Random Forest
- Scikit-learn
- SHAP
- Pandas
- NumPy
- Jupyter Notebook

---

##  Project Structure

```
AI-Text-Detection/
│
├── app.py
├── predictor.py
├── dashboard.py
├── notebooks/
├── models/
├── dataset/
├── templates/
├── static/
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Text-Detection.git
```

Navigate to the project

```bash
cd AI-Text-Detection
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```python dashboard.py

---

## 📊 Models Used

- Fine-tuned BERT Sequence Classification
- BERT + Random Forest
- SHAP Explainability

---

## 📈 Results

The developed models achieved high classification performance on the evaluation dataset.

Evaluation Metrics include:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix

---

## 💡 Future Enhancements

- Support additional languages
- Improve robustness against newer LLMs
- Cloud deployment
- REST API integration
- Enhanced dashboard analytics

---

## 👩‍💻 Author

**Voda Akshitha**

M.Tech in Data Science

Interested in Artificial Intelligence, Machine Learning, and Natural Language Processing.

---

## 📜 License

This project is intended for educational and research purposes.
