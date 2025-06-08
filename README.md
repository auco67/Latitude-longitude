# Latitude-longitude

住所または郵便番号から経度緯度データは取得することが可能。

住所から取得する`get_longitude_and_latitude_from_address.py`と郵便番号から取得する`get_longitude_and_latitude_from_zip_code.py`の２つのスクリプトを用意した

## 住所から緯度経度データを取得する

### get_longitude_and_latitude_from_address.py

住所から経度、緯度を取得するツール

※緯度経度データは、[Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview?hl=ja)の[geocode.address.geocodeAddress](https://developers.google.com/maps/documentation/geocoding/reference/rest/v4beta/geocode.address/geocodeAddress?hl=ja&_gl=1*11f1tbk*_up*MQ..*_ga*ODU4Mjk4ODI3LjE3NDkzNTU5MjU.*_ga_NRWSTWS78N*czE3NDkzNjY5MTIkbzMkZzAkdDE3NDkzNjY5MTIkajYwJGwwJGgw)を使用して取得する。

### 前提作業

Google Cloud プロジェクトをセットアップする

1. プロジェクトを作成する
2. 課金を有効にする（従量課金モデル）

    [Google Maps Platform コアサービスの料金リスト](https://developers.google.com/maps/billing-and-pricing/pricing?hl=ja&_gl=1*8kirx1*_up*MQ..*_ga*MjE1Mjk4MTY1LjE3NDkzNjcwNzc.*_ga_NRWSTWS78N*czE3NDkzNjcwNzckbzEkZzEkdDE3NDkzNjcyMTEkajEkbDAkaDA.#map-loads-pricing)を参照

3. API を有効にしAPIキーを取得する
4. API キーの制限する

### 使用方法（Windowsの場合）

1. githubからリポジトリをgit cloneする
    ```
    git clone https://github.com/auco67/Latitude-longitude.git
    ```

2. csvファイルを格納するフォルダ`csv_folder`を作成しCSVファイルを格納する
    ```
    latitude-longitude
    ├─csv_folder
    |  ├─sample
    |  |  ├─address.csv 
    ```

    CSVファイルの項目構成は次の通り

    |No|住所１|住所２|郵便番号|緯度|経度|
    |--|--|--|--|--|--|
    |1|東京都港区芝公園４丁目２－８||||

3. from_address.batを実行する

    from_address.batの中身
    ```
    cd dist
    get_longitude_and_latitude_from_address.exe "../csv_folder/address.csv"
    pause
    ```

    ※フォルダ名が`csv_folder`以外にする場合は、`main.bat`の中身も修正する必要がある

    ※数件のデータの場合長時間掛かる

    実行後は、同じCSVファイル名で上書きされる

## 郵便番号から緯度経度データを取得する

### get_longitude_and_latitude_from_zip_code.py

7桁の郵便番号から経度、緯度を取得するツール

緯度経度データは、[GeoApi](https://geoapi.heartrails.com/)を使用して取得する。APIは、[郵便番号による住所検索API](https://geoapi.heartrails.com/api.html#postal)を使用した

### 前提作業

郵便局のサイトの[住所の郵便番号（1レコード1行、UTF-8形式）（CSV形式）](https://www.post.japanpost.jp/zipcode/dl/utf-zip.html)から最新の全国の郵便番号一覧CSVを入手する

※データが膨大であるため、必要な都道府県を絞り、郵便番号のCSVファイルを用意する

例）東京都で絞ると郵便番号は4,106件（不要な郵便番号を除いた）

### 使用方法（Windowsの場合）

1. githubからリポジトリをgit cloneする
    ```
    git clone https://github.com/auco67/Latitude-longitude.git
    ```

2. csvファイルを格納するフォルダ`csv_folder`を作成しCSVファイルを格納する
    ```
    latitude-longitude
    ├─csv_folder
    |  ├─sample
    |  |  ├─postal.csv
    ```

    CSVファイルの項目構成は次の通り

    |No|住所１|住所２|郵便番号|緯度|経度|
    |--|--|--|--|--|--|
    |1|千代田区|飯田橋|1020072|||

3. from_zip_code.batを実行する

    from_zip_code.batの中身
    ```
    cd dist
    get_longitude_and_latitude_from_zip_code.exe "../csv_folder"
    pause
    ```

    ※フォルダ名が`csv_folder`以外にする場合は、`main.bat`の中身も修正する必要がある

    ※数件のデータの場合長時間掛かる

    実行後は、同じCSVファイル名で上書きされる