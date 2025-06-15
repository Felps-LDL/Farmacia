import streamlit as st

st.set_page_config(page_title="Diluição de Solução", layout="centered")

st.title("💉 Cálculo de Diluição para Grupos de Animais")
st.write("Esta aplicação calcula o volume necessário de solução com base nos pesos dos grupos de animais.")

# Entrada de número de grupos
qtd_grupos = st.number_input("Quantos grupos?", min_value=1, step=1)
concentracao = st.number_input("Concentração?", min_value=1.0, value=25.0)

# Coletando os pesos
peso_animais = []
grupos_ml = []

# Ordenar
ordem = []

with st.form("formulario_pesos"):
    st.subheader("Informe o peso de cada grupo (em gramas):")
    for i in range(qtd_grupos):
        peso = st.number_input(f"Peso do Grupo {i+1}", min_value=1.0, key=f"peso_{i}")
        peso_animais.append(peso)
        grupos_ml.append(peso / 100)

    submitted = st.form_submit_button("Calcular")

def quanto_precisa(i):
    if i >= qtd_grupos:
        return 0
    
    resultado = grupos_ml[i] + quanto_precisa(i + 1)
    
    if i != 0:
        ordem.append(resultado / 2)
        #st.write(f"💧 Grupo {i + 1}: {resultado / 2:.2f} mL de água")
    return resultado / 2

if submitted:
    st.success("Cálculo realizado com sucesso!")
    st.write("### Pesos dos grupos:")
    st.write(peso_animais)

    st.write("### Volume (em mL) por grupo:")
    ml_primeiro = quanto_precisa(0) * 2

    st.write(f"💊 **Massa de substância VII:** {(ml_primeiro / 10 * 25):.4f} mg")
    st.write(f"🧪 **Grupo 1:** {ml_primeiro:.2f} mL [{concentracao} mg/kg]")

    temp = concentracao

    for i in range(qtd_grupos - 2, -1, -1): 
        temp /= 2
        st.write(f"💧 **Grupo {qtd_grupos - i}:** {ordem[i]:.2f} mL de diluente + {ordem[i]:.2f} mL de G{qtd_grupos - i - 1} = {(ordem[i] * 2):.2f} mL [{temp} mg/kg]")