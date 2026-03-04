import streamlit as st
import matplotlib.pyplot as plt

# 
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️", layout="centered")

st.markdown("""
<style>

.stApp {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}

/* Button Styling */
div.stButton > button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    font-weight: bold;
    border-radius: 10px;
    height: 50px;
    width: 100%;
    border: none;
}

div.stButton > button:hover {
    background-color: #ff1e1e;
    color: white;
    transform: scale(1.05);
    transition: 0.3s;
}

</style>
""", unsafe_allow_html=True)
st.title("⚖️ BMI Calculator")

st.markdown('<div class="main-box">', unsafe_allow_html=True)

st.write("### Enter Your Details")

# ---- Input Section ----
weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (meters)", min_value=0.1)

if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    st.markdown(f"## Your BMI: `{round(bmi,2)}`")

    # Logic
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
        color = "green"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
        color = "orange"
    else:
        category = "Obese"
        color = "red"

    st.markdown(f"### Category: <span style='color:{color}'>{category}</span>", unsafe_allow_html=True)

    # ---- Chart ----
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    values = [18.5, 24.9, 29.9, 35]
    colors = ["blue", "green", "orange", "red"]

    fig, ax = plt.subplots()
    ax.bar(categories, values, color=colors)
    ax.axhline(y=bmi, color="white", linestyle="--", linewidth=2)
    ax.set_facecolor("#2c2f4a")
    fig.patch.set_facecolor("#2c2f4a")
    plt.xticks(rotation=45, color="white")
    plt.yticks(color="white")
    ax.set_title("BMI Categories Chart", color="white")

    st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)