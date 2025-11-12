import sqlite3
import random
from flask import Flask

app = Flask(__name__)
DATABASE = 'names.db'

def init_db():
    """Initialize database and add sample names"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS names (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    # Check if table is empty
    cursor.execute('SELECT COUNT(*) FROM names')
    if cursor.fetchone()[0] == 0:
        # Add sample names
        sample_names = [
            ('Alice',),
            ('Bob',),
            ('Charlie',),
            ('Diana',),
            ('Emma',),
            ('Frank',),
            ('Grace',),
            ('Henry',)
        ]
        cursor.executemany('INSERT INTO names (name) VALUES (?)', sample_names)
        conn.commit()
    
    conn.close()

def get_random_name():
    """Get a random name from database"""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM names')
    names = cursor.fetchall()
    conn.close()
    
    if names:
        return random.choice(names)[0]
    return "No names in database"

@app.route('/')
def hello():
    random_name = get_random_name()
    return f'''
        <html>
            <head>
                <title>Hello World App</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        text-align: center;
                        padding: 50px;
                        background-color: #f0f0f0;
                    }}
                    h1 {{
                        color: #333;
                    }}
                    .name {{
                        font-size: 24px;
                        color: #007bff;
                        margin-top: 20px;
                    }}
                    button {{
                        margin-top: 20px;
                        padding: 10px 20px;
                        font-size: 16px;
                        cursor: pointer;
                        background-color: #007bff;
                        color: white;
                        border: none;
                        border-radius: 5px;
                    }}
                    button:hover {{
                        background-color: #0056b3;
                    }}
                </style>
            </head>
            <body>
                <h1>Hello World!</h1>
                <div class="name">Random Name: <strong>{random_name}</strong></div>
                <button onclick="location.reload()">Get Another Name</button>
            </body>
        </html>
    '''

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

