from dotenv import load_dotenv
import os, requests, sys, time

# .envを読み込む
load_dotenv()

# 環境変数を取得する
api_key = os.getenv("API_KEY")

class GeocodeAPi:
    """GeocodeAPi
    
    Reference:
        https://developers.google.com/maps/documentation/geocoding/reference/rest/v4beta/geocode.address/geocodeAddress?hl=ja&_gl=1*11f1tbk*_up*MQ..*_ga*ODU4Mjk4ODI3LjE3NDkzNTU5MjU.*_ga_NRWSTWS78N*czE3NDkzNjY5MTIkbzMkZzAkdDE3NDkzNjY5MTIkajYwJGwwJGgw

    """
    def __init__(self):
        self._url = "https://geocode.googleapis.com/v4beta/geocode"
        self._key = api_key


    def get_latitude_longitude(self, address:str) ->dict:
        """緯度経度データを取得する

        Args:
            address(str): 住所

        Returns:
            json(dict): 緯度経度データ
        """
        delay_seconds = 0.5
        url = f"{self._url}/address"

        try:
            headers = {
                "Context-Type":"application/json"
            }
            params = {
                "key": self._key,
                "addressQuery": address
            }
            response = requests.get(url=url, headers=headers, params=params)
            if response.status_code == 200:
                json = response.json()
                time.sleep(delay_seconds)
                return json
            
        except Exception as e:
            print(self.__class__.__name__.__module__, e)


    def get_address(self, latitude:str, longitude:str) ->dict:
        """住所を取得する

        Args:
            latitude(str): 緯度データ
            longitude(str): 経度データ

        Returns:
            json(dict): 住所データ
        """
        delay_seconds = 0.5
        url = f"{self._url}/location/{latitude},{longitude}"
        try:
            headers = {
                "Context-Type":"application/json"
            }
            params = {
                "key": self._key,
            }
            response = requests.get(url=url, headers=headers, params=params)
            if response.status_code == 200:
                json = response.json()
                time.sleep(delay_seconds)
                return json["results"][0]

        except Exception as e:
            print(self.__class__.__name__.__module__, e)

# if __name__ == "__main__":
#     geocode_api = GeocodeAPi()
    # geocode_api.get_latitude_longitude("東京都港区芝公園４丁目２－８")
    # geocode_api.get_latitude_longitude(sys.argv[1])
    # print(geocode_api.get_address("35.6585696","139.745484"))