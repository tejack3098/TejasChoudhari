from flask import Flask, render_template, request, redirect, url_for
import requests


app = Flask(__name__)
app.secret_key="abcdffgdefgac"

@app.route('/')
def IndexPage():
    return render_template("index.html")

@app.route('/blog')
def Blog():
    return render_template("single.html")


if __name__ == '__main__':
    app.run(debug = True)