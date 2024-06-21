import streamlit as st
import pandas

st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpeg")

with col2:
    st.title("Krishan")
    content = """
    Hi, I am Krishan! I am a Python programmer. I graduated in 2018 with a B.tech in E.I.C.
I have worked in Japan. 
    """
    st.info(content)
content2 = """
Below you can find some of the apps i have built in python . feel free to contact me!
"""
st.write(content2)

col3,col4 = st.columns(2)
df = pandas.read_csv("data.csv",sep=";")

with col3:
    for index ,row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index ,row in df[10:].iterrows():
        st.header(row["title"])