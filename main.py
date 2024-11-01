import streamlit as st
import os
if not os.path.exists("dbms/notes.csv"):
    f = open("dbms/notes.csv","w")
    f.close()
st.set_page_config(initial_sidebar_state="collapsed",page_title="Anonymous Notes Maker", page_icon="📝")
st.title("📝 Anonymous Notes Maker")
st.header("How to use ?")
st.write("""
1) Just type title and body of your notes
2) Set a password
3) Done just user it...
""")
st.header("Create your notes today!!")
st.page_link("pages/Create.py",label="Create Note",icon="📝")
st.page_link("pages/Find Note.py",label="Find Note",icon="🔍")