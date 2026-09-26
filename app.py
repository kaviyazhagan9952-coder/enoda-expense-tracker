import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Enoda Expense Tracker")

st.title("💰 Enoda Expense Tracker")

# Sidebar la input
st.sidebar.header("Pudhu Selavu Add Pannu")
selavu_name = st.sidebar.text_input("Enna selavu?")
amount = st.sidebar.number_input("Evalo Rs?", min_value=1)
selavu_date = st.sidebar.date_input("Date", date.today())
category = st.sidebar.selectbox("Vagai", ["Food", "Travel", "Shopping", "Bills", "Others"])

if st.sidebar.button("Add Pannu"):
    # Excel la save pannum logic
    try:
        df = pd.read_csv("expenses.csv")
    except:
        df = pd.DataFrame(columns=["Date", "Name", "Category", "Amount"])
    
    new_data = pd.DataFrame([[selavu_date, selavu_name, category, amount]], 
                            columns=["Date", "Name", "Category", "Amount"])
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv("expenses.csv", index=False)
    st.sidebar.success("Saved!")

# Main page la kaamikurathu
try:
    df = pd.read_csv("expenses.csv")
    st.subheader("Total Selavu: Rs. " + str(df["Amount"].sum()))
    
    st.dataframe(df)
    
    # Pie chart
    st.subheader("Enga athigam selavu panrom?")
    chart_data = df.groupby("Category")["Amount"].sum()
    st.bar_chart(chart_data)

except:
    st.info("Innum selavu ethuvum add pannala. Sidebar la add pannunga.")