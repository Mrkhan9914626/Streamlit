import streamlit as st

# # Title
st.title("Streamlit Text Input Examples")

# # # Text Input
name = st.text_input("Enter your name:", "")

# # # Text Area
feedback = st.text_area("Enter your feedback:", "")

# # # Number Input
age = st.number_input("Enter your age:", min_value=0, max_value=120, step=1)

# # Date Input
import datetime

start_date = datetime.date(1920, 1, 1)  # Set your desired start date
end_date = datetime.date(2025, 12, 31)  # Set your desired end date

date = st.date_input("Select a date:", value=start_date, min_value=start_date, max_value=end_date)


# # Time Input
# Create a datetime object representing the desired initial time
initial_time = datetime.time(15, 30)  # 3:30 PM

# Use the value argument to set the initial time in the widget
time = st.time_input("Select a time:", value=initial_time)

# The user can now modify the time directly in the UI


# # Color Picker
color = st.color_picker("Pick a color")

# Display inputs
st.write("Name:", name)
st.write("Feedback:", feedback)
st.write("Age:", age)
st.write("Date:", date)
st.write("Time:", time)
st.write("Color:", color)

# # print color based on color values

# # HTML
html_code = """
        <h1 style='color: {};'>This is a Custom Color heading</h1>
        <p style='color: green;'>This is a green paragraph</p>
""".format(color)
st.markdown(html_code, unsafe_allow_html=True)