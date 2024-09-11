import streamlit as st
from datetime import datetime, time

def main():
    st.title("Sistema de CRM")
    email = st.text_input("Campo de texto para email")
    data = st.date_input("Campo de data", datetime.now())
    hora = st.time_input("Seleção da hora", value=time(9,0))
    valor = st.number_input("Valor da Venda")
    quantidade = st.number_input("quantidade de produtos")
    produto = st.selectbox("Tipo de produto", ["Gemini", "Chatgpt", "Llama"])
    
    if st.button("Salvar"):
        data_hora = datetime.combine(data, hora)
        st.write("**Dados da venda**")
        st.write(f"Email do vendedor : {email}")
        
    
    
    
if __name__ == "__main__":
    main()