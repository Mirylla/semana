# -*- coding: utf-8 -*-
# +
import altair as alt
import math
import os
import pandas as pd
import numpy as np  # np mean, np random
import streamlit as st  # 🎈 data web app development
import matplotlib.pyplot as plt
import plotly.figure_factory as ff

import matplotlib.lines as mlines
import matplotlib.patches as mpatches

# %matplotlib inline
# -

st.set_page_config(
    page_title="German Loans & Credit Rating",
    page_icon="Loan",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/library/api-reference',
        'About': "This app shows the main statistics about the loans of german"
    }
)


#DataFrame=pd.read_csv("./loan.csv", sep=";")
# Define function that loads the data and obtain new variables
@st.cache()
def load_data(nrows):
    working_directory = os.getcwd()
    filename = '\OneDrive\\Documentos\\MASTER_BIG_DATA\\Vodafone_Elena_Abril\\loan.csv'
    data_df = pd.read_csv(working_directory + filename,
                          delimiter=";")

    return data_df


st.title("Load of german")

data_load_state = st.text("Loading data...")
raw_df = load_data(10)

# +
page = st.sidebar.selectbox('Choose your page', ['Page 1', 'Page 2"', 'Page 3'])

# Create a page dropdown 
page = st.selectbox("Menu", ["Page 1", "Page 2", "Page 3"]) 

if page == 'Page 1':

    # Obtain global variables
    num_housing = raw_df['Housing'].nunique()
    num_loan = raw_df['Loan Duration'].nunique()
    min_value = math.floor(raw_df.Age.min())
    max_value = math.ceil(raw_df.Age.max())
    # Main variables
    column1, column2, _ = st.columns([1, 1, 2])
    column1.metric("Housing:", num_housing, +10)
    column2.metric("Teams:", num_loan, '-1%')
    # Sidebar for the filters
    st.sidebar.markdown("# Filters")
    teams_selected = st.sidebar.multiselect(
    'Select team:',
    raw_df.Housing.unique())
    
elif page == 'Page 2':
    st.title("Load of german2")
    #Bar Chart
    st.bar_chart(raw_df['Purpose of Loan'])
elif page == 'Page 3':
    st.title("Load of german3")
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #histogram
    df = pd.DataFrame(raw_df[:200], columns = ['Loan Amount'])
    df.hist()
    plt.show()
    st.pyplot()


# -

#DataFrame=pd.read_csv("./loan.csv", sep=";")
# Define function that loads the data and obtain new variables
@st.cache()
def load_data(nrows):
    working_directory = os.getcwd()
    filename = '\OneDrive\\Documentos\\MASTER_BIG_DATA\\Vodafone_Elena_Abril\\loan.csv'
    data_df = pd.read_csv(working_directory + filename,
                          delimiter=";")

    return data_df


# +
# Notify the reader that the data was successfully loaded.
#data_load_state.text("Loading data...done!")

# +
# Title to show the plots

# Show table
with st.expander("Expand to see data sample"):
    st.markdown("## Data")
    st.dataframe(raw_df.head(3))

# +
#plt.scatter(raw_df['Loan Amount'],raw_df["Age"])
#plt.figure()

# +

#figura = plt.figure(1)
#ejes = figura.add_subplot(111)
#ejes.hist([raw_df.Age],bins = 30, density = True, histtype='bar',rwidth=0.8,color=['blue'],label=["Exponencial"])




# +
#raw_df["Age"].plot.hist(alpha=0.5, color='y')
#plt.xlabel(col)
#plt.title(col)
#plt.show()
# -


