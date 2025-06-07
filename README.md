# Latitude-longitude

7桁の郵便番号から経度、緯度を取得するツール

緯度経度データは、[GeoApi](https://geoapi.heartrails.com/)を使用して取得する。APIは、[郵便番号による住所検索API](https://geoapi.heartrails.com/api.html#postal)を使用した

## 前提作業

郵便局のサイトの[住所の郵便番号（1レコード1行、UTF-8形式）（CSV形式）](https://www.post.japanpost.jp/zipcode/dl/utf-zip.html)から最新の全国の郵便番号一覧CSVを入手する

※データが膨大であるため、必要な都道府県を絞り、郵便番号のCSVファイルを用意する

例）東京都で絞ると郵便番号は4,106件（不要な郵便番号を除いた）

## 使用方法（Windowsの場合）

1. githubからリポジトリをgit cloneする
    ```
    git clone https://github.com/auco67/Latitude-longitude.git
    ```

2. csvファイルを格納するフォルダ`csv_folder`を作成しCSVファイルを格納する
    ```
    latitude-longitude
     ├─csv_folder
     |  ├─aaaa.csv
    ```

    CSVファイルの項目構成は次の通り

    |No|住所１|住所２|郵便番号|緯度|経度|
    |--|--|--|--|--|--|
    |1|千代田区|飯田橋|1020072|||

3. main.batを実行する

    main.batの中身
    ```
    cd dist
    main.exe 'csv_folder'
    pause
    ```

    ※フォルダ名が`csv_folder`以外にする場合は、`main.bat`の中身も修正する必要がある

    ※数件のデータの場合長時間掛かる

    実行後は、同じCSVファイル名で上書きされる