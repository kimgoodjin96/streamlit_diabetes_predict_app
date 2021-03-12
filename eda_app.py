import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import h5py
import tensorflow as tf
import tensorflow.keras
from sklearn.model_selection import train_test_split

def run_eda_app():
    st.subheader('EDA 화면입니다.')
    dia_df=pd.read_csv('data/diabetes.csv')

    radio_menu=['데이터프레임','통계치']
    selected_radio=st.radio('선택하세요',radio_menu)
    
    if selected_radio=='데이터프레임':
        st.dataframe(dia_df)
    
    elif selected_radio=='통계치':
        st.dataframe(dia_df.describe())

    columns=dia_df.columns
    columns=list(columns)
    selected_columns=st.multiselect('보고싶은 컬럼을 선택하세요',columns)
    if selected_columns:
        st.dataframe(dia_df[selected_columns])

    dia_corr=dia_df.columns
    selected_corr=st.multiselect('상관계수를 보고싶은 컬럼을 선택하세요',dia_corr)
    if len(selected_corr)!=0:
        st.dataframe(dia_df[selected_corr].corr())

        st.pyplot(sns.pairplot(dia_df[selected_corr]))
    
    else:
        st.write('선택한 컬럼이 없습니다.')

    




if __name__=='__main__':
    main()