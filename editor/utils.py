import requests

def grammar_check(text):
    response = requests.post("https://api.languagetoolplus.com/v2/check", data={
        "text": text,
        "language": "en-US"
    })
    return response.json()
