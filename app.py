import streamlit as st
import pandas as pd
import os
from tempfile import TemporaryDirectory
from connection_utils import CustomConnection


def main():
    st.title('Data Visualizer App')

    # File upload and connection setup
    uploaded_file = st.file_uploader(
        'Upload any CSV, JSON or XLSX file', type=['csv', 'json', 'xlsx'])
    if uploaded_file:
        # Get the data format (csv, json, xlsx)
        data_format = uploaded_file.type.split('/')[-1]

        # Create a temporary directory to save the uploaded file
        with TemporaryDirectory() as tmpdirname:
            filepath = os.path.join(tmpdirname, uploaded_file.name)

            # Save the uploaded file in the temporary directory
            with open(filepath, 'wb') as f:
                f.write(uploaded_file.getvalue())
                
             # Connect to CSV,JSON,XLSX database using the custom connection
            conn = st.experimental_connection(
                'custom_connection', type=CustomConnection, filepath=filepath, data_format=data_format)
            df = conn._connect(filepath=filepath, data_format=data_format)

            # Display the data
            st.subheader('Data Preview')
            st.dataframe(df)


if __name__ == '__main__':
    main()
