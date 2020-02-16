from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/players", methods=["POST"])
def players():
    nickname = request.form["query"]
    teste = []
    context = {
        "nickname": nickname,
        "teste": teste
    }
    return render_template("players.html", **context)

if __name__ == '__main__':
    app.run()