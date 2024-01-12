import sqlite3


class Error(Exception):
    pass


class DataBase:
    def __init__(self):
        pass

    def check_nickname(self, nickname):
        try:
            if nickname == '':
                raise Error('недопустимый никнейм')
            return 'OK'
        except Exception as e:
            return e
