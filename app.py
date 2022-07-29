import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **The Exploratory Data Analysis App**
This is the **Exploratory Data Analysis App** created in Streamlit using the **pandas-profiling** library.

''')

# Upload CSV data(Uploading of the CSV file)

with st.sidebar.header('1. Upload your CSV data'):
    uploaded_file = st.sidebar.file_uploader("Upload your input CSV file over here", type=["csv"])
    st.sidebar.markdown("""
[Sample CSV input file](https://github.com/SurajKH/Exploratory-Data-Analysis-Web-App/blob/main/heart.csv)
""")

# Pandas Profiling Report
# if user does not upload a csv file then they can use the Sample csv file.
if uploaded_file is not None:
    @st.cache
    #function to load the csv file
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    #generation of the Profile Report for the given datasets.
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file to be uploaded by the end user.')
    if st.button('Press to use Example Dataset'):
        # Example data
        @st.cache
        def load_data():
            a = pd.DataFrame(
                np.random.rand(100, 5),
                columns=['column1', 'column2', 'columns3', 'column4', 'column3']
            )
            return a
        #generation of the Dataframe
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input DataFrame**')
        st.write(df)
        st.header('**Pandas Profiling Report**')
        st_profile_report(pr)
