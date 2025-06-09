import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sustainable Lifestyle Calculator", layout="centered")

st.title("🌿 Sustainable Lifestyle Calculator")
st.markdown("----")
st.markdown("#### 🌱 How This Works:")
st.markdown("""
This app helps you understand how sustainable your lifestyle is by calculating a score based on:

- ⚡ Electricity Usage
- 🚗 Travel Habits
- 🍽️ Diet
- 🚿 Water Consumption
- 🛍️ Plastic Use

You'll get a score out of 100, eco feedback, and improvement tips.
""")
st.markdown("----")

# 🧮 INPUTS (move outside button)
electricity = st.number_input("⚡ Daily Electricity Usage (units)", min_value=0.0, step=0.1)
travel = st.selectbox("🚗 Primary Mode of Travel", ["Walking/Cycling", "Public Transport", "Bike", "Car"])
diet = st.radio("🍽️ Diet Type", ["Vegetarian", "Mixed", "Non-Vegetarian"])
water = st.number_input("🚿 Daily Water Usage (liters)", min_value=0.0, step=1.0)
plastic = st.slider("🛍️ Plastic Items Used Per Week", 0, 20, 5)

# 🧮 CALCULATION
if st.button("Calculate My Eco Score"):
    score = 100  # starting score

    # ⚡ Electricity Scoring
    if electricity > 5:
        score -= 25
    elif electricity > 3:
        score -= 15
    elif electricity > 1:
        score -= 5

    # 🚗 Travel Scoring
    if travel == "Car":
        score -= 25
    elif travel == "Bike":
        score -= 15
    elif travel == "Public Transport":
        score -= 5

    # 🍽️ Diet Scoring
    if diet == "Non-Vegetarian":
        score -= 15
    elif diet == "Mixed":
        score -= 7

    # 🚿 Water Usage
    if water > 200:
        score -= 20
    elif water > 100:
        score -= 10
    elif water > 70:
        score -= 5

    # 🛍️ Plastic Usage
    if plastic > 15:
        score -= 15
    elif plastic > 7:
        score -= 10
    elif plastic > 3:
        score -= 5

    # Clamp score
    score = max(0, min(score, 100))

    st.markdown("---")
    st.subheader("🌱 Your Sustainability Score")
    st.progress(score)

    # 📊 Score Pie Chart
    labels = ['Sustainability Score', 'Remaining']
    sizes = [score, 100 - score]
    colors = ['#4CAF50', '#d3d3d3']
    explode = (0.1, 0)

    fig, ax = plt.subplots()
    ax.pie(sizes, explode=explode, labels=labels, colors=colors,
           autopct='%1.1f%%', shadow=True, startangle=90)
    ax.axis('equal')
    st.markdown("### 📊 Score Visual")
    st.pyplot(fig)

    # 🧾 Feedback
    if score >= 80:
        st.success(f"✅ Excellent! Your score is {score}/100. You’re living sustainably! 🌟")
    elif score >= 50:
        st.warning(f"⚠️ Not bad! Your score is {score}/100. Let’s improve a bit.")
    else:
        st.error(f"🚨 Needs Improvement! Your score is {score}/100. Time to make changes.")

    # 💡 Eco Tips
    st.markdown("### 💡 Eco Tips:")

    if electricity > 3:
        st.markdown("- Reduce usage of high-power devices. Try LED lights and smart switches.")
    if travel in ["Car", "Bike"]:
        st.markdown("- Use public transport, carpooling, or cycle short distances.")
    if diet == "Non-Vegetarian":
        st.markdown("- Reduce meat consumption. Go veg a few days a week.")
    if water > 100:
        st.markdown("- Fix leaks and install low-flow taps or showers.")
    if plastic > 5:
        st.markdown("- Say no to plastic bags and use reusables.")
