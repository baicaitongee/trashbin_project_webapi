import sqlite3
from sqlite3 import Error
class_a=0
class_b=0
class_c=0
class_d=0

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_project(conn, project):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' REPLACE INTO person(name,passwd,amount)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    return cur.lastrowid


def create_task(conn, task):
    """
    Create a new task
    :param conn:
    :param task:
    :return:
    """

    sql = ''' REPLACE INTO trash(id,class_a,class_b,class_c,class_d)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    return cur.lastrowid


def update_data(class_a_add,class_b_add,class_c_add,class_d_add):
    database = r"./pythonsqlite.db"
    global class_a
    global class_b
    global class_c
    global class_d

    class_a+=class_a_add
    class_b+=class_b_add
    class_c+=class_c_add
    class_d+=class_d_add
    sum=class_a + class_b +class_c+class_d
    # create a database connection
    conn = create_connection(database)
    with conn:
        # create a new project
        # project = ('Cool App with SQLite & Python', '2015-01-01', '2015-01-30');
        # project_id = create_project(conn, project)

        # tasks
        task_1 = ('baicaitong',123456,sum)
        task_2 = (1,class_a,class_b,class_c,class_d)

        # create tasks
        create_project(conn, task_1)
        create_task(conn, task_2)


