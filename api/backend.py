import requests

def create_account(username, email, crm, password):
    url = "http://127.0.0.1:8000/v1/register/"
    data = {
        "username": username,
        "email": email,
        "crm": crm,
        "password": password
    }

    response = requests.post(url, json=data)
    return response.text


def make_login(username, password):
    url = "http://127.0.0.1:8000/v1/login/"
    data = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=data)
    return {
        "status": response.status_code,
        "text": response.text
    }

def create_hospital(name, address, phone, email):
    url = "http://127.0.0.1:8000/v1/hospitals/"
    data = {
        "name": name,
        "address": address,
        "phone": phone,
        "email": email
    }

    response = requests.post(url, json=data)
    return {
        "status": response.status_code,
        "text": response.text
    }

def get_hospitals():
    url = "http://127.0.0.1:8000/v1/hospitals/"
    response = requests.get(url)
    return {
        "status": response.status_code,
        "text": response.text
    }

def add_schedule(user_id, date, time, patient, age, value, description):
    url = "http://127.0.0.1:8000/v1/schedules/"
    data = {
        "date": date,
        "time": time,
        "patient": patient,
        "age": age,
        "value": value,
        "description": description
    }

    params = {
        "user_id": user_id
    }

    response = requests.post(url, json=data, params=params)
    return {
        "status": response.status_code,
        "text": response.text
    }


def get_schedules(user_id):
    url = "http://127.0.0.1:8000/v1/schedules/"
    params = {
        "user_id": user_id
    }
    response = requests.get(url, params=params)
    return {
        "status": response.status_code,
        "text": response.text
    }