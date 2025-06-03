import streamlit as st

# 🌈 Custom CSS for styling
st.markdown("""
    <style>
        .big-font {
            font-size: 24px !important;
            font-weight: bold;
            color: #2E86AB;
        }
        .emoji-title {
            font-size: 40px;
        }
        .recommend-box {
            border: 2px solid #4CAF50;
            padding: 10px;
            border-radius: 10px;
            background-color: #e8f5e9;
        }
        .stApp {
        background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSjZA1oDcQ3YcWHKDxuCeCFbkZz84-POIqpYg&s");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }
    </style>
""", unsafe_allow_html=True)

# 🏷️ Title
st.title('🧮 BMI Calculator')
st.write("📏 Enter your height and weight to calculate your BMI.")

# 📏 Height Input (m, cm, ft/in)
height_unit = st.radio("Select height unit", ("cm", "m", "ft/in"))

if height_unit == "cm":
    height_cm = st.number_input("Enter height in centimeters", min_value=0.0, format="%.2f")
    height_meters = height_cm / 100

elif height_unit == "m":
    height_meters = st.number_input("Enter height in meters", min_value=0.0, format="%.2f")

elif height_unit == "ft/in":
    col1, col2 = st.columns(2)
    with col1:
        feet = st.number_input("Feet", min_value=0.0, format="%.0f")
    with col2:
        inches = st.number_input("Inches", min_value=0.0, format="%.1f")
    
    total_inches = feet * 12 + inches
    height_meters = total_inches * 0.0254  # 1 inch = 0.0254 m

# ⚖️ Weight Input (kg or pounds)
weight_unit = st.radio("Select weight unit", ("kg", "lbs"))
weight_input = st.number_input("Weight", min_value=0.0, format="%.2f")
weight_kg = weight_input * 0.453592 if weight_unit == "lbs" else weight_input

# 🧮 BMI Calculation
if st.button("📊 Calculate BMI"):
    if height_meters > 0 and weight_kg > 0:
        bmi = weight_kg / (height_meters ** 2)
        st.markdown(f'<p class="big-font">📈 Your BMI is: {bmi:.2f}</p>', unsafe_allow_html=True)

        # 💡 BMI Interpretation + 🍎 Food Emoji + 🍽️ Recommendations
        if bmi < 18.5:
            st.warning("😟 You are underweight. 🥛🥚🍞")
            st.markdown("""
                <div class='recommend-box'>
                🥗 <strong>Recommendations:</strong><br>
                - Increase calorie intake with healthy fats and carbs.<br>
                - Include nuts, dried fruits, milkshakes, and peanut butter.<br>
                - Consider strength training to build muscle mass.
                </div>
            """, unsafe_allow_html=True)

        elif 18.5 <= bmi < 24.9:
            st.success("✅ You have a normal weight. 🥦🍗🍚")
            st.markdown("""
                <div class='recommend-box'>
                🥗 <strong>Recommendations:</strong><br>
                - Maintain a balanced diet and regular exercise.<br>
                - Keep hydrated and include fruits, vegetables, and lean proteins.<br>
                - Aim for consistency rather than intensity.
                </div>
            """, unsafe_allow_html=True)

        elif 25 <= bmi < 29.9:
            st.warning("⚠️ You are overweight. 🍔🍟🍕")
            st.markdown("""
                <div class='recommend-box'>
                🥗 <strong>Recommendations:</strong><br>
                - Reduce sugar and processed food intake.<br>
                - Add more physical activity like walking or cycling.<br>
                - Eat smaller portions, more frequently.
                </div>
            """, unsafe_allow_html=True)

        else:
            st.error("🚨 You are obese. 🍩🥤🍫")
            st.markdown("""
                <div class='recommend-box'>
                🥗 <strong>Recommendations:</strong><br>
                - Consult a healthcare provider or nutritionist.<br>
                - Avoid sugary drinks and high-calorie snacks.<br>
                - Increase fiber intake and aerobic exercise.
                </div>
            """, unsafe_allow_html=True)

        # 📊 BMI Classification Chart
        st.markdown("### 📚 BMI Categories:")
        st.table({
            "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
            "BMI Range": ["< 18.5", "18.5 – 24.9", "25.0 – 29.9", "30.0 and above"],
            "Emoji": ["😟", "✅", "⚠️", "🚨"]
        })

    else:
        st.error("❗Please enter valid values for height and weight.")
