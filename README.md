# Telco Customer Churn Analysis

Analyzed customer churn using **Python** for data cleaning and exploratory data analysis (EDA) and built an interactive **Power BI dashboard** to uncover key business insights.

---

# Table of Contents

- [Overview](#overview)
- [Problem Statement](#problem-statement)
- [Project Structure](#project-structure)
- [Dataset](#dataset)
- [Tools & Technologies](#tools--technologies)
- [Methodology](#methodology)
- [Key Insights](#key-insights)
- [Dashboard](#dashboard)
- [How to Run This Project](#how-to-run-this-project)
- [Results & Conclusion](#results--conclusion)
- [Future Work](#future-work)
- [Author](#author)

---

# Overview

This project analyzes customer churn in a telecom company to identify the key factors influencing customer churn.

Python was used for data cleaning and exploratory data analysis (EDA), while Power BI was used to build an interactive dashboard for business insights.

---

# Problem Statement

Customer churn is a major challenge for telecom companies as it directly impacts revenue and customer retention.

The objective of this project is to identify the factors associated with customer churn and provide actionable insights through data analysis and visualization.

---

# Project Structure

```text
Telco-Customer-Churn-Analysis/
│
├── Dataset/
│   └── Telco-Customer-Churn.csv
│
├── Python/
│   └── Telco_churn.py
│
├── Dashboard/
│   ├── Customer Churn Analysis.pbix
│   └── Dashboard.png
│
└── README.md
```

---

# Dataset

- **Dataset:** Telco Customer Churn
- **Format:** CSV

### Key Columns

- CustomerID
- Gender
- SeniorCitizen
- Partner
- Dependents
- Tenure
- PhoneService
- MultipleLines
- InternetService
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- StreamingTV
- StreamingMovies
- Contract
- PaymentMethod
- MonthlyCharges
- TotalCharges
- Churn

---

# Tools & Technologies

- Python
- Pandas
- Power BI

---

# Methodology

1. Imported the dataset into Python.
2. Cleaned missing values and corrected data types.
3. Performed exploratory data analysis (EDA).
4. Exported the cleaned dataset.
5. Built an interactive dashboard in Power BI.

---

# Key Insights

- Customers with Month-to-Month contracts have the highest churn rate.
- Fiber Optic customers show a higher churn rate than DSL customers.
- Customers with higher monthly charges are more likely to churn.
- Customers with shorter tenure have a greater likelihood of churning.
- Electronic Check is the most common payment method among churned customers.
- Senior citizens have a higher churn rate than non-senior customers.

---

# Dashboard

![Dashboard](Dashboard/Dashboard.png)

---

# How to Run This Project

1. Clone this repository.
2. Open the Python script in the **Python** folder and run it.
3. Open the Power BI file (`Telco_Customer_Churn.pbix`) from the **Dashboard** folder.
4. Refresh the data if required.

---

# Results & Conclusion

The analysis identified contract type, tenure, internet service, monthly charges, payment method, and senior citizen status as key factors associated with customer churn.

These insights can help telecom companies understand customer behavior and support data-driven decision-making.

---

# Future Work

- Build a machine learning model to predict customer churn.
- Automate dashboard refresh using Power BI Service.
- Develop a customer churn prediction dashboard with real-time insights.

---

# Author

**Rashi Gondane**

Aspiring Data Analyst