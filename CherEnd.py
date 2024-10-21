import streamlit as st
import pandas as pd
from io import StringIO

st.write("""
Welcome Back....""")


# Upload files

st.file_uploader("Upload pdf notes:", type=["pdf"], key="uploaded_file")

st.file_uploader("Upload recording of class:", type=["mp3"], key="uploaded_file")

st.file_uploader("Upload document notes:", type=["doc"], key="uploaded_file")























#uploaded_file = st.file_uploader("Choose a file")
#if uploaded_file is not None:
    # To read file as bytes:
    #bytes_data = uploaded_file.getvalue()

    # To convert to a string based IO:
    #stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

    # To read file as string:
    #string_data = stringio.read()

    # Can be used wherever a "file-like" object is accepted:
    #dataframe = pd.read_csv(uploaded_file)
