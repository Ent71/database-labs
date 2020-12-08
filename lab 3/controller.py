import backend as bc
import model as md
import view as vw
import time

class Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def insert(self, table, columns, values):
        self.model.insert(table, columns, values)
        self.view.display_insert(table, columns, values)

    def update(self, table, set, condition):
        self.model.update(table, set, condition)
        self.view.display_update(table, set, condition)
    
    def delete(self, table, condition):
        self.model.delete(table, condition)
        self.view.display_delete(table, condition)

    


def menu():
    c = Controller(md.Model(), vw.View())
    work = True
    previos_menu_type = "MAIN"
    menu_type = "MAIN"
    while(work):
        if menu_type == "MAIN":
            print("\nTables")
            print("Insert")
            print("Update")
            print("Delete")
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
            columns = []
            values = []
            value = " "
            print("\nInput table continue:\n")
            table = input()
            print("\nInput columns(separator - ,)")
            columns = input().replace(" ", "").split(',')
            while len(value) != 0:
                print("Input values or nothing to continue(separator - ,):")
                value = input()
                value = value.replace(" ", "")
                if len(value) != 0:
                    values.append(value.split(','))
            for i in range(len(values)):
                for j in range(len(values[0])):
                    if values[i][j].isdigit():
                        values[i][j] = int(values[i][j])
            c.insert(table, columns, values)
            print("\nInput something to continue...\n")
            input()
            menu_type = "MAIN"
        elif menu_type == "UPDATE":
            set = ""
            lst_set = []
            
            str = " "
            cond = ""
            lst_cond = []
            print("\nInput table")
            table = input()
            while len(str) != 0:
                print("Input column or nothing to continue:")
                lst = []
                str = input()
                if len(str) != 0:
                    lst.append(str)
                #if len(str) != 0:
                #    str += "="
                #    if len(set) != 0:
                #        set += ","
                print("Input value or nothing to continue:")
                str = input()
                if len(str) != 0:
                    if str.isdigit():
                        lst.append(int(str))
                    else:
                        lst.append(str)
                if len(lst) != 0:
                    lst_set.append(lst)
            print("Input condition or nothing to continue:")
            cond = input().replace(" ", "").split('=')
            #cond = input()
            if len(cond) == 0:
                cond = "t"
            c.update(table, lst_set, cond)
            menu_type = "MAIN"
        elif menu_type == "DELETE":
            print("\nInput table")
            table = input()
            print("Input condition or nothing to continue:")
            cond = input().replace(" ", "").split('=')
            if len(cond) == 0:
                cond = "t"
            c.delete(table, cond)
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



menu()

