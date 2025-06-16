from flask import Flask, render_template, url_for, redirect
import asyncio
from form_filler import fill_form

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    print('called')
    asyncio.run(fill_form())
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)