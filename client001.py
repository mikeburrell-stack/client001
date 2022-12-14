import streamlit as st
import pandas as pd
import numpy as np

# Markdown: # symbol refers to heading level 1, ## heading level 2
st.write(""" # Forecast 2022 Oct """)

st.write(""" Normal Text """)

st.write(""" ## Model """)

st.write(""" ### Data """)

df = pd.DataFrame({
  'col 1': [1,2,3],  'col 2': [10,20,30]
})

st.write(df)

df2 = pd.DataFrame(
  np.random.randn(20,3),
  columns = ['a','b','c']
)

st.line_chart(df2)

x = st.slider('x')
st.write(x,'Square the value', x * x)

st.text_input("your name", key="name")

st.session_state.name

col1,col2,col3 = st.columns(3)
col1.metric("USD", "18.01 $","0.5 $")
col2.metric("ZND", "15.01 $","-1.5 $")
col3.metric("BWP", "16.50 $","1.2 $")



