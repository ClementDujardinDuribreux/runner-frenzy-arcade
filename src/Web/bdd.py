import sqlite3
import panda as pd
import os
connection = sqlite3.connect('bdd_jeu.db')


# Code pour effectuer des requêtes SQL
sql = 'SELECT login, Scores.score FROM Joueurs JOIN Scores ON Joueurs.id = Scores.id_player'
mycursor = connection.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

df = pd.DataFrame()
for x in myresult :
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df,df2])

df.to_html('templates/index.html')