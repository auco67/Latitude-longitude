from pathlib import Path
import sys

from src.lib.csv_reader import CsvReader
from src.lib.geoapi import GeoApi

def main(csv_folder:Path):

    # GEO API
    geoapi = GeoApi()

    try:
        # フォルダからCSVファイルを抽出する
        files = csv_folder.glob("*.csv")

        # CSVファイル毎繰り返す
        for file in files:
            # CSVファイルを読み込みデータフレームを返す
            csv_reader = CsvReader(file)
            df_csv = csv_reader._read_csv_to_dataframe()

            # データフレームの郵便番号からAPIで緯度、経度を調べる
            for index, value in enumerate(df_csv.values):
                print(value[1], value[2])

                if(value[3]):
                    postal = value[3]
                    
                    json = geoapi.get_town_area_info_json(postal)
                    df_csv.iloc[index, 5] = json["response"]["location"][0]["x"]
                    df_csv.iloc[index, 4] = json["response"]["location"][0]["y"]
            
            # CSVファイルに出力する
            df_csv.to_csv(file)

    except Exception as e:
        print(e)
    
if __name__ == "__main__":
    # csv_folder = Path("data/csv")
    csv_folder = Path(sys.argv[1])
    main(csv_folder)