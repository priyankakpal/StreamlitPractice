import streamlit as st 

st.title("First streamlit project")
st.header("Hello Web App")

agree = st.checkbox("Hello I am agree with Priyanka...")

if agree:
    st.write("Great")

genre = st.radio("what's your favorite movie genre",['comedy','Drama','Documentary'])

if genre == 'comedy':
    st.write('Hahaa')