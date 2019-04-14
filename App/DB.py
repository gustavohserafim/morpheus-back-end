import app


class DB:

    @staticmethod
    def selectAll(columns, table):
        names = ''
        for i in columns:
            names = names + i + ','
        names = names[:-1] + ' '
        sql = 'SELECT ' + names + 'FROM ' + table + ';'
        mysql = app.mysql
        cur = mysql.connection.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        result = []
        for k, v1 in enumerate(data):
            row = {}
            for k, v2 in enumerate(v1):
                row.update({columns[k]: v2})
            result.append(row)

        return result

    @staticmethod
    def insert(data, table):
        columns = ''
        values = ''
        for k, v in enumerate(data):
            columns = columns + k
            values = values + v

        sql = 'INSERT INTO' + table + '(' + columns + ') VALUES (' + values + ')'
        mysql = app.mysql
        cur = mysql.connection.cursor()
        cur.execute(sql)
        mysql.connection.commit()
        cur.execute('SELECT id FROM' + table + 'ORDER BY id DESC LIMIT 1;')
        print(cur.fetchone())