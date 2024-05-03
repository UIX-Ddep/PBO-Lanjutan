from flask import Flask, render_template
from connection import get_db

app = Flask(__name__)
db = get_db()


@app.route("/dosen")
def index ():
    cursor = db.cursor()
    cursor.execute('select * from dosen')
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', dosen=data)



if __name__ == '__main__':
    app.run(debug=True)