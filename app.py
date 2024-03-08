import sqlite3
import google.generativeai as genai
import streamlit as st
import os
import pandas as pd
# from prompt import prompt
from test_prompt import prompt
from dotenv import load_dotenv
from datetime import datetime


load_dotenv()
genai.configure(api_key=os.getenv("gemini_api_key"))

def  get_gemini_response(question,prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql, db,start_time):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()

    if len(rows) == 0:
        st.write("The result is empty")
    elif len(rows) > 1 or len(rows[0]) > 1:
        columns = [description[0] for description in cur.description]
        data = pd.DataFrame(rows, columns=columns)
        st.dataframe(data)
        end = datetime.now()
        st.write(f"time required:{(end.second)-(start_time.second)} sec.")
    else:
        st.write(rows[0][0])
        end = datetime.now()
        st.write(f"time required:{(end.second)-(start_time.second)} sec.")
    conn.commit()
    conn.close()
    return rows



st.set_page_config(page_title="AI Analytics")
st.header("Gemini App to retrive SQL Data")

question=st.text_input("**Question**", placeholder="Ask Question About Your Data.", key='input')
# question_list = ['',"Total Users?","Total Stores?"]
# question=st.selectbox("**Question**",question_list)
submit=st.button('Send ⬆️')


if submit and question:
    start  = datetime.now()
    response = get_gemini_response(question, prompt)
    res = response.split("```")
    query = (res[1].removeprefix("sql\n")).removesuffix("\n")
    logic = (res[2].removeprefix("\n\n")).removesuffix("\n")
    st.write("**SQL Query :**",query)
    st.write("\n")
    st.write(logic)
    st.write("\n")
    st.write("**The Response is:**")
    data = read_sql_query(query, "rewardola1.db",start)
    print("SQL Query:",query)
    print("Logic & Explaination:",logic)