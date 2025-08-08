import streamlit as st
import time
import random

def show_overview():
    st.subheader("Real-time CO₂e Tracking")

    # Simulating live CO₂e value changes
    co2_value = random.randint(200, 300)  # Example: replace with actual calculation
    st.metric("Current CO₂e Emission", f"{co2_value} kg", delta=random.randint(-5, 5))

    with st.expander("How this is calculated"):
        st.write("""
        The CO₂e (carbon dioxide equivalent) value here is currently simulated.
        In the final version, it can be linked to your actual carbon footprint data.
        """)
