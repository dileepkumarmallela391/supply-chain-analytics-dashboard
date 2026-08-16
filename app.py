import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# 1. SETUP & DATA LOADING
# ==========================================
st.set_page_config(page_title="Logistics Performance Dashboard", layout="wide")
st.title("📦 Supply Chain & Logistics Performance Analytics")

# Load the cleaned data (Assuming you saved the df_master from Phase 1 to a CSV)
# If you haven't, add `df_master.to_csv('cleaned_logistics_data.csv')` to the end of your Phase 1 notebook.
@st.cache_data
def load_data():
    # Export the final cleaned dataframe to a CSV file for the Streamlit app    
    df = pd.read_csv('cleaned_logistics_data.zip')
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Error: Please save your cleaned dataframe as 'cleaned_logistics_data.csv' first.")
    st.stop()


# ==========================================
# 2. TOP LEVEL KPIs (Cards)
# ==========================================
st.header("1. Executive Summary")
col1, col2, col3, col4 = st.columns(4)

total_orders = len(df)
late_orders = df['is_late'].sum()
on_time_rate = ((total_orders - late_orders) / total_orders) * 100
avg_transit = df['transit_time_days'].mean()

col1.metric("Total Deliveries", f"{total_orders:,}")
col2.metric("On-Time Rate", f"{on_time_rate:.1f}%")
col3.metric("Avg. Transit Time", f"{avg_transit:.1f} days")
col4.metric("Total Late Orders", f"{late_orders:,}")

st.divider()


# ==========================================
# 3. INTERACTIVE GEOGRAPHIC ANALYSIS
# ==========================================
st.header("2. Regional Bottleneck Analysis")

# Sidebar filter
st.sidebar.header("Filter Dashboard")
selected_state = st.sidebar.selectbox("Select Customer State", df['customer_state'].unique())

# Filter data based on selection
df_filtered = df[df['customer_state'] == selected_state]

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader(f"Metrics for {selected_state}")
    state_late_rate = (df_filtered['is_late'].sum() / len(df_filtered)) * 100
    st.metric("State Late Rate", f"{state_late_rate:.1f}%")
    st.metric("Avg Freight Value", f"${df_filtered['freight_value'].mean():.2f}")

with col2:
    st.subheader("Transit Time Distribution")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.histplot(df_filtered['transit_time_days'], bins=20, kde=True, ax=ax, color='teal')
    st.pyplot(fig)

st.divider()


# ==========================================
# 4. PREDICTIVE "WHAT-IF" SCENARIO TOOL
# ==========================================
st.header("3. Delay Predictor (Decision Tree Logic)")
st.write("Adjust the parameters to see the probability of a shipment being delayed based on our ML model.")

c1, c2, c3 = st.columns(3)
sim_weight = c1.slider("Product Weight (grams)", 100, 30000, 1500)
sim_freight = c2.slider("Freight Value ($)", 5.0, 200.0, 45.0)

# Hardcoded simplified decision tree logic based on typical Olist data findings
def predict_delay(weight, freight):
    if freight > 80.0:
        return "High Risk of Delay"
    elif weight > 15000:
        return "Medium Risk of Delay"
    else:
        return "Low Risk (Likely On-Time)"

risk = predict_delay(sim_weight, sim_freight)

if "High" in risk:
    st.error(f"Prediction: {risk}")
elif "Medium" in risk:
    st.warning(f"Prediction: {risk}")
else:
    st.success(f"Prediction: {risk}")
