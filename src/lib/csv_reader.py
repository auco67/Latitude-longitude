import pandas as pd

class CsvReader:
    """CSVファイルを読み取るクラス"""

    def __init__(self, csv_file:str):
        self._csv_file = csv_file


    def _read_csv_to_dataframe(self) -> pd.DataFrame:
        """CSVファイルを読み込みデータフレームに変換する

        Returns:
            df_csv(pd.DataFrame): データフレーム
        """
        csv_file = self._csv_file
        df_csv = pd.read_csv(csv_file).fillna('')
        return df_csv