import streamlit as st
import streamlit as st
import pandas as pd
#import matplotlib.pyplot as plt
#import plotly.express as px
file_path="./data/data.xlsx"
ex2=pd.read_excel(file_path)

df0=pd.DataFrame(ex2).dropna()
newheader=df0.iloc[0].tolist()
df0=df0[1:]
df0.columns=newheader 

st.set_page_config(
    page_title="estadisticas",
    page_icon="📊",
    layout="wide"
)

st.title("Comportamiento de los usuarios")
st.markdown("permite conocer datos sobre las interacciones en el chat")

st.write("Porcentaje de interacción positivos vs negativos")

df1=df0.groupby("User")[["positivos","negativos"]].sum()

""""
En esta linea de codigo se llevara a cabo la grafica positivos vs negativos
"""
st.bar_chart(df1, stack=False)

#en este apartado se muestra la tabla de datos
st.dataframe(
    df1
)

st.write("tiempo promedio de respuesta")

df2=df0.groupby("User")["TR"].mean()
st.bar_chart(df2, horizontal=True)
st.dataframe(df2)


st.write("Registro total de interacciónes")


st.dataframe(df0)
#Datos consolidados

dfpositivo=int(df0["positivos"].sum())
dfnegativo=int(df0["negativos"].sum())



col1,col2,col3=st.columns(3)

with col1: 
    st.header("Interacciones Positivas")
    st.subheader(dfpositivo)

with col2:
    st.header("Interacciones negativas")
    st.subheader(dfnegativo)

with col3:
    st.header("Total de interacciones")
    st.subheader(int(dfpositivo+dfnegativo))
