from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>Hello from Flask on port 5000!</h1>"

@app.route('/hello')
def helloagain():
    return "<h1>Hello endpoint!</h1>"

@app.route('/bye')
def helloagain():
    return "<h1>Bye!</h1>"

if __name__ == '__main__':
    app.run(port=5000)

