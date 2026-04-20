# 📱 Smartphone Addiction Prediction (ML Project)

An end-to-end Machine Learning project that predicts whether a user is likely addicted to smartphone usage based on behavioral patterns such as screen time, social media usage, sleep habits, and notification activity.

---

# 🌐 Live Demo

👉 [https://smart-phone-addiction-analysis-prediction.streamlit.app/](https://smart-phone-addiction-analysis-prediction.streamlit.app/)

---

# 🎯 Problem Statement

Smartphone addiction can negatively impact productivity, mental health, and sleep quality.

Goal of this project:

> Build a machine learning model to predict smartphone addiction using user behavior data.

---

# 🧠 ML Workflow

1. Data Cleaning
2. Feature Engineering
3. Train-Test Split
4. Preprocessing using ColumnTransformer
5. Model Training (Multiple Algorithms)
6. Model Evaluation (Accuracy, Precision, Recall, F1-score)
7. Hyperparameter Tuning
8. Deployment using Streamlit

---

# 📊 Features Used

### Behavioral Features

* daily screen time
* social media usage
* gaming hours
* work/study hours
* sleep duration
* notifications per day
* app opens per day
* weekend usage

### Engineered Features

* entertainment usage ratio
* weekend usage difference
* notification engagement
* sleep deficit indicator

### Categorical Features

* gender
* stress level
* academic/work impact

---

# 🤖 Models Trained

* Logistic Regression
* Decision Tree
* Random Forest ⭐ (Best Model)
* KNN
* SVM

Final model selected based on **F1-score** due to class imbalance.

---

# 📈 Model Performance (Random Forest)

* Accuracy: ~94%
* Precision: ~96%
* Recall: ~95%
* F1 Score: ~0.956

---

# 🛠 Tech Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

# 🚀 Run Locally

```bash
git clone https://github.com/siddagovardhanreddy33/Ml_project--Smart_Phone_Addiction_Analysis.git

cd Ml_project--Smart_Phone_Addiction_Analysis

pip install -r requirements.txt

streamlit run app.py
```

---

# 📂 Project Structure

```
app.py                      # Streamlit app
smartphone_addiction_model.pkl
preprocessor.pkl
requirements.txt

notebooks (EDA + ML workflow)
```

---

# 👤 Author

Govardhan Reddy Sidda
