# Team members and there contributions ( Does not show relative ranking of contributions )
# Samay Patel (2403127) - Custom Database for Notes and Home Page
# Amruta Dagle (2403113) - Create note section
# Dhanvith Kumar (2403110) - Find Note Section
# Saksham Pandey (2404232) - Find Note Section
# Joy Prakash (2403120) - View Note Section


import streamlit as st
import os
if not os.path.exists("notes.csv"):
    f = open("notes.csv","w")
    f.write("id,title,body,password\n")
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