import backend as bc

class Model(object):

    def __init__(self, input_cur, input_conn):
        self.cur = input_cur
        self.conn = input_conn

    def insert(self, table, columns, values):
        bc.insert(self.cur, table, columns, values)
        self.conn.commit()

    def update(self, table, set, condition):
        bc.update(self.cur, table, set, condition)
        self.conn.commit()
    
    def delete(self, table, condition):
        bc.delete(self.cur, table, condition)
        self.conn.commit()

    def random_film(self, n):
        bc.random_film(self.cur, self.conn, n)
        self.conn.commit()

    def random_hall(self, n):
        bc.random_hall(self.cur, self.conn, n)
        self.conn.commit()

    def random_performance(self, n):
        bc.random_performance(self.cur, self.conn, n)
        self.conn.commit()

    def random_performance_hall(self, n):
        bc.random_performance_hall(self.cur, self.conn, n)
        self.conn.commit()

    def random_ticket(self, n):
        bc.random_ticket(self.cur, self.conn, n)
        self.conn.commit()

    def select(self, columns, table, condition):
        bc.select(self.cur, columns, table, condition)
        self.conn.commit()