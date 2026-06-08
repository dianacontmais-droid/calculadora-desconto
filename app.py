import streamlit as st

# Configuração da página
st.set_page_config(page_title="Calculadora de Desconto", page_icon="💰")

st.title("💰 Calculadora de Desconto")
st.write("Insira os valores abaixo para calcular o preço final.")

# Campos onde o usuário vai digitar
preco = st.number_input("Preço da Mercadoria (R$):", min_value=0.0, value=1000.00, step=10.0)
percentual = st.number_input("Percentual de Desconto (%):", min_value=0.0, max_value=100.0, value=25.0, step=1.0)

# Cálculo
valor_desconto = preco * (percentual / 100)
preco_a_pagar = preco - valor_desconto

# Mostrando o resultado formatado
st.divider()
st.subheader("Resultado:")
st.write(f"**Valor do desconto:** R$ {valor_desconto:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ','))
st.write(f"**Preço a pagar:** R$ {preco_a_pagar:,.2f}".replace('.', 'X').replace(',', '.').replace('X', ','))
