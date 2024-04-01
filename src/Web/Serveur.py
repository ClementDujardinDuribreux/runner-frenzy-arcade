from flask import Flask, render_template
from flask import request
from Connexion.Sql import Sql
import sqlite3
app = Flask(__name__)

@app.route("/home")
def page() :
    return render_template('home.html')
@app.route('/scores')
def page1() :
    connection = sqlite3.connect('bdd/bdd_jeu.db')


    # Code pour effectuer des requêtes SQL
    sql = 'SELECT login, Scores.score FROM Joueurs JOIN Scores ON Joueurs.id = Scores.id_player'
    mycursor = connection.cursor()
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return render_template('index.html', data=myresult)

@app.route("/connecte", methods =['POST'])
def page2():
    print(request.form['Id'],request.form['Mdp'])
    Sql.open_bdd()
    a = Sql.connection(request.form['Id'],request.form['Mdp'])
    if a :
        b = Sql.get_scores()
        print(b)
        return render_template('Doofenshmirtz.html', data = b)
    else :
        faux = "L'identifiant/MDP n'est pas bon"
        return faux    

@app.route('/about')
def page3() :
    return render_template('Aboutus.html')
    

     
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug = True)

