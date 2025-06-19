import sys

from src.lib.csv_reader import CsvReader
from src.lib.geocodeapi import GeocodeAPi

def main(csv_file:str):
    geocode_api = GeocodeAPi()

    try:
        # CSVファイルを読み込みデータフレームを返す
        csv_reader = CsvReader(csv_file)
        df_csv = csv_reader._read_csv_to_dataframe()

        # データフレームの緯度経度からAPIで住所を調べる
        for index, value in enumerate(df_csv.values):
            latitude = str(value[4])
            longitude = str(value[5])
            if(latitude and longitude):
                print(latitude, longitude)
                json = geocode_api.get_address(latitude,longitude)

                if "formattedAddress" in json and json["formattedAddress"]:
                    df_csv.iloc[index, 1] = str(json["formattedAddress"]).replace("日本、〒","")[9:]
                if "postalAddress" in json and json["postalAddress"]:
                    if "postalCode" in json["postalAddress"]:
                        df_csv.iloc[index, 3] = str(json["postalAddress"]["postalCode"]).replace("-","")
        
        # CSVファイルに出力する
        df_csv.to_csv(csv_file)

    except Exception as e:
        print(e)

if __name__ == "__main__":
    csv_file = "csv_folder/sample/location.csv"
    # csv_file = sys.argv[1]
    main(csv_file)