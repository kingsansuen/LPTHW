from flask import Flask, session, request
from flask import url_for, redirect, render_template
import map
from lexicon import *


app = Flask(__name__)


@app.route('/game', methods=['GET'])
def game_get():
    if 'scene' in session:
        thescene = map.SCENES[session['scene']]
        return render_template('show_scene.html', scene=thescene, password = map.pw)
    else:
        return render_template('you_died.html')

@app.route('/game', methods=['POST'])
def game_post():
    userinput = request.form.get('userinput')
    final_userinput = lexicon.output(userinput)
    if 'scene' in session:
        if userinput is None:
            return render_template('you_died.html')
        else:
            currentscene = map.SCENES[session['scene']]
            nextscene = currentscene.go(final_userinput)

            if nextscene is None:
                return render_template('you_died.html')
            else:
                session['scene'] = nextscene.urlname
                return render_template('show_scene.html', scene=nextscene, password = map.pw)
    else:
        return render_template('you_died.html')

@app.route('/')
def index():
    session['scene'] = map.START.urlname
    return redirect(url_for('game_get')) # redirect the browser to the url for game_get
app.secret_key = 'replace this with your secret key'

if __name__ == "__main__":
    app.run()
