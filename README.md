# 🎬 RecoBot – Movie Recommender System

RecoBot is an AI-powered movie recommender system built using **Python**, **Streamlit**, and **Natural Language Processing** (NLP). It helps users discover movies similar to their favorites by analyzing genres and descriptions using **TF-IDF vectorization** and **cosine similarity**.

![RecoBot Cover](https://via.placeholder.com/1000x400?text=RecoBot+-+Your+Movie+Recommendation+Buddy)

---

## 🚀 Demo

📌 **Live App**: Coming soon  
📂 **GitHub Repo**: [RecoBot](https://github.com/khyati9304/RecoBot)

---

## 🧠 Features

- 🔎 **Search by movie name**
- 🤖 **Recommends top similar movies**
- 🧾 **Based on genres + plot summaries**
- 🧠 Uses **TF-IDF + Cosine Similarity**
- ⚡ Fast, simple UI using **Streamlit**

---

## 🛠️ Tech Stack

| Tool          | Use                          |
|---------------|-------------------------------|
| 🐍 Python      | Core programming language     |
| 🧠 Scikit-learn | TF-IDF & Similarity Modeling |
| 🧾 Pandas      | Data handling                 |
| 🎨 Streamlit   | Web-based UI framework        |

---

## 🧪 How it Works

1. **Preprocess dataset** (`movies.csv`)
2. **Generate TF-IDF matrix** from movie overviews
3. **Compute cosine similarity matrix**
4. Store this in `similarity.pkl` for fast access
5. App loads model and shows recommendations based on user selection

---
