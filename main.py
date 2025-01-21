import streamlit as st
from api.backend import create_account, make_login, create_hospital, get_hospitals, add_schedule, get_schedules
import pandas as pd
import json

if "user_id" not in st.session_state:
    st.session_state["user_id"] = None

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
create_accont = st.expander("POST Criar Conta")
with create_accont.form("Create Account"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    crm = st.text_input("CRM")
    password = st.text_input("Password", type="password")
    gender = st.selectbox("Gender", ("male", "female", "other"))
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = create_account(username, email, crm, password, gender)

        st.success(response)

login = st.expander("POST Login")
with login.form("Login"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = make_login(username, password)

        st.success(response)
        content = json.loads(response["text"])  
        st.session_state["user_id"] = content["user"]["user_id"]

st.markdown("""
    ---
    ## Testando o fluxo para registro e listagem dos hospitais.
    A ideia é fazer com que apenas um admin possa fazer o cadastro.
    Mas por enquanto, como é apenas uma demonstração, qualquer usuário pode fazer o cadastro.
"""
            )
hospitals = st.expander("POST Hospitais")
with hospitals.form("Hospitais"):
    name = st.text_input("Name")
    address = st.text_input("Address")
    phone = st.text_input("Phone")
    email = st.text_input("Email")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = create_hospital(name, address, phone, email)
        st.success(response)

get_hospitais = st.expander("GET Hospitais")

with get_hospitais.form("GET Hospitais"):
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = get_hospitals()
        content = json.loads(response["text"])

        df = pd.DataFrame(content["hospitals"])
        st.dataframe(df, hide_index=True)


st.markdown("""
    ---
    ## Testando o fluxo para agendamento de consulta
""")

schedule = st.expander("POST Schedule")
with schedule.form("Schedule"):
    start_date = st.date_input("Data de Início")
    end_date = st.date_input("Data de Fim")
    specialty = st.text_input("Especialidade")
    value = st.text_input("Value")
    description = st.text_input("Description")

    submit_button = st.form_submit_button("Submit")
    if submit_button:
        response = add_schedule(
            st.session_state["user_id"], 
            start_date, 
            end_date, 
            specialty, 
            value, 
            description
        )
        st.success(response)

get_schedule = st.expander("GET Schedules")
with get_schedule.form("GET Schedule"):
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        response = get_schedules(st.session_state["user_id"])
        content = json.loads(response["text"])

        df = pd.DataFrame(content["schedules"])
        st.dataframe(df, hide_index=True)