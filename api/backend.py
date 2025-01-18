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