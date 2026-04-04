from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect('feedback.db')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            message TEXT
        )
    ''')
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    conn = sqlite3.connect('feedback.db')
    msg = None   # success message

    # Insert feedback
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']

        conn.execute(
            "INSERT INTO feedback (name, message) VALUES (?, ?)",
            (name, message)
        )
        conn.commit()

        msg = "Feedback submitted successfully!"

    # Fetch all feedback
    cursor = conn.execute("SELECT name, message FROM feedback")
    data = cursor.fetchall()
    conn.close()

    return render_template('index.html', feedbacks=data, msg=msg)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)