import streamlit as st

st.title("Find Note")
id = st.text_input("Note Id",key="id",placeholder="Enter note id")
password = st.text_input("Password",key="pass",placeholder="Password")
if (not(id==""or password=="")):
    st.link_button("Get Note",f"/Note?id={id}&password={password}")