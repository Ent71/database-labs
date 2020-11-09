from psycopg2 import sql

def insert(cur, table, columns, values):
    cur.execute(sql.SQL("insert into " + table + " (" + columns + ") values " + values ))

def update(cur, table, set, condition):
    cur.execute(sql.SQL("update " + table + " set " + set + " where " + condition))

def delete(cur, table, condition):
    cur.execute(sql.SQL("delete from " + table + " where " + condition))

def str_rand_len(n):
    str = "chr(trunc(65 + random() * 25)::int)"
    i = 1
    for i in range(n):
        str += "|| chr(trunc(65 + random() * 25)::int)"
    return str

def random_one_film(cur, i, conn):
    try:
        cur.execute(sql.SQL("insert into \"Film\""  + " (\"FilmID\", \"Movie_title\", \"Director\", \"MPAA\") values (trunc(random()*10000000)::int," + str_rand_len(10) + "," + str_rand_len(10) + "," + str_rand_len(10) + ")"))
        return i + 1
    except:
        conn.rollback()
        return i

def random_film(cur, conn, n):
    i = 0
    while i < n:
        i = random_one_film(cur, i, conn)
        conn.commit()


def random_one_hall(cur, i, conn):
    try:
        cur.execute(sql.SQL("insert into \"Hall\"" + " (\"HallID\", \"Size\", \"Number\") values (trunc(random()*100000)::int, trunc(random()*1000000)::int, trunc(random()*1000000)::int)"))
        return i + 1
    except:
        conn.rollback()
        return i

def random_hall(cur, conn, n):
    i = 0
    while i < n:
        i = random_one_hall(cur, i, conn)
        conn.commit()
        
def random_one_performance(cur, i, conn):
    try:
        cur.execute(sql.SQL("insert into \"Performance\"" + " (\"PerformanceID\", \"FilmID\", \"Time\") values (trunc(random()*1000000)::int, (SELECT \"FilmID\" FROM \"Film\" OFFSET floor(random()*(select count(\"FilmID\") from \"Film\")) LIMIT 1), (random()*(time '23:59:59'))::time(0))"))
        return i + 1
    except Exception as e:
        conn.rollback()
        return i

def random_performance(cur, conn, n):
    i = 0
    while i < n:
        i = random_one_performance(cur, i, conn)
        conn.commit()

def random_one_performance_hall(cur, i, conn):
    try:
        cur.execute(sql.SQL("insert into \"Performance/Hall\"" + " (\"PerformanceHallID\", \"PerformanceID\", \"HallID\") values (trunc(random()*1000000)::int, (SELECT \"PerformanceID\" FROM \"Performance\" OFFSET floor(random()*(select count(\"PerformanceID\") from \"Performance\")) LIMIT 1), (SELECT \"HallID\" FROM \"Hall\" OFFSET floor(random()*(select count(\"HallID\") from \"Hall\")) LIMIT 1))"))
        return i + 1
    except Exception as e:
        conn.rollback()
        return i

def random_performance_hall(cur, conn, n):
    i = 0
    while i < n:
        i = random_one_performance_hall(cur, i, conn)
        conn.commit()

def random_one_ticket(cur, i, conn):
    try:
        cur.execute(sql.SQL("insert into \"Ticket\"" + " (\"TicketID\", \"Seat\", \"Row\", \"PerformanceHallID\") values (trunc(random()*1000000)::int, trunc(random()*1000000)::int, trunc(random()*10000)::int, (SELECT \"PerformanceHallID\" FROM \"Performance/Hall\" OFFSET floor(random()*(select count(\"PerformanceHallID\") from \"Performance/Hall\")) LIMIT 1))"))
        return i + 1
    except Exception as e:
        conn.rollback()
        return i

def random_ticket(cur, conn, n):
    i = 0
    while i < n:
        i = random_one_ticket(cur, i, conn)
        conn.commit()

def select(cur, columns, table, condition):
    cur.execute(sql.SQL("select " + columns + " from " + table + " where " + condition))

