#creating game rock, paper, scissors with python and flask 
# Date: 10/10/2021
import flask
from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    #if player choose undefined 
    if user_choice not in choices:
        return render_template('index.html', result = 'Please choose rock, paper, or scissors')
    if user_choice == computer_choice:
        return render_template('index.html', result = 'Tie! You both chose ' + user_choice)
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return render_template('index.html', result = 'You win! The computer chose ' + computer_choice)
    elif user_choice == 'paper' and computer_choice == 'rock':
        return render_template('index.html', result = 'You win! The computer chose ' + computer_choice)
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return render_template('index.html', result = 'You win! The computer chose ' + computer_choice)
    else:
        return render_template('index.html', result = 'You lose! The computer chose ' + computer_choice)

if __name__ == '__main__':
    app.run(debug=True)

