# 📦 Supply Chain & Logistics Performance Analytics

## Project Overview
This project is an end-to-end data analytics and machine learning pipeline designed to evaluate and predict supply chain efficiency. Using the Olist Brazilian E-Commerce dataset, the project transforms raw, multi-table relational data into a clean analytical dataset, engineers key logistical metrics, and deploys a predictive Machine Learning model via an interactive web dashboard.

## 🚀 Live Demo
**[Launch Streamlit Web App](https://share.streamlit.io/)** *(Update with your deployed link)*

## 🛠️ Technology Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Decision Tree Classifier)
* **Visualization:** Matplotlib, Seaborn
* **Deployment & Web UI:** Streamlit

## 📊 Key Features
* **Automated Data Wrangling:** Merged multiple raw CSV files (Orders, Items, Customers, Products) and engineered logical features like `transit_time_days` and `is_late` flags.
* **Exploratory Data Analysis (EDA):** Analyzed geographic delivery bottlenecks and evaluated the correlation between product weight, freight cost, and delivery delays.
* **Predictive Modeling:** Trained a Decision Tree Classifier to predict the probability of a shipment being delayed based on physical product attributes and destination states.
* **Interactive Dashboard:** Built a live Streamlit application allowing stakeholders to filter KPIs by region and test "What-If" scenarios using the predictive model.

## 💻 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/dileepkumarmallela391/supply-chain-analytics-dashboard.git](https://github.com/dileepkumarmallela391/supply-chain-analytics-dashboard.git)
   cd supply-chain-analytics-dashboard
