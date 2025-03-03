import streamlit as st

st.title("🔄 Universal Unit Converter")
st.markdown("### Convert Length, Weight, and Time Instantly!")
st.write("Hey there! Choose a conversion type, enter your value, and see the magic happen in real time.")

category = st.selectbox("📌 Select a Category", ["Length", "Weight", "Time"])

def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
        
    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24
    return 0

if category == "Length":
    unit = st.selectbox("📏 Choose a Conversion", ["Miles to Kilometers", "Kilometers to Miles"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Choose a Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏳ Choose a Conversion", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

value = st.number_input("🔢 Enter the value you want to convert")

if st.button("🔄 Convert Now!"):
    result = convert_units(category, value, unit)
    st.success(f"✅ Converted Value: {result:.2f}")
