import streamlit as st 

st.title("Basic Calculator")

def Calculator(x):
    return x*x


number = st.number_input("Enter the number")

if st.button("Get Square"):
    st.header(Calculator(number))