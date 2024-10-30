from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/hello')
def main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)


@app.post("/summarize")
def summarize(text):
    return summ_text