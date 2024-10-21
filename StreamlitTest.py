
import streamlit as st
import numpy as np
import pandas as pd


## Code

st.write("""
Gopal Country Club""")

  # Like and Dislike Chart
chart_data = pd.DataFrame(
     data=np.random.randn(20, 2),
     columns=['Dislikes', 'likes'])
     
chart_data = pd.DataFrame({"Likes":[2, 3, 4, 5], "Dislikes": [9, 5, 6, 1]})

print(chart_data)

st.line_chart(chart_data)

  # Map




  # Widget
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
st.text_input("Your name", key="name")

st.session_state.name


if st.checkbox('Show dataframe'):
    #chart_data = pd.DataFrame(
    #   np.random.randn(20, 3),
    #   columns=['a', 'b', 'c'])
    chart_data = pd.DataFrame(data)

    chart_data

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'What is your favourite type of country stuff?',
     df['first column'])

'You selected: ', option

 
add_selectbox = st.sidebar.selectbox(

    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)







