
class View(object):

    def display_insert(self, table, columns, values):
        print("Insert {0} ({1}) into table {2}\n".format(values, columns, table))

    def display_update(self, table, set, condition):
        if condition == "\'t\'":
            print("All columns update {0} in table {1}\n".format(set, table))
        else:
            print("All columns where {0} = {1} update {2} in table {3}\n".format(condition[0], condition[1], set, table))

    def display_delete(self, table, condition):
        if condition == "\'t\'":
            print("All columns delete in table {1}\n".format(table))
        else:
            print("All columns where {0} = {1} delete in table {2}\n".format(condition[0], condition[1], table))


