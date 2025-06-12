import streamlit as st
import requests
import pandas as pd


st.title("Salary Advance & Loan Calculator")

with st.form("loan_form"):
    name = st.text_input("Your Name")
    position = st.selectbox("Your Position", ["Junior", "Mid", "Senior", "Lead"])
    req_amount = st.number_input("Requested Amount", min_value=0.0, format="%.2f")
    annual_rate = st.number_input("Annual Interest Rate (%)", min_value=0.0, format="%.2f")
    months = st.number_input("Number of Months", min_value=1, max_value=60, value=12)
    submitted = st.form_submit_button("Calculate Loan")

if submitted:
    payload = {
        "name": name,
        "position": position,
        "requested_amount": req_amount,
        "annual_rate": annual_rate,
        "period_months": int(months)
    }
    try:
        resp = requests.post("http://backend:8000/loan", json=payload)
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        st.error(f"Error calling backend: {e}")
    else:
        st.success(f"Advanc approved: {data['advance_amount']}")
        schedule = pd.DataFrame(data['schedule'])
        st.dataframe(schedule)