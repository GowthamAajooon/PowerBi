import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pagesz1():
    st.title("Welcome to Page 1")
    st.write("This is the content of Page 1.")

    # Call additional functions to show different content
    display_chart()
    display_data()

def display_chart():
    st.subheader("Sample Chart")
    
    # Create some sample data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)

    # Plot the chart
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("Sine Wave")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    
    # Display the chart in Streamlit
    st.pyplot(fig)

def display_data():
    st.subheader("Sample Data")
    
    # Create a sample DataFrame
    data = {
        'Column A': np.random.randint(1, 10, 10),
        'Column B': np.random.rand(10),
        'Column C': np.random.choice(['A', 'B', 'C'], 10)
    }
    df = pd.DataFrame(data)

    # Display the DataFrame
    st.dataframe(df)

