import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="🎓 Student Data Generator", layout="wide")
st.markdown("<h1 style='color: #4CAF50;'>📄 Student CSV File Generator</h1>", unsafe_allow_html=True)
st.markdown("Generate colorful & fun student reports with 🎓 Grades, ✅ Status & 📊 Marks!")

names = ["Rayyan", "Hiba", "Daniyal", "Laiba", "Usman", "Aleena", "Hamza", "Eman", "Saad", "Zoya"]

# Grade assignment based on marks
def get_grade(marks):
    if marks >= 90:
        return "A+ 🌟"
    elif marks >= 80:
        return "A 🏅"
    elif marks >= 70:
        return "B+ 😊"
    elif marks >= 60:
        return "B 🙂"
    elif marks >= 50:
        return "C 😐"
    elif marks >= 40:
        return "D 😟"
    else:
        return "F 💀"

# Pass/Fail assignment
def get_status(marks):
    return "✅ Pass" if marks >= 40 else "❌ Fail"

students = []
for i in range(1, 11):
    marks = random.randint(30, 100)
    student = {
        "ID": i,
        "Name": random.choice(names),
        "Age": random.randint(17, 24),
        "Marks": marks,
        "Grade": get_grade(marks),
        "Status": get_status(marks)
    }
    students.append(student)

df = pd.DataFrame(students)

# Styled Table
st.markdown("<h2 style='color: #2196F3;'>📊 Generated Student Data</h2>", unsafe_allow_html=True)
st.dataframe(df.style
    .applymap(lambda val: 'color: green; font-weight: bold' if val == "✅ Pass" else 'color: red', subset=['Status'])
    .applymap(lambda val: 'background-color: #E3F2FD' if "A+" in str(val) else '', subset=['Grade'])
)

# CSV Download
csv_file = df.to_csv(index=False).encode('utf-8')
st.download_button("⬇️ Download CSV File", csv_file, "students.csv", "text/csv")
st.success("🎉 Students Report Generated Successfully!")
