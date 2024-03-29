import sqlite3


class Error(Exception):
    pass


class DataBase:
    def __init__(self):
        self.db = "database_game.sqlite3"
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()

    def check_nickname(self, nickname):
        try:
            if nickname == '':
                raise Error('недопустимый никнейм')
            if len(nickname) < 3:
                raise Error('слишком короткий никнейм')
            return 'OK'
        except Exception as e:
            return e

    def add_to_database(self, nickname, result, score):
        query = "INSERT INTO game_result(nickname, result, score) VALUES (?, ?, ?)"
        self.cursor.execute(query, (nickname,result, score,))
        self.connection.commit()
