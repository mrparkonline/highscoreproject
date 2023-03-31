from flask import Flask

# High Score Flask App
''' Running our app
python3 -m flask --app APPNAME run
'''
app = Flask(__name__)

@app.route("/")
def main():
    return "Hello, World!"