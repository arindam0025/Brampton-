import os
from flask import Flask, render_template, request
from brampton_agent import run_brampton

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_query = request.form['query']
        answers = run_brampton(user_query)
        return render_template('index.html', query=user_query, answers=answers)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
