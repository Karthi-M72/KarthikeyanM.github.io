# 📞 Customer Churn Prediction – Machine Learning Project

**Dataset Credit:** Customer Churn Dataset
**Dataset Size:** \~4,617 rows × 21 columns (mix of categorical & numerical features)

---

## 🎯 Objective

The aim of this project is to build a **Machine Learning model** that predicts the probability of a customer **churning (leaving the company)**.

This helps businesses to:

* Retain at-risk customers before they switch to competitors.
* Reduce revenue loss caused by churn.
* Personalize engagement to improve customer satisfaction & loyalty.

---

## 🔑 Key Insights from the Analysis

* Customers with **more than 3 customer service calls** showed significantly higher churn risk.
* **Shorter tenure** (new customers) were more likely to churn compared to long-term subscribers.
* **Contract type** (month-to-month vs annual) strongly influenced churn — short contracts had higher churn.
* **Payment method** (electronic checks vs credit card/bank transfer) emerged as an important factor.

---

## ✅ Recommended Actions

* **Customer Retention** – Detect at-risk customers early and offer targeted retention strategies.      
* **Revenue Growth** – Minimize revenue leakage by reducing churn and retaining high-value customers.      
* **Enhanced Customer Experience** – Provide proactive support to churn-prone customers.       
* **Business Insights** – Share churn predictions with marketing & support teams for targeted campaigns.             
* **AI-Powered Support** – Use chatbots to intervene in real time when churn signals appear.                 

---

## 🛠️ What I Worked On

* Started with a structured telecom dataset (≈ **4,617 rows × 21 columns**).
* Performed **data preprocessing**:

  * Encoded categorical variables using **One-Hot Encoding**
  * Scaled numerical features with **StandardScaler**
  * Addressed class imbalance with **SMOTE**
  * Train-test split for robust evaluation
* Conducted **Exploratory Data Analysis (EDA)** to identify customer churn drivers.
* Built and compared multiple ML models:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine 
  * XGBoost 
* Evaluated models with **Accuracy, Precision, Recall, and F1-score**.

---

## 📊 Model Performance

**Best Performing Model:** **XGBoost (XGBClassifier)**
* **Accuracy (Test Set):** \~97.54%
  
**Other models for comparison:**

* Random Forest: \~94%
* SVM: \~92%
* Logistic Regression: \~85–88%
* Decision Tree: \~82%

**XGBoost provided the most balanced and reliable performance for predicting churn.**

---

## 🌟 Impact

* Strengthened my skills in **data preprocessing, feature engineering, and ML model building**.
* Demonstrated how **machine learning can transform customer retention strategies** by predicting churn with high accuracy.
* Showcased the importance of **data-driven insights** for designing personalized offers, reducing churn, and increasing customer lifetime value.
