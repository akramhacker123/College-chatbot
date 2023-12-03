from flask import Flask, render_template, request
import Bot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_input = request.args.get('msg')
    response = Bot.function(user_input)
    return str(response)

if __name__ == '__main__':
    app.run(debug=True)
