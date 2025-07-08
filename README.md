
#  Teen Mental Health & Stress Prediction

This project uses machine learning to predict whether a teen is in a **Low**, **Medium**, or **High** stress state based on their daily behaviors, like screen time, sleep, social media use, and physical activity.


> A Streamlit-powered machine learning app that predicts whether a teen is in a **Low**, **Medium**, or **High** stress state based on their lifestyle behaviors like screen time, sleep, exercise, and social media use

## 🔗 Live Demo
 https://teen-mental-health-analysis-cqvhhvnzbcxydfetbjfw3b.streamlit.app/    

 
![image](https://github.com/user-attachments/assets/bd5253fe-6d6b-4f3d-8124-4e8642ac1a2c)



##  Extended Project Description

Adolescent mental health is a growing concern worldwide. Rising stress levels are frequently linked to digital overexposure, poor sleep, and sedentary lifestyles. But without data, it's hard to take informed action.

This project aims to bridge that gap. 

By analyzing behavioral data from 5,000 teens, including screen time, exercise, sleep, and social habits, we trained a machine learning model to classify their **stress levels** (Low, Medium, High) based on **wearable stress scores**.

The goal is to offer:
- A behavioral lens on mental health
- A simple but effective way to **flag at-risk teens**
- A conversation starter for schools, parents, and policymakers

---

##  Objective

Build a model that uses behavioral data to predict teen stress levels, enabling early intervention and promoting digital wellness and mental health awareness.

---

##  Tech Stack

- **Python**: pandas, scikit-learn, seaborn, matplotlib
- **Google Colab**: development environment
-  **Streamlit:** Web app deployment
- **GitHub**: version control and documentation
- **Machine Learning**: Random Forest Classifier (classification model)

---

##  Dataset Overview

| Column Name            | Description                                   |
|------------------------|-----------------------------------------------|
| `age`                  | Teen participant’s age                        |
| `screen_time_hours`    | Total screen time per day                     |
| `sleep_hours`          | Average sleep hours per night                 |
| `exercise_hours`       | Daily physical activity in hours              |
| `social_media_hours`   | Time spent on social media                    |
| `survey_stress_score`  | Self-reported stress score                    |
| `wearable_stress_score`| Device-based physiological stress level       |

> The final target column, `stress_category`, was created by binning `wearable_stress_score` into `Low`, `Medium`, and `High` categories using quantiles.

---

##  Methodology

1. **Data Cleaning & EDA**
   - Checked for nulls, outliers, and imbalance
   - Explored trends in behavior and stress

2. **Feature Engineering**
   - Created `stress_category` from continuous wearable scores
   - Dropped non-numeric columns for modeling

3. **Modeling**
   - Trained a **Random Forest Classifier**
   - Evaluated using a confusion matrix & classification report

---

## 📊 Model Results

### ✅ Confusion Matrix


![download](https://github.com/user-attachments/assets/421c38db-0e81-447d-a9ef-a90fa471341b)


- The model was able to learn and predict all 3 stress categories.
- Most confusion occurred between **High** and **Medium** classes — a common trend given overlapping behaviors.

### 📋 Classification Report (Excerpt)

| Class   | Precision | Recall | F1-score |
|---------|-----------|--------|----------|
| High    | 0.33      | 0.39   | 0.36     |
| Medium  | 0.33      | 0.32   | 0.32     |
| Low     | 0.31      | 0.25   | 0.28     |

---

## 📈 Feature Importance

![download](https://github.com/user-attachments/assets/b4d60943-55f8-42e7-904c-c577e117eda6)


The most influential predictors were:
- **Screen time hours**
- **Sleep hours**
- **Exercise hours**
- **Social media use**

---

## 💡 Key Insights

- **Behavioral data alone** can be a strong indicator of physiological stress.
- **Screen time and lack of sleep** are top stress contributors.
- Teens with higher physical activity and more sleep had consistently lower stress predictions.

---

##  Real-World Applications

This project can inform:
- **School counselors**: Early flagging of at-risk students
- **Parents**: Encouraging better digital balance
- **Policymakers**: Grounding wellness programs in real data

---

## 📁 Repo Structure



teen-mental-health-analysis/

├── app.py # Streamlit app

├── data/ # (Dataset - not uploaded to GitHub)

├── notebooks/ # Colab notebooks (EDA + Modeling)

├── visuals/ # Plots and images (confusion matrix, etc.)

├── README.md # Project documentation

└── requirements.txt # Python dependencies (optional)

##  Impact

This model can be used as part of a digital wellness or school intervention system to identify high-stress teens early and recommend behavioral changes.

---

## 👩🏾‍💻 Author

**Charity Murugi Nguru**  
Data Scientist | Tech Communicator | Mental Health Advocate | Statistician  
📫 charitymurugi55@gmail.com  
📍 Kenya

---

## ⭐️ Let's Connect!

If you're an educator, researcher, or wellness advocate looking to collaborate, feel free to reach out. Let’s use data to support mental health together. 🌿
