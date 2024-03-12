import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)
with col1:
    st.image("images/photo.jpg")
with col2:
    st.title("Ezra Smith")
    content = """
    Hello, my name is Ezra. This is my first web project using python and streamlit. This website itself is one of the 
    projects that I am working on, including this page that showcases all of my projects, and a contact form. \n\n
    I was a .net developer who entered the automotive SaaS industry as tech support,to get my foot in the door. 
    I never made it onto a dev team but as python feels more useful to my every day life, this is just for fun.
    """
    st.info(content)

content_about = """Below you can find the projects that I have worked on during the course:\n
"Learn Python completely in 60 days or less by building 20 real-world applications from web development to data science."
\nIt's on UDEMY and pretty effin cool.
"""
st.write(content_about)
st.title("Current Project being worked: Generate PDF Template")
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
