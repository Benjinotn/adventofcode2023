import requests
from bs4 import BeautifulSoup
import json

def get_variables():
    with open("variables.json") as json_data:
        d = json.load(json_data)
        json_data.close()

        if not d["year"]:
            raise ValueError('year in variables.json is missing!')
        
        if not d["cookie"]:
            raise ValueError('cookie in variables.json is missing!')

    return d

def get_text_input_from_file(file):
    f = open(file, 'r')
    text = f.read()
    f.close()
    return text

def get_puzzle_input_from_web(day):

    variables = get_variables()
    cookie = variables["cookie"]
    year = variables["year"]
    cookies = {'session': cookie}

    url = str("https://adventofcode.com/%s/day/%s/input" % (year, day))

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }

    r = requests.get(url, headers=headers, cookies=cookies)

    soup = BeautifulSoup(r.content, "html.parser")

    return soup
