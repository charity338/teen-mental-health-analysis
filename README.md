
#  Teen Mental Health & Stress Prediction

This project uses machine learning to predict whether a teen is in a **Low**, **Medium**, or **High** stress state based on their daily behaviors — like screen time, sleep, social media, and exercise.

---

##  Objective

To build a data-driven model that can support early mental health interventions for adolescents using behavioral data and physiological stress indicators.

---

##  Tools Used

- Python (Pandas, Sklearn, Matplotlib)
- Google Colab for model development
- GitHub for version control
- Random Forest Classifier for stress prediction

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

We created a new target column: `stress_category` (Low / Medium / High) based on wearable stress quantiles.

---

##  Key Results

- **Model Type:** Random Forest Classifier  
- **Target:** `stress_category` (multiclass: Low / Medium / High)
- **Performance:** Model successfully learned all three classes

### Confusion Matrix

![Confusion Matrix](visuals/confusion_matrix.png)

> The model most often confused **Medium** and **High** stress classes — a common pattern with behavioral overlap — but still achieved good predictive balance.

---

##  Impact

This model can be used as part of a digital wellness or school intervention system to identify high-stress teens early and recommend behavioral changes.

---

## 👩🏾‍💻 Author

**Charity Murugi Nguru**  
Data Scientist | Tech Communicator | Mental Health Advocate  
📫 charitymurugi55@gmail.com  
📍 Kenya

---

## ⭐️ Let's Connect!

If you're a school, wellness org, or researcher interested in using behavioral AI for good, get in touch!
