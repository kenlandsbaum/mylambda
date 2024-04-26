import requests

def make_get_request(url: str):
    try:
        res = requests.get(url=url)
        return res.json()
    except Exception as ex:
        return {"error": ex}