import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Ezra Smith")
    content = """
    Hello, my name is Ezra. I am working through some udemy courses while I learn how to automate my job. Below are some images that I got from the course, and the
    different projects that I have completed so far. This is my first web project using python and streamlit.
    """
    st.info(content)

content_about = """Below you can find the projects that I have worked on during the course:
Learn Python completely in 60 days or less by building 20 real-world applications from web development to data science.
"""
st.write(content_about)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
