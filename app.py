from flask import Flask, render_template


app = Flask(__name__)
app.secret_key = "aayush"


@app.route('/')
def hello_world():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()