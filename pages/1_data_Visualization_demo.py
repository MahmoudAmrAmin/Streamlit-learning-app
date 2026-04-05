import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import plotly.express as px 
# Save data in cach

@st.cache_data
def load_data(file) : 
    return pd.read_csv(file)

# create file uploader component 

file = st.file_uploader(label='Upload CSV file' ,  type=['csv' , 'pdf']) 

if file is not None : 
    df = load_data(file)
    # slider element 
    n_rows = st.slider("set number of rows you need:", 
                       min_value=5,
                       max_value=df.shape[0],
                       step= 1)
    # multi select element  
    columns = st.multiselect(label="Select columns you want" , options=df.columns.to_list() , default=df.columns.to_list())

    # show table from dataframe 
    st.write(df[:n_rows][columns])

    """
        make visualization with plotly 
        and make user choose columns of x and y axis  

        component select box for ====>choose column 
        plotly figure to visualize scatter plot 

    
    """
    tab1 , tab2 = st.tabs(['Scatter Plot' , 'Histogram Plot'])


    with tab1:
        col1 , col2 , col3 = st.columns(3)
        with col1 : 
            X_column = st.selectbox('Choose X-axis Column' ,df.select_dtypes(exclude='object').columns.to_list() )
        with col2 : 
            y_column = st.selectbox('Choose y-axis Column' , df.select_dtypes(exclude='object').columns.to_list())
        with col3 : 
            color = st.selectbox('Select column to be color: ' , df.columns.to_list())

        # to lets create scatter plot 
        figure_scatter = px.scatter(df , x = X_column , y = y_column ,color=color )

        st.plotly_chart(figure_scatter)
    

   
    with tab2:
        """
           now list create histogram plot and set it in another tap 
        """
        num_columns_hist = df.select_dtypes('number').columns.to_list() 
        X_column_hist = st.selectbox("select column to make histogram plot" , num_columns_hist)
        fig_hist = px.histogram(df , x = X_column_hist) 
        st.plotly_chart(fig_hist)
