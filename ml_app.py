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
import joblib


def run_ml_app():
    model=joblib.load('data/best_model.pkl')
    df=pd.read_csv('data/diabetes.csv')
    st.dataframe(df)

    new_data=np.array([3,88,58,11,54,24,0.26,22])
    new_data=new_data.reshape(1,-1)
    print(new_data)

    st.write(model.predict(new_data))



if __name__=='__main__':
    main()