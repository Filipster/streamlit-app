import streamlit as st
from joblib import load
import pandas as pd
import numpy as np
from PIL import Image
from scipy.stats import halfnorm


#Front-end development

st.title('Matchmaking Software - LALA')

st.header("Faça o match entre o alumni e o estágio ideal")
st.write("Os request's são feitos através da base de dados atualizada do mês 11")

#carregando a imagem
image = Image.open('LatinAmericanLeadershipAcademy.png')

st.image(image, caption ='LALA')

#criando um perfil proveniente dos dados
df = pd.read_csv('MATCHING - 2ND SEASON LALA Career Internship.csv')
new_profile = pd.DataFrame(columns=df.columns, index=[df.index[-1]+1])

#new_profile['Bios'] = st.text_input("Faça upload da descrição interessada: ")

# Printando alguns exemplos para o usuario
#example_bios()
option = st.selectbox(
...     'How would you like to be contacted?',
...     ('Email', 'Home phone', 'Mobile phone'))
>>>
>>> st.write('You selected:', option)


# Entrando os valores input
