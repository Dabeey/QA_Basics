import requests

URL = 'https://reqres.in/api'

def test_url():
    res = requests.get(URL + '/users')
    assert res.status_code == 200, f'Expected 200 as status code'
    print(f'Test passed: {res.status_code} received from {URL}')
    return res.json()


def test_api():
    res = requests.get(URL + '/users/4')
    assert res.json() is not None, 'Expected a JSON response'
    print(f'Test passed: JSON response received from {URL}')
    return res.json()


def test_login():
    payload = {
        "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }

    res = requests.post(URL + '/login',json=payload)
    assert res.status_code == 200, f'Expected 200 as status code'
    assert 'token' in res.json(), 'Expected a token in the response'
    data = res.json()
    print(f'Test passed: Login successful with token {data["token"]}')
    return data

