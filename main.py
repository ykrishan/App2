import streamlit as st


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Krishan Sulce")
    content = """
    Hi, I am Krishan! I am a Python programmer. I graduated in 2018 with a B.tech in E.I.C.
I have worked in Japan. 
    """
    st.info(content)
content2 = """
Below you can find some of the apps i have built in python . feel free to contact me!
"""
st.write(content2)