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

# Subjects
subjects = ["Physics", "Chemistry", "Biology", "Maths", "English"]

# User input section
st.sidebar.header("✏️ Enter Your Study Data")

study_hours = []
completed_tasks = []

for subject in subjects:

    st.sidebar.subheader(subject)

    hours = st.sidebar.number_input(
        f"Hours studied - {subject}",
        min_value=0.0,
        max_value=24.0,
        value=0.0,
        step=0.5,
        key=f"hours_{subject}"
    )

    tasks = st.sidebar.number_input(
        f"Tasks completed - {subject}",
        min_value=0,
        max_value=100,
        value=0,
        step=1,
        key=f"tasks_{subject}"
    )

    study_hours.append(hours)
    completed_tasks.append(tasks)

# Create DataFrame
df = pd.DataFrame({
    "Subject": subjects,
    "Study Hours": study_hours,
    "Completed Tasks": completed_tasks
})

# Statistics
total_hours = df["Study Hours"].sum()

average_hours = df["Study Hours"].mean()

total_tasks = df["Completed Tasks"].sum()

top_subject = df.loc[
    df["Study Hours"].idxmax(), "Subject"
]

# Dashboard
st.subheader("📊 Study Statistics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Hours", total_hours)
col2.metric("Average Hours", round(average_hours, 2))
col3.metric("Tasks Completed", total_tasks)
col4.metric("Top Subject", top_subject)

# Data table
st.subheader("📋 Your Study Data")

st.dataframe(df, use_container_width=True)

# Bar chart
st.subheader("📈 Study Hours by Subject")

fig = px.bar(
    df,
    x="Subject",
    y="Study Hours",
    color="Subject",
    text="Study Hours",
    title="Study Hours Analysis"
)

st.plotly_chart(fig, use_container_width=True)

# Pie chart
st.subheader("🥧 Study Time Distribution")

fig2 = px.pie(
    df,
    names="Subject",
    values="Study Hours",
    hole=0.4,
    title="Study Time Distribution"
)

st.plotly_chart(fig2, use_container_width=True)

# Task chart
st.subheader("📝 Completed Tasks by Subject")

fig3 = px.bar(
    df,
    x="Subject",
    y="Completed Tasks",
    color="Subject",
    title="Task Completion"
)

st.plotly_chart(fig3, use_container_width=True)

st.success("Your study data has been analyzed!")
