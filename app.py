import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Application Test :red[Streamlit]")
st.header(':blue[Analyse sur la base de données IRIS]')
st.subheader("👨🏾‍💻 Applications web")
st.text("Ma première application web avec Streamlit ! ")


# importer et nommé les colonnes du dataset
iris = pd.read_csv("IRIS.csv",header=None)
col1,col2 = st.columns(2)

iris.rename(columns={0:'longueur sepale',
                     1:'longueur sepale normalisé',
                     2:'largeur sepale',
                     3:'largeur sepale normalisé',
                     4:'longueur petale',
                     5:'longueur petale normalisé',
                     6:'largeur petale',
                     7:'largeur petale normalisé',
                     8:'espece'},inplace=True)
                     

st.text("Les statistiques et graphes  se sont basés sur la base de données IRIS")
st.write(iris)
st.header(":orange[Statistiques de l'ensemble]")

st.subheader("Distribution selon une caractéristique ")
option = st.selectbox("Choisissez la caractéristique à visualiser",("longueur sepale","longueur petale","largeur petale","largeur sepale"))
#initialiser une nouvelle figure pour eviter la superposition
plt.figure()
#histogramme
plt.title("Histogramme selon "+option)
sns.histplot(iris[option])
st.pyplot(plt)

st.divider()

st.subheader("Distribution a deux dimensions")
st.text("Distribution des points basé sur : ")

col1,col2 = st.columns(2)
with col1:
    #recuperer la caractéristique a affiché sur l'axe des abscisses
    st.radio("Abscisses (X)",options=["longueur sepale","longueur petale","largeur petale","largeur sepale"],key="x_key")

with col2:
    #recuperer la caractéristique a affiché sur l'axe des ordonnées
    st.radio("Ordonnées (Y)",options=["longueur sepale","longueur petale","largeur petale","largeur sepale"],key="y_key")

#nouvelle figure
plt.figure()
sns.scatterplot(data=iris,x=st.session_state.x_key,y=st.session_state.y_key,hue="espece")
st.pyplot(plt)
st.divider()
st.subheader("Auteur")
st.text("Ludel TOPANOU")
