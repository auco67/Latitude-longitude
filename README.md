# Latitude-longitude

住所または郵便番号から経度緯度データは取得することが可能。

住所から取得する`get_longitude_and_latitude_from_address.py`と郵便番号から取得する`get_longitude_and_latitude_from_zip_code.py`の２つのスクリプトを用意した

## 前提作業

Google Cloud プロジェクトをセットアップする

1. プロジェクトを作成する
2. 課金を有効にする（従量課金モデル）

    [Google Maps Platform コアサービスの料金リスト](https://developers.google.com/maps/billing-and-pricing/pricing?hl=ja&_gl=1*8kirx1*_up*MQ..*_ga*MjE1Mjk4MTY1LjE3NDkzNjcwNzc.*_ga_NRWSTWS78N*czE3NDkzNjcwNzckbzEkZzEkdDE3NDkzNjcyMTEkajEkbDAkaDA.#map-loads-pricing)を参照

3. API を有効にしAPIキーを取得する
4. API キーの制限する

## 住所から緯度経度データを取得する

### get_longitude_and_latitude_from_address.py

住所から経度、緯度を取得するツール

使用API：[Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview?hl=ja)の[geocode.address.geocodeAddressQuery](https://developers.google.com/maps/documentation/geocoding/reference/rest/v4beta/geocode.address/geocodeAddressQuery?hl=ja&_gl=1*25slz2*_up*MQ..*_ga*MTYxNjg5NTkwNy4xNzQ5MzcwNDI2*_ga_NRWSTWS78N*czE3NDkzNzczMjUkbzIkZzEkdDE3NDkzNzczMzEkajU0JGwwJGgw)

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

## 緯度経度データから住所を取得する

### get_address_from_longitude_and_latitude.py

経度、緯度から住所を取得するツール

使用API：[Google Maps Geocoding API](https://developers.google.com/maps/documentation/geocoding/overview?hl=ja)の[geocode.location.geocodeLocationQuery](https://developers.google.com/maps/documentation/geocoding/reference/rest/v4beta/geocode.location/geocodeLocationQuery?hl=ja&_gl=1*1gjlyv1*_up*MQ..*_ga*MTYxNjg5NTkwNy4xNzQ5MzcwNDI2*_ga_NRWSTWS78N*czE3NDkzNzczMjUkbzIkZzEkdDE3NDkzNzczMjckajU4JGwwJGgw)

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
    |  |  ├─location.csv 
    ```

    CSVファイルの項目構成は次の通り

    |No|住所１|住所２|郵便番号|緯度|経度|
    |--|--|--|--|--|--|
    |1||||35.6585696|139.745484|

3. from_address.batを実行する

    from_loation.batの中身
    ```
    cd dist
    get_address_from_longitude_and_latitude.exe "../csv_folder/location.csv"
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