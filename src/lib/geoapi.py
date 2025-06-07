import requests
import time

class GeoApi:
    """Geo Api"""
    def __init__(self):
        self._url = "https://geoapi.heartrails.com/api/json?method=searchByPostal"

    def get_town_area_info_json(self, postal:str)->dict:
        delay_seconds = 0.5

        try:
            headers = {
                "Context-Type":"application/json"
            }
            params = {
                "method":"searchByPostal",
                "postal": str(postal).zfill(7)
            }
            response = requests.get(url=self._url, headers=headers, params=params)
            if response.status_code == 200:
                json = response.json()
                # x = json["response"]["location"][0]["x"]
                # y = json["response"]["location"][0]["y"]
                time.sleep(delay_seconds)
                return json

        except Exception as e:
            print(self.__class__.__name__, e)


if __name__ == "__main__":
    geoapi = GeoApi()
    geoapi.get_town_area_info_list("0640941")


