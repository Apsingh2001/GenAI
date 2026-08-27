import streamlit as st

st.title("Price Calculator")

price = st.number_input("Product price", min_value=0.0, value=0.0, step=1.0)
discount = st.slider("Discount percentage", min_value=0, max_value=50, value=0)

if st.button("Calculate Discounted Price"):
    discounted_price = price * (1 - discount / 100)
    st.success(
        f"Original Price: {price:.2f}\n\n"
        f"Discount: {discount}%\n\n"
        f"Final Price: {discounted_price:.2f}"
    )
    st.table([
        ["Before", "After"],
        [f"{price:.2f}", f"{discounted_price:.2f}"],
    ])
