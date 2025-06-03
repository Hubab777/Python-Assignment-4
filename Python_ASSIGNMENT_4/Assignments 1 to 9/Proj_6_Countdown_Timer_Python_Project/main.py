import time
import streamlit as st

def countdown_timer(seconds):
    start_msg = st.empty()            # Placeholder for the "starting" message
    countdown_placeholder = st.empty()  # Placeholder for the timer

    start_msg.write("⏳ Starting the countdown... ⏳")
    
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = '{:02d}:{:02d}'.format(mins, secs)
        countdown_placeholder.write(f"{time_format} ⏳")
        time.sleep(1)
        seconds -= 1

    # Countdown complete — update display
    start_msg.empty()  # Remove the "Starting..." message
    countdown_placeholder.write("00:00 🛑")
    st.write("🎉 Time is Up! 🎉")

# Streamlit UI
st.title("⏰ Countdown Timer")
total_seconds = st.number_input("Enter the countdown time in seconds:", min_value=1, step=1)

if st.button("Start Countdown"):
    countdown_timer(total_seconds)

