from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "<hdh1> Congratulation It worked !! </hfg1>"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
