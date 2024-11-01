import streamlit as st
import os
if not os.path.exists("dbms/tables/notes.csv"):
    f = open("dbms/tables/notes.csv","w")
    f.close()
st.set_page_config(page_title="Anonymous Notes Maker", page_icon="📝")
st.title("📝 Anonymous Notes Maker")

st.header("How to use ?")
st.write("""
1) Just type title and body of your notes
2) Set a password
3) Done just user it...
""")
st.header("Create your notes today!!")
st.page_link("pages/Create.py",label="Create Note",icon="📝")
