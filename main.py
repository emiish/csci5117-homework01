from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    user_name = request.args.get("user", "unknown")
    return render_template('main.html', user=user_name)