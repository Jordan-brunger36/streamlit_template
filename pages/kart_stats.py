import streamlit as st
import pandas as pd

st.markdown("# Kart Configurations 🏎️")
st.sidebar.markdown("# Kart Configurations 🏎️")

st.write("What Kart Configuration is Best?")

df_kart = pd.read_csv('data/kart_stats.csv')

st.dataframe(df_kart)

#x = st.slider('How many racers to show',1,len(df_kart))
df_kart_less_columns = df_kart[['Body','Weight','Acceleration','On-Road traction','Off-Road Traction','Mini-Turbo']].sort_values('Body',ascending=False)#.iloc[0:x]
st.dataframe(df_kart_less_columns.style
            .highlight_max(color='lightgreen', axis=0,subset=['Weight','Acceleration','On-Road traction','Off-Road Traction','Mini-Turbo'])
            .highlight_min(color='red', axis=0,subset=['Weight','Acceleration','On-Road traction','Off-Road Traction','Mini-Turbo'])
)

st.area_chart(df_kart_less_columns, x='Weight', y=['On-Road traction','Off-Road Traction'])

st.bar_chart(df_kart_less_columns,x='Weight', y='Acceleration')

chosen_kart = st.selectbox('Pick a Kart', df_kart['Body'])

df_single_kart = df_kart.loc[df_kart['Body'] == chosen_kart]

df_single_kart = df_single_kart.drop(columns=['Body'])

df_unp_kart = df_single_kart.unstack().rename_axis(['category','row number']).reset_index().drop(columns='row number').rename({0:'strength'}, axis=1)
                                     
st.bar_chart(df_unp_kart, x='category', y='strength')
