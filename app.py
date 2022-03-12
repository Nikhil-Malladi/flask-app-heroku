from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return '<h1>I want to Deploy Flask to Heroku</h1>'

if __name__=="__main__":
    app.run()
