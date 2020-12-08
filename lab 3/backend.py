from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy import create_engine
from psycopg2 import sql
import psycopg2
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

Base = declarative_base()
DATABASE_URI = 'postgres://postgres:e28n3t0@localhost/Cinema'

class Film(Base):
    __tablename__ = 'Film'
    FilmID = Column('FilmID' ,Integer, primary_key=True)
    Movie_title = Column('Movie_title', String)
    Director = Column('Director', String)
    MPAA = Column('MPAA', String)

    performance = relationship("Performance", back_populates="film")
    
    def __repr__(self):
        return "<Film(Movie_title='{}', Director='{}', MPAA='{}')>"\
                .format(self.Movie_title, self.Director, self.MPAA)

class Performance(Base):
    __tablename__ = 'Performance'
    PerformanceID = Column('PerformanceID', Integer, primary_key=True)
    Time = Column('Time', Time)
    FilmID = Column('FilmID', Integer, ForeignKey('Film.FilmID'))

    film = relationship("Film", back_populates="performance")
    performancehall = relationship("PerformanceHall", back_populates = "performance")
    
    def __repr__(self):
        return "<Performance(Time={})>"\
                .format(self.Time)

class Hall(Base):
    __tablename__ = 'Hall'
    HallID = Column(Integer, primary_key = True)
    Size = Column(Integer)
    Number = Column(Integer)

    performancehall = relationship("PerformanceHall", back_populates = "hall")

    def __rerp__(self):
        return "<Hall(Size={}, Number={})>"\
                .fromat(self.Size, self.Number)

class PerformanceHall(Base):
    __tablename__ = 'Performance/Hall'
    PerformanceHallID = Column('PerformanceHallID', Integer, primary_key = True)
    HallID = Column('HallID', Integer, ForeignKey('Hall.HallID'))
    PerformanceID = Column('PerformanceID', Integer, ForeignKey('Performance.PerformanceID'))

    performance = relationship("Performance", back_populates="performancehall")
    hall = relationship("Hall", back_populates="performancehall")
    ticket = relationship("Ticket", back_populates ="performancehall")

    def __rerp__(self):
        return "<PerformanceHall()>"\
                .fromat(self.Size, self.Number)

class Ticket(Base):
    __tablename__ = 'Ticket'
    TicketID = Column('TicketID', Integer, primary_key = True)
    Seat = Column('Seat', Integer)
    Row = Column('Row', Integer)
    PerformanceHallID = Column('PerformanceHallID', Integer, ForeignKey('Performance/Hall.PerformanceHallID'))

    performancehall = relationship("PerformanceHall", back_populates = "ticket")

    def __repr__(self):
        return "<Ticket(Seat={}, Row={})>"\
                .format(self.Seat, self.Row)




#user_id = Column(Integer, ForeignKey('users.id'))
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
ed_user = Film(Movie_title='film1', Director='d1', MPAA='r18')
session = Session()
session.add(ed_user)
session.commit()



"""
def insert_into(table, columns, values, ind):
    try:
        
        add_list=[]
        length=len(columns)
        count=0
        if table== "Users":
            for i in range(ind):
                u=User()
                for j in range(length):
                    if columns[j]=="Name":
                        u.Name=values[count]
                    elif columns[j]=="Email":    
                        u.Email=values[count]
                    elif columns[j]=="N_sub":    
                        u.N_sub=values[count]
                    count+=1
                add_list.append(u)
        elif table == "Posts":
            for i in range(ind):
                p=Post()
                for j in range(length):
                    if columns[j]=="Topic":
                        p.Topic=values[count]
                    elif columns[j]=="Post":    
                        p.Post=values[count]
                    elif columns[j]=="Time_create":    
                        p.Time_create=values[count]
                    elif columns[j]=="UserIDFK":    
                        p.useridfk=values[count]
                    count+=1
                add_list.append(p)
        elif table == "Comments":
            for i in range(ind):
                c=Comment()
                for j in range(length):
                    if columns[j]=="Comment":
                        c.Comment=values[count]
                    elif columns[j]=="Time_create":    
                        c.Time_create=values[count]
                    elif columns[j]=="UserIDFK":    
                        c.useridfk=values[count]
                    elif columns[j]=="PostIDFK":    
                        c.postidfk=values[count]
                    count+=1
                add_list.append(c)
        elif table == "Ratings":
            for i in range(ind):
                r=Rating()
                for j in range(length):
                    if columns[j]=="Rating":
                        r.Rating=values[count]
                    elif columns[j]=="Time_create":    
                        r.Time_create=values[count]
                    elif columns[j]=="UserIDFK":    
                        r.useridfk=values[count]
                    elif columns[j]=="PostIDFK":    
                        r.postidfk=values[count]
                    count+=1
                add_list.append(r)
        session.add_all(add_list)
        session.commit()
        return True
    except Exception as err:
        print("Error {} ".format(err))
        session.rollback();
        return False
"""

def insert(table, columns, values):
    try:
        length = len(columns)
        table_obj = eval(table)()
        result = []
        for value in values:
            for i in range(length):
                setattr(table_obj, columns[i], value[i])
            result.append(table_obj)
        session.add_all(result)
        session.commit()
    except Exception as err:
        print("Error: {}".format(err))
        session.rollback()

def update(table, set, condition):
    try:
        s = session.query(eval(table))
        if condition != 't':
            s = session.query(eval(table)).filter(getattr(eval(table),condition[0]) == condition[1])
        for elem in s:
            for st in set:
                setattr(elem, st[0], st[1])
        session.commit()
    except Exception as err:
        print("Error: {}".format(err))
        session.rollback()

def delete(table, condition):
    try:
        s = session.query(eval(table))
        if condition != 't':
            s = session.query(eval(table)).filter(getattr(eval(table),condition[0]) == condition[1]).delete()
        else:
            s = session.query(eval(table)).delete()
        session.commit()
    except Exception as err:
        print("Error: {}".format(err))
        session.rollback()


    #new_film = 
        