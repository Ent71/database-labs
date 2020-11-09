
class View(object):

    def display_insert(self, table, columns, values):
        print("Insert {0} ({1}) into table {2}\n".format(values, columns, table))

    def display_update(self, table, set, condition):
        if condition == "\'t\'":
            print("All columns update {0} in table {1}\n".format(set, table))
        else:
            print("All columns where {0} update {1} in table {2}\n".format(condition, set, table))

    def display_delete(self, table, condition):
        if condition == "\'t\'":
            print("All columns delete in table {1}\n".format(table))
        else:
            print("All columns where {0} delete in table {2}\n".format(condition, set, table))

    def display_random(self, table, n):
        print("Randomed {0} rows in table {1}\n".format(n, table))

    def display_select(self, columns , tables, cursor, time, columns1):
        if cursor!=None:
            print("Select {} column(s) in {} table(s) is done\n".format(columns1,tables))
            print(columns)
            for cur in cursor:
                for c in cur:
                    print("%-25s" % c,end='')
                print()
            print("\nTime of select: {} ms".format(time * 1000.0))
        else:
            print("Can't select {} column(s) in {} table(s)".format(columns,tables))

