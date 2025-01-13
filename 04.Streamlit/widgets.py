import streamlit as st 
import pandas as pd

st.title("Stramlit text input")

name = st.text_input("What is your name?")

if name:
    st.write(f"Hello {name}!")

age = st.slider("Select your age", 0, 100, 25)

if age:
    st.write(f"Your age is {age}")

options = ['Python', 'C++', 'Java']

lang = st.selectbox(label="Languages", options=options)

if lang:
    st.write(f"Your selected {lang}")
    
data = {
    "Name": ["Satvik", "Ishita", "Rajni"],
    "Age": [20, 21, 40],
    "City": ["Chennai", "Delhi", "Delhi"]
}

df = pd.DataFrame(data)
# df.to_csv("sampleinput.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)   