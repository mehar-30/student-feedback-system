from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('feedback.db')
    conn.execute('CREATE TABLE IF NOT EXISTS feedback (id INTEGER PRIMARY KEY, name TEXT, message TEXT)')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        conn = sqlite3.connect('feedback.db')
        conn.execute("INSERT INTO feedback (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()

    return render_template('index.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)