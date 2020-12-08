import backend as bc

class Model(object):

    def insert(self, table, columns, values):
        bc.insert(table, columns, values)

    def update(self, table, set, condition):
        bc.update(table, set, condition)
    
    def delete(self, table, condition):
        bc.delete(table, condition)
