import app


class DB:

    @staticmethod
    def selectAll(columns, table):
        names = ''
        for i in columns:
            names = names + i + ','
        names = names[:-1] + ' '
        sql = 'SELECT ' + names + 'FROM ' + table + ' WHERE removed = 0;'
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
        columns = []
        values = []
        print(data, table)
        for i in data:
            columns.append(i)
            values.append(data[i])

        query_placeholders = ', '.join(['%s'] * len(values))
        query_columns = ', '.join(columns)
        try:

            mysql = app.mysql
            insert_query = ''' INSERT INTO %s (%s) VALUES (%s) ;''' % (table, query_columns, query_placeholders)
            cur = mysql.connection.cursor()
            cur.execute(insert_query, values)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        # cur.execute('SELECT id FROM' + table + 'ORDER BY id DESC LIMIT 1;')

    @staticmethod
    def SelectById(id, columns, table):
        names = ''
        for i in columns:
            names = names + i + ','
        names = names[:-1] + ' '

        mysql = app.mysql
        cur = mysql.connection.cursor()
        sql = 'SELECT ' + names + 'FROM ' + table + ' WHERE id = {} AND removed = 0;'.format(id)

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
    def remove(id, table):
        try:
            mysql = app.mysql
            sql = ''' UPDATE {} SET removed = 1 WHERE id = {};'''.format(table, id)
            cur = mysql.connection.cursor()
            cur.execute(sql)
            mysql.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    @staticmethod
    def runFetchRow(sql):

        mysql = app.mysql
        cur = mysql.connection.cursor()
        cur.execute(sql)
        data = cur.fetchall()

        return data

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
    #         mysql = app.mysql
    #         insert_query = ''' INSERT INTO %s (%s) VALUES (%s) ;''' % (table, query_columns, query_placeholders)
    #         cur = mysql.connection.cursor()
    #         cur.execute(insert_query, values)
    #         mysql.connection.commit()
    #         return True
    #     except Exception as e:
    #         print(e)
    #         return False
        # cur.execute('SELECT id FROM' + table + 'ORDER BY id DESC LIMIT 1;')
