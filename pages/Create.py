import streamlit as st
from dbms.db_commands import db
db = db()
st.title("Create Note")
title = st.text_input("Title",key="title",placeholder="Title").replace(',',"%#$d35f906(")
body = st.text_area("Body",key="body",placeholder="Body",height=250).replace(',',"%#$d35f906(")
password = st.text_input("Password",key="pass",placeholder="Password").replace(',',"%#$d35f906(")
if (not(title==""or body==""or password=="")):
    btn_res= st.button("Create Note")
    if (btn_res):
        id = db.insert_into_table("notes",values=[title,body,password],fields=["title","body","password"])
        st.success("Note Created")
        st.link_button("View Note",f"/Note?id={id}&password={password}")