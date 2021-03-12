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
from eda_app import run_eda_app
from ml_app import run_ml_app


def main():
    st.title('당뇨병 예측')
    menu=['Home','Eda','Ml']
    choice=st.sidebar.selectbox('Menu',menu)
    if choice=='Home':
        st.write('당뇨병 예측 프로그램입니다.')
    elif choice=='Eda':
        run_eda_app()
    elif choice=='Ml':
        run_ml_app()

        
    


if __name__=='__main__':
    main()