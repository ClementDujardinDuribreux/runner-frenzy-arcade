import sqlite3

class Sql:

    """
    Cette classe permet d'interagir avec la base de donnee
    """

    connected = False

    def open_bdd(cls):
        cls.bdd = sqlite3.connect('bdd/bdd_jeu.db')
        cls.cursor = cls.bdd.cursor()
    
    def close_bdd(cls):
        cls.cursor.close()
        cls.bdd.commit()
        cls.bdd.close()

    def connection(cls, login:str, password:str):
        if cls.verification_login_mdp(login, password):
            cls.id_player = cls.get_id_player(login)
            cls.connected = True
            return True
        return False

    def get_id_player(cls, login:str):
        cls.cursor.execute("SELECT id FROM Joueurs WHERE login = ?", (login, ))
        identifiant = cls.cursor.fetchall()
        return identifiant[0][0]

    def add_player(cls, login:str, password:str):
        cls.cursor.execute("INSERT INTO Joueurs(login, password) VALUES (?, ?)", (login, password))
        cls.bdd.commit()

    def add_score(cls, score:int):
        cls.cursor.execute("INSERT INTO Scores(id_player, score) VALUES (?, ?)", (cls.id_player, score))
        cls.bdd.commit()

    def get_scores(cls):
        liste_scores = []
        cls.cursor.execute("SELECT score FROM Scores WHERE id_player = ? ORDER BY score DESC", (str(cls.id_player)))
        scores = cls.cursor.fetchall()
        for score in scores:
            liste_scores.append(score[0])
        return liste_scores

    def get_max_score(cls):
        cls.cursor.execute("SELECT MAX(score) FROM Scores WHERE id_player = ?", (str(cls.id_player)))
        return cls.cursor.fetchall()[0][0]

    def get_max_score_all_player(cls):
        cls.cursor.execute("SELECT login, MAX(score) FROM Scores JOIN Joueurs ON Joueurs.id = Scores.id_player GROUP BY login ORDER BY score DESC")
        return cls.cursor.fetchall()

    def verification_login_mdp(cls, login:str, password:str):
        cls.cursor.execute("SELECT login, password FROM Joueurs WHERE login = ? AND password = ?", (login, password))
        l = cls.cursor.fetchall()
        if l != []:
            return True
        return False

    open_bdd = classmethod(open_bdd)
    close_bdd = classmethod(close_bdd)
    connection = classmethod(connection)
    get_id_player = classmethod(get_id_player)
    add_player = classmethod(add_player)
    add_score = classmethod(add_score)
    get_scores = classmethod(get_scores)
    get_max_score = classmethod(get_max_score)
    get_max_score_all_player = classmethod(get_max_score_all_player)
    verification_login_mdp = classmethod(verification_login_mdp)