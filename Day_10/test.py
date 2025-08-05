import requests

URL = ''

def test_url():
    res = requests.get(URL)
    assert res.status