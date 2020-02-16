from flask import Flask, request, render_template
import requests 

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/players", methods=["POST"])
def players():
    nickname = request.form["query"]
    response = requests.get(f"https://api-paladins.herokuapp.com/searchplayers/{nickname}")
    context = {
        "nickname": nickname,
        "players": response.json()
    }
    return render_template("players.html", **context)

@app.route("/player/<string:nickname>")
def player(nickname):
    player_info = requests.get(f"https://api-paladins.herokuapp.com/getplayer/{nickname}")
    champions = requests.get(f"https://api-paladins.herokuapp.com/getchampions/{nickname}")
    context = {
        "info": player_info.json(),
        "champions": champions.json()
    }
    return render_template('player.html', **context)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")