import mysql.connector
from os import environ


class DB:

    def __init__(self):
        self._conn = mysql.connector.connect(host=environ['HOST'],
                                             user=environ['USER'],
                                             passwd=environ['PASSWD'],
                                             database=environ['DB'])
        self._cur = self._conn.cursor(dictionary=True)

    def selectAll(self, columns, table):
        cur = self._cur
        names = ''
        for i in columns:
            names = names + i + ','
        names = names[:-1] + ' '
        sql = 'SELECT ' + names + 'FROM ' + table + ' WHERE removed = 0;'
        cur.execute(sql)
        data = cur.fetchall()
        return data

    def insert(self, data, table):
        cur = self._cur
        columns = []
        values = []

        for i in data:
            columns.append(i)
            values.append(data[i])

        query_placeholders = ', '.join(['%s'] * len(values))
        query_columns = ', '.join(columns)
        try:
            insert_query = ''' INSERT INTO %s (%s) VALUES (%s) ;''' % (table, query_columns, query_placeholders)
            cur.execute(insert_query, values)
            cur.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        # cur.execute('SELECT id FROM' + table + 'ORDER BY id DESC LIMIT 1;')

    def SelectById(self, id, columns, table):
        cur = self._cur
        names = ''
        for i in columns:
            names = names + i + ','
        names = names[:-1] + ' '

        sql = 'SELECT ' + names + 'FROM ' + table + ' WHERE id = {} AND removed = 0;'.format(id)

        cur.execute(sql)
        data = cur.fetchall()
        return data

    def remove(self, id, table):

        try:
            sql = ''' UPDATE {} SET removed = 1 WHERE id = {};'''.format(table, id)
            cur = self._cur
            cur.execute(sql)
            cur.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def runFetchRow(self, sql):
        cur = self._cur
        cur.execute(sql)
        data = cur.fetchall()

        return data

    def getPasswordByEmail(self, email):
        cur = self._cur
        sql = '''SELECT password FROM user WHERE email = '{}';'''.format(email)
        cur.execute(sql)
        password = cur.fetchone()
        print(password)
        if password is None:
            return False
        return password

    def __del__(self):
        self._conn.close()

    # @staticmethod
    # def update(id, params, table):
    #
    #     columns = []
    #     values = []
    #
    #     for i in data:
    #         columns.append(i)
    #         values.append(data[i])
    #
    #     query_placeholders = ', '.join(['%s'] * len(values))
    #     query_columns = ', '.join(columns)
    #     try:
    #
    #         db = app.mysql
    #         insert_query = ''' INSERT INTO %s (%s) VALUES (%s) ;''' % (table, query_columns, query_placeholders)
    #         cur = mysql.cursor()
    #         cur.execute(insert_query, values)
    #         mysql.connection.commit()
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False
        # cur.execute('SELECT id FROM' + table + 'ORDER BY id DESC LIMIT 1;')
