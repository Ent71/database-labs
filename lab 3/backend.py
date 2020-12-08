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
        
