import requests
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('API_URL')

def test_url():
    res = requests.get(URL + '/users')
    assert res.status_code == 200, f'Expected 200 as status code'
    print(f'Test passed: {res.status_code} received from {URL}')
    data = res.json()
    assert isinstance(data, dict), 'Expected a JSON response'
    assert 'data' in data, 'Expected "data" key in the response'
    return data


def test_api():
    res = requests.get(URL + '/users/4')
    assert res.json() is not None, 'Expected a JSON response'
    print(f'Test passed: JSON response received from {URL}')
    data = res.json()
    assert isinstance(data, dict), 'Expected a JSON response'
    # assert 'data' in data, 'Expected "data" key in the response'
    return data


def test_login():
    payload = {
        "email": "eve.holt@reqres.in",
    "password": "cityslicka"
    }

    res = requests.post(URL + '/login',json=payload,
                        headers={'x-api-key': os.getenv('X_API_KEY')})
    print(f'Status Code: {res.status_code}')
    assert res.status_code == 200, f'Expected 200 as status code'
    assert 'token' in res.json(), 'Expected a token in the response'
    data = res.json()
    print(f'Test passed: Login successful with token {data["token"]}')
    return data

if __name__ == '__main__':
    print('Running API tests...')
    test_url()
    test_api()
    test_login()
    print('All tests completed successfully.')