import streamlit as st
from db_commands import db
db = db()
params = st.query_params
if (not params.get("id") or not params.get("password")):
    st.error("Unauthorized Access!!")
else:
    id = st.query_params["id"].replace(" ","")
    raw_data = db.get_data("notes")
    found_data = None
    for i in raw_data:
        if (i["id"]==id):found_data=i;break
    if(found_data==None):st.error("Note not found")
    else:
        if (found_data["password"].replace("%#$d35f906(","")==st.query_params["password"]):
            st.header("Title: "+found_data["title"].replace("%#$d35f906(",","))
            st.write("Id: ",found_data["id"])
            st.write("Password: "+found_data["password"].replace("%#$d35f906(",""))
            st.write(found_data["body"].replace("%#$d35f906(","").replace("%&$HTSSGRSRy35644rFGFlP}';","\n"))
        else:st.error("Wrong Password")
