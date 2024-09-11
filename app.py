import streamlit as st
from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
from database import salvar_no_postgres


def main():
    st.title("Sistema de CRM")
    email = st.text_input("Campo de texto para email")
    data = st.date_input("Campo de data", datetime.now())
    hora = st.time_input("Seleção da hora", value=time(9,0))
    valor = st.number_input("Valor da Venda")
    quantidade = st.number_input("quantidade de produtos")
    produto = st.selectbox("Tipo de produto", ["Gemini", "GPT", "Llama"])
    
    if st.button("Salvar"):
        try:
            data_hora = datetime.combine(data, hora)
            venda = Vendas(
                email = email,
                data = data_hora,
                valor = valor,
                quantidade = quantidade,
                produto = produto
                )
            st.write(venda)
            salvar_no_postgres(venda)
        except ValidationError as e:
            st.error(f"deu erro{e}")
            
 
        
    
    
    
if __name__ == "__main__":
    main()