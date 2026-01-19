import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="User Registration", layout="centered")

st.title("📝 User Registration Form")

# File to store users
DATA_FILE = "users.csv"

# Create file if not exists
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Name", "Email", "Password"])
    df.to_csv(DATA_FILE, index=False)

# Registration form
with st.form("registration_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    password = st.text_input("Password", type="password")

    submit = st.form_submit_button("Register")

if submit:
    if not name or not email or not password:
        st.error("❌ All fields are required")
    else:
        # Save data
        new_user = pd.DataFrame([[name, email, password]],
                                columns=["Name", "Email", "Password"])
        new_user.to_csv(DATA_FILE, mode="a", header=False, index=False)

        st.success("✅ Registration successful!")
