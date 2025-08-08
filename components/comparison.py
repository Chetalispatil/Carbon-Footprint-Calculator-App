import streamlit as st

def show_comparison():
    st.subheader(" Comparison to National Average")

    # Example numbers — replace with your actual logic
    user_emission = 440
    avg_emission = 520
    difference = avg_emission - user_emission

    if difference > 0:
        st.success(f" Your emissions are {difference} kg **less** than the national average!")
    elif difference < 0:
        st.error(f" Your emissions are {-difference} kg **more** than the national average.")
    else:
        st.info("ℹ Your emissions are exactly at the national average.")
