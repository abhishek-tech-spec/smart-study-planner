
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Study Planner",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Smart Study Planner")
st.write("Track your study progress and improve your productivity!")

# Sample data
df = pd.DataFrame({
    "Subject": ["Physics", "Chemistry", "Biology", "Maths", "English"],
    "Study Hours": [2, 1.5, 3, 2, 1],
    "Completed Tasks": [4, 3, 5, 4, 2]
})

# Statistics
total_hours = df["Study Hours"].sum()
average_hours = df["Study Hours"].mean()
total_tasks = df["Completed Tasks"].sum()
top_subject = df.loc[df["Study Hours"].idxmax(), "Subject"]

# Dashboard
st.subheader("📊 Study Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Hours", total_hours)
col2.metric("Average Hours", round(average_hours, 2))
col3.metric("Tasks Completed", total_tasks)
col4.metric("Top Subject", top_subject)

# Bar Chart
st.subheader("📈 Study Hours by Subject")

fig = px.bar(
    df,
    x="Subject",
    y="Study Hours",
    color="Subject",
    text="Study Hours"
)

st.plotly_chart(fig, use_container_width=True)

# Pie Chart
st.subheader("🥧 Study Time Distribution")

fig2 = px.pie(
    df,
    names="Subject",
    values="Study Hours",
    hole=0.4
)

st.plotly_chart(fig2, use_container_width=True)
