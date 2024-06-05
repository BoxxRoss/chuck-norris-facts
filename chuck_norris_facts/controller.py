"""
controller.py
made to connect to the chuck norris facts
"""
import requests

base_url = "https://api.chucknorris.io/jokes/random?category="



def grab_fact(category):
    url = base_url + category

    response = requests.get(url)
    if response.ok:
        results = response.json()["value"]
    else:
        results = response.json()["message"]
    return results

if __name__ == "__main__":

    response = grab_fact("animal")
    print(response)