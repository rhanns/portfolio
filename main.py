import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg")

with col2:
    st.title("Ezra Smith")
    content = """
    Hello, my name is Ezra. I am working through some udemy courses while I learn how to automate my job. Below are some images that I got from the course, and the
    different projects that I have completed so far.
    """
    st.info(content)