# 📱 Cell Phone Price Prediction – A Machine Learning Approach

**Dataset Credit:** Cell Phone Price Prediction Dataset

---

## 🎯 Objective

To predict the price range of cell phones based on their technical specifications.
This project applies **Machine Learning models** to help manufacturers, retailers, and consumers make data-driven decisions on pricing strategies and product positioning.

---

## 🔑 Key Insights from the Analysis

* Features like **RAM**, **battery power**, and **pixel resolution** were the most influential in predicting price ranges.
* Devices with **higher RAM and battery capacity** consistently mapped to premium categories.
* **Talk time** and **camera resolution** also contributed but had less predictive power compared to RAM.

---

## ✅ Recommended Actions

* **Manufacturers**: Focus on optimizing **RAM and battery life** for budget-friendly models to increase competitiveness.
* **Retailers**: Use predictive insights to classify products more accurately and suggest alternatives to customers.
* **Consumers**: Compare devices with similar RAM and battery power when evaluating price vs. performance.

---

## 🛠️ What I Worked On

* Started with a **structured dataset** (≈ 2,000 rows × 21 features).
* Performed **data preprocessing**:

  * Normalized numerical features.
  * Train-test split for robust evaluation.
* Conducted **exploratory data analysis (EDA)** to identify the most impactful specifications.
* Built and compared multiple ML models:

  * Logistic Regression
  * Decision Tree
  * Random Forest
  * Support Vector Machine (SVM)
  * XGBoost
  * Gradient Boosting
* Evaluated models using **Accuracy** on the test set.

---

## 📊 Model Performance

**Best Performing Model:** Support Vector Machine (SVM)
**Accuracy (Test Set):** \~81%

Other models for comparison:

* Logistic Regression: \~66.75%
* Decision Tree: \~100% (likely overfitting)
* Random Forest: \~100% (likely overfitting)
* XGBoost: \~100% (likely overfitting)
* Gradient Boosting: \~100% (likely overfitting)

**SVM provided the most balanced and reliable performance.**

---

## 🌟 Impact

* Strengthened skills in **EDA, feature analysis, and model evaluation**.
* Showcased how **machine learning can assist pricing strategy** in the consumer electronics market.
* Demonstrated the importance of addressing **overfitting** and focusing on **generalizable models** (SVM in this case).
