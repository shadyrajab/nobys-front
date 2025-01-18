import streamlit as st
from api.backend import create_account

st.markdown("""
    ## Funcionamento inicial do Back-End do Nobys-App
            
    Essa Interface inicial serve apenas para mostrar o funcionamento do aplicativo
    e validação das regras de negócio do projeto.
            
    Acreditamos que com uma amostragem visual, será mais fácil visualizar o futuro comportamento
    do projeto e expandir a mente para novas ideias.
    
    Como é apenas uma demonstração, não nos preocupamos com a interatividade da interface em si, e sim
    com o funcionamento do Back-End.
    
    A interface servirá para testes de escritas e consultas no banco de dados na empresa. 
""")

st.markdown("""
    ---
    ## Testando o fluxo inicial para criar conta, fazer login e troca de senha
""")
create_accont = st.expander("Criar Conta")
with create_accont.form("Create Account"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    crm = st.text_input("CRM")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = create_account(username, email, crm, password)

        st.success(response)

login = st.expander("Login")
with login.form("Login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        print(username, password)