import streamlit as st

# Import pages
from pages1 import pagesz1
from page2 import page2

# Set the page title
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a page:", ["Page 1", "Page 2"])

# Route to the selected page
if page == "Page 1":
    pagesz1()
elif page == "Page 2":
    page2()
