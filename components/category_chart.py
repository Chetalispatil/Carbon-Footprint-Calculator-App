import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_category_breakdown():
    st.subheader(" Category Breakdown")

    # Example data — replace with your real category-wise data
    data = pd.DataFrame({
        "Category": ["Transport", "Electricity", "Food", "Waste"],
        "CO2_kg": [120, 200, 90, 30]
    })

    fig, ax = plt.subplots()
    ax.bar(data["Category"], data["CO2_kg"], color="#2E8B57")
    ax.set_xlabel("Category")
    ax.set_ylabel("CO₂e Emissions (kg)")
    ax.set_title("Carbon Footprint by Category")

    st.pyplot(fig)
