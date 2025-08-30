# ❤️ Heart Disease Prediction – A Data-Driven Approach Using Machine Learning

**Dataset Credit:** Heart Disease dataset 

---

## 🎯 Objective

To predict whether a patient is likely to have **heart disease** based on clinical and demographic features.
This project leverages **Machine Learning** techniques to identify key medical risk factors and improve early detection for better treatment outcomes.

---

## 🔑 Key Insights from the Analysis

* Patients with **higher cholesterol and resting blood pressure** showed greater chances of heart disease.
* **Chest pain type (cp)** and **exercise-induced angina (exang)** strongly influenced predictions.
* **Age** and **thalassemia (thal)** also emerged as significant medical indicators.

---

## ✅ Recommended Actions

* Encourage **preventive screening** for patients with abnormal cholesterol, blood pressure, or chest pain symptoms.
* Use **predictive risk scores** to assist doctors in recommending further tests (ECG, treadmill test, etc.).
* Develop **personalized care programs** targeting older patients and those with exercise-related angina.

---

## 🛠️ What I Worked On

* Started with a structured **clinical dataset** (≈ 180 rows × 15 columns).
* Performed **data preprocessing**:

  * Normalized numerical features with **MinMaxScaler**
  * Handled **class imbalance** using **SMOTE**
  * Train-test split for robust evaluation
* Conducted **exploratory data analysis (EDA)** to identify medical risk factors
* Built and compared multiple ML models:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine (SVM)
  * Bagging
  * XGBoost (with hyperparameter tuning via RandomizedSearchCV)
* Evaluated models with **Accuracy, Precision, Recall, and F1-score**

---

## 📊 Model Performance

* **Best Performing Model:** **Support Vector Machine (SVM)**
* **Accuracy (Test Set):** \~88.89%

Other models for comparison:

* Random Forest: \~86.67%
* Logistic Regression, KNN: \~84.44%
* Bagging: \~80%
* Decision Tree: \~77.78%
* XGBoost: \~80–84.44%

SVM provided the most balanced and reliable performance.

---

## 🌟 Impact

* Strengthened my skills in **data preprocessing, model building, and evaluation**.
* Demonstrated how **machine learning can be applied in healthcare** for early risk detection.
* Showcased the importance of **data-driven insights** to support **preventive care and timely diagnosis** for heart-related conditions.
