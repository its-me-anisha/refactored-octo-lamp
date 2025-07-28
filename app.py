import streamlit as st

# Set page config
st.set_page_config(
    page_title="Hello App",
    page_icon="👋",
    layout="centered"
)

# Main content
st.title("👋 Hello!")
st.write("Welcome to my Streamlit app!")

# Add some interactivity
name = st.text_input("What's your name?", placeholder="Enter your name here...")

if name:
    st.success(f"Hello, {name}! Nice to meet you! 🎉")
else:
    st.info("Please enter your name above to get a personalized greeting!")

# Add some fun elements
st.markdown("---")
st.subheader("About this app")
st.write("This is a simple Streamlit app created to say hello to users.")

# Add a button
if st.button("Click me for a surprise!"):
    st.balloons()
    st.write("🎈 Surprise! You got balloons! 🎈")

# Footer
st.markdown("---")
st.markdown("*Made with ❤️ using Streamlit*") 