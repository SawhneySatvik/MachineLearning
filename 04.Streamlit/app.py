import streamlit as st 
import pandas as pd
import numpy as np

"""
streamlit run app.py
"""

# Title of the application
st.title("Hello Streamlit")

# Simple Text
st.write("This is a simple text")

df = pd.DataFrame({
    'first col': [1, 2,3 , 4],
    'second col': [10, 20, 30, 40]
})

# display the dataframe
st.write('Here is the dataframe')
st.write(df)


#create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns = ['a', 'b', 'c']
)

st.line_chart(chart_data)