import requests

RANDOM_JOKE_URL="http://api.icndb.com/jokes/random"

def get_random_chuck_joke():
    try:
        r = requests.get(RANDOM_JOKE_URL)
        return r.json()['value']['joke']
    except:
        return "Sorry, can't get a joke right now!"