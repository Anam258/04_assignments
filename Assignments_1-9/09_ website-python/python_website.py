import streamlit as st
import pandas as pd

# Title of the Dashboard
st.title("📊 Simple Data Dashboard")

# File uploader to accept CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

# Check if a file has been uploaded
if uploaded_file is not None:
    # Read the CSV file using pandas
    df = pd.read_csv(uploaded_file)

    # Show the top 5 rows of the data
    st.subheader("👀 Data Preview")
    st.write(df.head())

    # Show statistical summary of the data
    st.subheader("📈 Data Summary")
    st.write(df.describe())

    # Filtering section
    st.subheader("🔍 Filter Data")
    
    # Let user select column to filter
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column to filter by", columns)

    # Show unique values from the selected column
    unique_values = df[selected_column].unique()
    selected_value = st.selectbox("Select value", unique_values)

    # Filter the dataframe based on selection
    filtered_df = df[df[selected_column] == selected_value]
    st.write(filtered_df)

    # Data plotting section
    st.subheader("📊 Plot Data")

    # Let user choose x and y axis columns for plotting
    x_column = st.selectbox("Select x-axis column", columns)
    y_column = st.selectbox("Select y-axis column", columns)

    # Button to generate line chart
    if st.button("Generate Plot"):
        try:
            # Set index as x-axis column and plot y values
            st.line_chart(filtered_df.set_index(x_column)[y_column])
        except Exception as e:
            st.error(f"Plotting Error: {e}")
else:
    # Show this message if no file has been uploaded yet
    st.info("👈 Please upload a CSV file to get started.")
