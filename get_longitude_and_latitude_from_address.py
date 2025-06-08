import sys

from src.lib.csv_reader import CsvReader
from src.lib.geocodeapi import GeocodeAPi

def main(csv_file:str):
    geocode_api = GeocodeAPi()

    try:
        # CSVファイルを読み込みデータフレームを返す
        csv_reader = CsvReader(csv_file)
        df_csv = csv_reader._read_csv_to_dataframe()

        # データフレームの郵便番号からAPIで緯度、経度を調べる
        for index, value in enumerate(df_csv.values):
            if(value[1]):
                print(value[1])
                address = value[1]
                
                json = geocode_api.get_latitude_longitude(address)
                df_csv.iloc[index, 4] = json["results"][0]["location"]["latitude"]
                df_csv.iloc[index, 5] = json["results"][0]["location"]["longitude"]
        
        # CSVファイルに出力する
        df_csv.to_csv(csv_file)

    except Exception as e:
        print(e)



if __name__ == "__main__":
    # csv_file = "csv_folder/sample/address.csv"
    csv_file = sys.argv[1]
    main(csv_file)