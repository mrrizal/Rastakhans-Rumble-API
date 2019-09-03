import json
import requests


def get_card_info():
    # function for get card information and save it to json file
    headers = {
        'X-Mashape-Key': 'ZTMJtzbYvXmshPTFEZI4ztIy3I68p1nPwgHjsnIGukKZeJxGcs'
    }
    url = 'https://omgvamp-hearthstone-v1.p.mashape.com/cards/sets/Rastakhan%27s%20Rumble'
    r = requests.get(url, headers=headers)
    data = r.json()
    with open('card_info.json', 'w') as f:
        for i in data:
            f.write(json.dumps(i))
            f.write('\n')


if __name__ == '__main__':
    get_card_info()
