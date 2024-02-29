import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Ezra Smith")
    content = """
    Hello, my name is Ezra. This is my first web project using python and streamlit. This website itself is one of the projects that I am working on,
    including this page that showcases all of my projects, and a contact form. \n\nI was a .net developer who over the years has unfortunately lost several skillsets
    due to not ending up in a development role. As python feels more useful to my every day life, and not as an actual career choice, this is mostly just for fun.
    """
    st.info(content)

content_about = """Below you can find the projects that I have worked on during the course:
"Learn Python completely in 60 days or less by building 20 real-world applications from web development to data science."
\nIt's on UDEMY and I want to give credit to the course.
"""
st.write(content_about)
st.title("29/02/24 - set up homepage. contact form not functional. no projects added.")
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
