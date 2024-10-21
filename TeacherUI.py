import streamlit as st
import pandas as pd

#Login

credentials = {
    "Mrs Lee": "UserLee123",
    "Mr Gan": "IamMrGan"
}



st.write("""
Teacher Log In""")
user = st.text_input("Username", key='name')
password = st.text_input("Password", key='password', type="password")

if st.button("Log In"):
    if user in credentials.keys():
         if credentials[user] != password:
           st.write("""
           Password Incorrect....""")
    else:
         st.write("""
         Unknown user name....""")

        
