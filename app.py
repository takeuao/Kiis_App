from flask import Flask, render_template, jsonify
from get_bus import get_timetable, get_next_bus
from get_weather import get_weather_info

#Flaskアプリを作成
app = Flask(__name__)

# ★ここに追加：サービスワーカーをルート階層で読み込めるようにする
@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')

#トップページにアクセスされたときにこの関数を動かす
@app.route("/")
def index():
    #太宰府駅発の時刻表を準備する
    timetable_station = get_timetable(1)
    next_station = get_next_bus(timetable_station)

    #次のバスのリストを取得する
    timetable_uni = get_timetable(0)
    next_uni = get_next_bus(timetable_uni)

    #天気情報を取得
    weather = get_weather_info()

    #index.htmlにtimetableのデータを渡して表示する
    return render_template("index.html",
                           next_station=next_station,
                           next_uni=next_uni,
                           weather=weather)

#バスのデータだけを返すAPI
@app.route("/api/bus")
def update_bus():
    #太宰府駅発を計算
    timetable_station = get_timetable(1)
    next_station = get_next_bus(timetable_station)

    #大学発を計算
    timetable_uni = get_timetable(0)
    next_uni = get_next_bus(timetable_uni)

    #計算結果をJSON形式で返す
    return jsonify({
        "next_station": next_station,
        "next_uni": next_uni
    })

#アプリを起動
if __name__ == "__main__":
    app.run(debug=True)