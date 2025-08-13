import streamlit as st
import pandas as pd
import joblib

# Carregar o modelo treinado
try:
    model = joblib.load('modelo_decision_match_ai.joblib')
except FileNotFoundError:
    st.error("Arquivo do modelo 'modelo_decision_match_ai.joblib' não encontrado.")
    st.stop()

# --- Interface do Usuário ---
st.set_page_config(page_title="Decision Match AI", page_icon="🤖", layout="wide")

st.title('🤖 Decision Match AI')
st.subheader('MVP para Recomendação Inteligente de Candidatos')
st.write("""
Esta aplicação demonstra o funcionamento do modelo de IA para prever a compatibilidade
entre um candidato e uma vaga. Insira os valores das features abaixo para testar.
""")

st.sidebar.header('Parâmetros de Entrada')

def user_input_features():
    """Coleta os inputs do usuário pela sidebar."""
    similaridade = st.sidebar.slider('Score de Similaridade de Texto (CV vs Vaga)', 0.0, 1.0, 0.5, 0.01)
    match_ingles = st.sidebar.selectbox('Candidato atende ao requisito de Inglês?', (1, 0), help="1 = Sim, 0 = Não")
    match_sap = st.sidebar.selectbox('Candidato atende ao requisito de SAP?', (1, 0), help="1 = Sim, 0 = Não")

    data = {
        'similaridade_texto': similaridade,
        'match_nivel_ingles': match_ingles,
        'match_sap': match_sap
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('Features Inseridas:')
st.write(input_df)

if st.button('Calcular Compatibilidade'):
    prediction_proba = model.predict_proba(input_df)
    compatibility_score = prediction_proba[0][1] * 100

    st.subheader('Resultado da Análise de IA:')
    st.write(f"A probabilidade deste candidato ser um **Match** para a vaga é de:")
    
    st.progress(int(compatibility_score))
    st.markdown(f"<h2 style='text-align: center; color: #28a745;'>{compatibility_score:.2f}%</h2>", unsafe_allow_html=True)

st.write("---")
st.write("Projeto desenvolvido para o Datathon - Desafio Decision.")