import requests
import datetime
from bs4 import BeautifulSoup


def get_timetable(table_index):
    #スクールバス運行表のURL
    url = "https://www.kiis.ac.jp/information/bus/"

    #ページ取得の命令
    response = requests.get(url)

    #HTMLをBeautifulSoupに渡して、扱いやすい状態にする
    soup = BeautifulSoup(response.text, "html.parser")

    #すべての表tableを探す
    tables = soup.find_all("table")

    #1つ目の表を選択
    target_table = tables[table_index]

    #選んだ表の中から行trを探す
    rows = target_table.find_all("tr")

    #リストを作成
    timetable = []

    ### print(f"見つかった行の数: {len(rows)}")

    #すべての行をループする
    for row in rows:
        #その行の中にあるすべてのセルtdを探す
        cols = row.find_all("td")

        #セルがちょうど2つある行だけを処理 (見出しなどを除外)
        if len(cols) == 2:
            hour = cols[0].text.strip() #1つ目のセル…時間
            minutes_text = cols[1].text.strip() #2つ目のセル…分

            #カンマで区切ってリスト配列にする
            departures = minutes_text.split(",")

            ### print(f"【{hour}】")

            for dep in departures:
                if "←" in dep:
                    #矢印があれば区切る
                    parts = dep.split("←")
                    minute = parts[0]
                    note = parts[1]
                    ### print(f" - 分: {minute} (※注釈: {note})")
                else:
                    minute = dep
                    note = "" #注釈がない場合は空文字にする
                    #矢印がなければそのまま表示する
                    ### print(f" - 分: {dep}")

                bus_data = {
                    "hour": hour,
                    "minute": minute,
                    "note": note
                }

                timetable.append(bus_data)

    return timetable

def get_next_bus(timetable):
    now =datetime.datetime.now()

    next_buses = []

    #リストの中身を順番にチェックする
    for bus in timetable:

        #「時」という文字を取り除く
        h = int(bus["hour"].replace("時", ""))

        #分が文字の場合
        if not bus["minute"].isdigit():
            
            #その時間が今の時間以降なら表示する
            if h >= now.hour:
                next_buses.append(bus)

                #2つ先の便まで探す
                if len(next_buses) >= 2:
                    break
            
            continue

        #分が数字の場合
        m = int(bus["minute"])
        
        #今日の日付と合成して比較用データを作成する
        bus_time = datetime.datetime(now.year, now.month, now.day, h, m)

        if bus_time > now:
            next_buses.append(bus)

            #2つ先の便まで探す
            if len(next_buses) >= 2:
                break
        
    return next_buses

#if __name__ == "__main__":
#    result = get_timetable()
#    print(result)

if __name__ == "__main__":
    timetable = get_timetable()
    result_buses = get_next_bus(timetable)
    print(f"次のバスは: {result_buses}")