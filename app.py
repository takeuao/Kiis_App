from flask import Flask, render_template
from get_bus import get_timetable

#Flaskアプリを作成
app = Flask(__name__)

#トップページにアクセスされたときにこの関数を動かす
@app.route("/")
def index():
    timetable = get_timetable()

    #index.htmlにtimetableのデータを渡して表示する
    return render_template("index.html", timetable=timetable)

#アプリを起動
if __name__ == "__main__":
    app.run(debug=True)