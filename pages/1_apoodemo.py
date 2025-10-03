import streamlit as st
import pandas as pd
import plotly.express as px


st.header("data analysis")
file= st.file_uploader("upload file in csv only ",type=["csv"])
if file is not None:
    df = pd.read_csv(file)
    n_rows=st.slider("choose num of rows to display",min_value=1,max_value=len(df),step=1)
    show_me=st.multiselect("select columns ",df.columns.to_list(),default=df.columns.to_list())
    st.write(df[:n_rows][show_me])
    col1,col2=st.columns(2)
    with col1:
        x_col =st.selectbox("select x axis",df.columns.to_list())
    with col2:
        y_col = st.selectbox("select y axis",df.columns.to_list())
    fig = px.scatter(df, x=x_col, y=y_col)


    st.plotly_chart(fig)