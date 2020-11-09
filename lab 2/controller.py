import backend as bc
import model as md
import view as vw
import psycopg2
import time

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def insert(self, table, columns, values):
        try:
            self.model.insert(table, columns, values)
            self.view.display_insert(table, columns, values)
        except Exception as e:
            print("can't insert into {0} columns {1} values {2}".format(table, columns, values))
            print(e)
            self.model.conn.rollback()

    def update(self, table, set, condition):
        try:
            self.model.update(table, set, condition)
            self.view.display_update(table, set, condition)
        except Exception as e:
            print(e)
            self.model.conn.rollback()
    
    def delete(self, table, condition):
        try:
            if table == "\"Film\"":
                self.delete_film(table, condition)
            elif table == "\"Performance\"":
                self.delete_performance(table, condition)
            elif table == "\"Hall\"":
                self.delete_hall(table, condition)
            elif table == "\"Performance/Hall\"":
                self.delete_performance_hall(table, condition)
            elif table == "\"Ticket\"":
                self.delete_ticket(table, condition)
            #self.model.delete(table, condition)
            self.view.display_delete(table, condition)
        except Exception as e:
            if condition == "\'t\'":
                print("can't delete table {0}".format(table))
            else:
                print("can't delete table in {0} with condition {1}".format(table, condition))
            print(e)
            self.model.conn.rollback()

    def delete_film(self, table, condition):
        try:
            self.delete_performance("\"Performance\"", "\"FilmID\" in (select \"FilmID\" from \"Film\" where " + condition + ")")
            self.model.delete(table, condition)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

    def delete_hall(self, table, condition):
        try:
            self.delete_performance_hall("\"Performance/Hall\"", "\"HallID\" in (select \"HallID\" from \"Hall\" where " + condition + ")")
            self.model.delete(table, condition)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

    def delete_performance(self, table, condition):
        try:
            self.delete_performance_hall("\"Performance/Hall\"", "\"PerformanceID\" in (select \"PerformanceID\" from \"Performance\" where " + condition + ")")
            self.model.delete(table, condition)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

    def delete_performance_hall(self, table, condition):
        try:
            self.delete_ticket("\"Ticket\"", "\"PerformanceHallID\" in (select \"PerformanceHallID\" from \"Performance/Hall\" where " + condition + ")")
            self.model.delete(table, condition)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

    def delete_ticket(self, table, condition):
        try:
            self.model.delete(table, condition)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

    def select(self, columns, table, condition, columns_all):
        try:
            Time = time.time()
            self.model.select(columns, table, condition)
            Time = time.time() - Time
            self.view.display_select(columns_all, table, self.model.cur, Time, columns)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

    def random_table(self, table, n):
        try:
            if table == "\"Film\"":
                self.model.random_film(n)
            elif table == "\"Performance\"":
                self.model.random_performance(n)
            elif table == "\"Hall\"":
                self.model.random_hall(n)
            elif table == "\"Performance/Hall\"":
                self.model.random_performance_hall(n)
            elif table == "\"Ticket\"":
                self.model.random_ticket(n)
            #self.model.delete(table, condition)
            self.view.display_random(table, n)
        except Exception as e:
            print(e)
            self.model.conn.rollback()

def table_to_columns(table):
    n = 17
    if table == "\"Film\"":
        return "\"FilmID\"" + " " * n + "\"Movie_title\"" + " " * n + "\"Director\"" + " " * n + "\"MPAA\"" + " " * n
    elif table == "\"Hall\"":
        return "\"HallID\"" + " " * n + "\"Size\"" + " " * n + "\"Number\"" + " " * n
    elif table == "\"Performance\"":
        return "\"PerformanceID\"" + " " * n + "\"FilmID\"" + " " * n + "\"Time\"" + " " * n
    elif table == "\"Performance/Hall\"":
        return "\"PerformanceHallID\"" + " " * n + "\"PerformanceID\"" + " " * n + "\"HallID\"" + " " * n
    elif table == "\"Ticket\"":
        return "\"TicketID\"" + " " * n + "\"PerformanceHallID\"" + " " * n + "\"Seat\"" + " " * n + "\"Row\"" + " " * n
    else:
        return ""

def menu():
    conn = psycopg2.connect(dbname="Cinema", user="postgres", password="e28n3t0")
    cur = conn.cursor()
    c = Controller(md.Model(cur, conn), vw.View())
    work = True
    previos_menu_type = "MAIN"
    menu_type = "MAIN"
    while(work):
        if menu_type == "MAIN":
            print("\nTables")
            print("Insert")
            print("Update")
            print("Delete")
            print("Random")
            print("Select")
            print("Help")
            print("Exit\n")
            previos_menu_type = "MAIN"
            menu_type = input().upper()
        elif menu_type == "TABLES":
            print("\nFilm:")
            print("FilmID - int; Movie_title - string; Director - string; MPAA - string")
            print("Performance:")
            print("PerformanceID - int; FilmID - int; Time - time(23:59:59)")
            print("Hall:")
            print("HallID - int; Size - int; Number - int")
            print("Performance/Hall:")
            print("PerformanceHallID - int; PerformanceID - int; HallID - int")
            print("Ticket:")
            print("TicketID - int; Seat - int; Row - int; PerformanceHallID - int")
            print("\nInput something to continue...\n")
            input()
            menu_type = "MAIN"
        elif menu_type == "INSERT":
            columns = ""
            values = ""
            value = " "
            print("\nInput table continue:\n")
            table = input()
            print("\nInput columns(separator - ,)")
            columns = input()
            while len(value) != 0:
                print("Input values or nothing to continue(separator - ,):")
                value = input()
                if len(value) != 0:
                    value = "(" + value + ")"
                    if len(values) != 0:
                        values += ","
                values += value
            c.insert(table, columns, values)
            print("\nInput something to continue...\n")
            input()
            menu_type = "MAIN"
        elif menu_type == "UPDATE":
            set = ""
            str = " "
            cond = ""
            print("\nInput table")
            table = input()
            while len(str) != 0:
                print("Input column or nothing to continue:")
                str = input()
                if len(str) != 0:
                    str += "="
                    if len(set) != 0:
                        set += ","
                print("Input value or nothing to continue:")
                str += input()
                set += str
            print("Input condition or nothing to continue:")
            cond = input()
            if len(cond) == 0:
                cond = "\'t\'"
            c.update(table, set, cond)
            menu_type = "MAIN"
        elif menu_type == "DELETE":
            print("\nInput table")
            table = input()
            print("Input condition or nothing to continue:")
            cond = input()
            if len(cond) == 0:
                cond = "\'t\'"
            c.delete(table, cond)
            menu_type = "MAIN"
        elif menu_type == "RANDOM":
            print("Select table:")
            table = input()
            try:
                print("Select number:")
                n = int(input())
                c.random_table(table, n)
            except:
                print("Its not number")
            
            menu_type = "MAIN"
        elif menu_type == "SELECT":
            tables = ""
            table = " "
            columns = ""
            column = " "
            columns_all = ""
            while len(column) != 0:
                print("Input column or * to all or nothing to continue:")
                column = input()
                if len(column) != 0 and len(tables) != 0:
                    columns += ","
                columns += column

            while len(table) != 0:
                print("Input table or nothing to continue:")
                table = input()
                if len(table) != 0:
                    if len(tables) != 0:
                        tables += ","
                    if columns == "*":
                        columns_all += table_to_columns(table)
                    else:
                        columns_all = columns
                
                tables += table

            print("Input condition or nothing to continue:")
            cond = input()
            if len(cond) == 0:
                cond = "\'t\'"

            c.select(columns, tables, cond, columns_all)
            menu_type = "MAIN"
        elif menu_type == "HELP":
            print("\nInput string example: \'example\'")
            print("Input table or column example: \"TableID\"")
            print("Separator - ,")
            print("\nInput something to continue...\n")
            input()
            menu_type = "MAIN"
        elif menu_type == "EXIT":
            work = False
        else:

            menu_type = previos_menu_type
    cur.close()
    conn.close()

menu()
