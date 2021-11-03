from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL


app = Flask(__name__,
            static_url_path='', 
            static_folder='static',
            template_folder='templates')
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Euromak:2828'
app.config['MYSQL_DATABASE_DB'] = 'euromak_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
conn = mysql.connect()
cursor =conn.cursor()

@app.route("/")
def index():
    cursor.execute("SELECT * FROM euromak_db.machines;")
    db_machines = cursor.fetchall()
    print(db_machines)
    return render_template("index.html",table=db_machines)

@app.route("/ekle")
def ekle():
    return render_template("ekle.html")

@app.route('/ekle_post', methods=['POST'])
def handle_data():
    manufacturer = request.form['manufacturer']
    model = request.form["model"]
    year = request.form["year"]
    impressions = request.form["impressions"]

    print(manufacturer)
    print(model)
    print(year)
    print(impressions)
    cursor.execute("INSERT INTO `euromak_db`.`machines` ( `manufacturer`, `model`, `year`, `impressions`) VALUES ('{}', '{}', '{}', '{}');".format(manufacturer, model, year, impressions))
    conn.commit()
    return redirect("http://127.0.0.1:5000", code=302)

if __name__ == '__main__':
   app.run(debug=True)


# 
