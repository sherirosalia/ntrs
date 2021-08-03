import requests

# from urllib import urlencode
from urllib.parse import urlencode



class ntrs:
    def __init__(self):
        self.base_url = 'https://ntrs.nasa.gov/api/citations/'

    def search(self, q, fromPage):
        query = {
            "q": q,
            "page.size": 100,
            "page.from": fromPage
        }

        request = requests.get(self.base_url + "search?" + urlencode(query))
        print(self.base_url + "search?" + urlencode(query))
        data = request.json()

        return data