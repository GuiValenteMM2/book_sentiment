from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<word>")
def definition(word):
    uppercase = word.upper()
    return {"word": word,
            "uppercase": uppercase}


if __name__ == "__main__":
    app.run(debug= True)
