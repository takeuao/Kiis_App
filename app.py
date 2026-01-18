from flask import Flask

#Flaskアプリを作成
app = Flask(__name__)

#トップページにアクセスされたときにこの関数を動かす
@app.route("/")
def index():
    return "<h1>Webアプリ開発へようこそ！</h1>"

#アプリを起動
if __name__ == "__main__":
    app.run(debug=True)