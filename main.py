import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
sidebar=st.sidebar.selectbox('страницы',('lupa','zalupa'))

if sidebar=='lupa':
     st.write('Hello, *World!* :sunglasses:')
     st.header('st.button')
     but = st.button('ид')
     hut = st.button('и')
     if but:
          sidebar='zalupa'
          st.write('Why hello there')
     elif hut:
          st.write('Goodbye')
else:
     columns = st.columns(2)
     with columns[0]:
          st.metric('Сколько камней в кг', 72, 3)
     with columns[1]:
          st.metric('Сколько воды в л', 424, -6)
     df = pd.DataFrame(sns.load_dataset('iris'))
     st.write(df)
     '''
     fig, ax = plt.subplots()
     sns.scatterplot(x='sepal_length', y='sepal_width', data=data, ax=ax)
     st.write("График разброса:")
     st.pyplot(fig)'''

