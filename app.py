from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action/<action>')
def action(action):
    messages = {
        'buy': 'You clicked Buy! 🛒',
        'sell': 'You clicked Sell! 💸',
        'info': 'This is a demo Flask shop. Try the buttons!'
    }
    return jsonify({'message': messages.get(action, 'Unknown action.')})

if __name__ == '__main__':
    # Ensure templates folder exists for Flask
    if not os.path.exists('templates'):
        os.makedirs('templates')
    app.run(debug=True)
