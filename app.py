import os
import sys
import multiprocessing
from flask import Flask, render_template, request
from trading import launch_trading_app

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/launch', methods=['POST'])
def launch():
    if sys.platform.startswith('win'):
        # Windows-specific multiprocessing
        multiprocessing.freeze_support()
    
    process = multiprocessing.Process(target=launch_trading_app)
    process.start()
    return "success", 200

if __name__ == "__main__":
    app.run(debug=True, port=5001)