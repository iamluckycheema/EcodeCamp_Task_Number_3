# app.py
from flask import Flask, render_template, request, redirect, url_for
from quiz import questions

app = Flask(__name__)
score = 0
current_question = 0

@app.route('/')
def home():
    global score, current_question
    score = 0
    current_question = 0
    return render_template('index.html', question=questions[current_question], score=score)

@app.route('/next', methods=['POST'])
def next_question():
    global score, current_question
    answer = request.form['answer'].upper()
    if answer == questions[current_question]['answer']:
        score += 1
    current_question += 1

    if current_question < len(questions):
        return render_template('index.html', question=questions[current_question], score=score)
    else:
        return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
