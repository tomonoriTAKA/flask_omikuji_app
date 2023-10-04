import random
from flask import Flask, render_template

app = Flask(__name__)


# おみくじアプリルーティング
@app.route("/omikuji")
def omikuji():
    # 変数を作成
    # result = "大吉!!"
    # random.choiceを使って大吉、吉、凶に振り分ける
    result = random.choice(["大吉!!", "吉", "凶..."])
    # テンプレートでresult変数を使用する
    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(port=8000, debug=True)
