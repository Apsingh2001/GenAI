import streamlit as st

st.title("Simple Sales Dashboard")
st.write("View monthly sales performance.")

months = ["January", "February", "March", "April"]
sales = {
    "January": 1200,
    "February": 1500,
    "March": 900,
    "April": 2000,
}

selected_month = st.selectbox("Select a month", months)
st.metric("Sales", f"{sales[selected_month]:,}")

st.subheader("Monthly Sales")
st.bar_chart(list(sales.values()))
