import sqlite3


def query_db(query):
    conn = sqlite3.connect('inzynierka.db')
    c = conn.cursor()
    cur = c.execute(query)
    rv = cur.fetchall()
    cur.close()
    return rv if rv else None


def query_db_insert(query):
    conn = sqlite3.connect('inzynierka.db')
    c = conn.cursor()
    cur = c.execute(query)
    conn.commit()
    cur.close()

def basic_data_tasks():
    description_search = "The task is to find an element in the list. <br><br> For example if there is a list: " \
                         " <br><br> [10,29,21,42] <br><br> and the task is to find number  29 <br><br>" \
                         " Then the task is to" \
                         "provide an algorithm which will <br> check whether the number is on the list <br> and return the " \
                         "index of the number. <br> The task is to find number  <b> 29 </b>. "
    description_sort = "The task is to sort the list from the smallest value to the biggest. <br><br>" \
                       " For example if there is a list: " \
                         " <br><br> [10,29,21,42]<br><br> the result should be:" \
                       " <br><br> [10,21,29,42] <br><br>" \
                         " Then the task is to" \
                         "provide an algorithm which will <br> sort the list <br> and return the " \
                         "sorted list.<br> "
    script_test = "search=29 \n" \
                  "test = data.index(search) if (search in data) else -1 \n" \
                  "print test"
    query_db_insert("INSERT INTO Tasks (name_task, task, method_for_test) Values('Searching', '%s', '%s')" % (description_search, script_test))
    query_db_insert("INSERT INTO Tasks (name_task, task, method_for_test) Values('Sorting', '%s', 'test = data.sort()')" % description_sort)


def basic_data_theory():
    theory_alg = "Algorithm by definition is a list of step to achieve goal."+\
        "In computer science is a collection of instructions, which should be well defined, "+\
        "clear and should be written in such a way, that computer would understand the control flow." +\
       " Algorithms should represent the best way to get expected results."+ \
        "Algorithms contains couple important features such as: <br> <br> " +\
       " \t    1. Must have a unique name <br> <br>  " + \
       " \t  2.Should have explicitly defined set of inputs and outputs <br> <br> " +\
        "\t 3.Should be well-ordered with unambiguous operations <br> <br>  " +\
        "\t    4.Algorithm has to be done in a finite amount of time <br> <br> "+\
        "\t   5.Algorithm should return the correct result <br> <br> "
    theory_python = "Python is a programming language.It is a simple language, which becomes more and more popular." + \
                    "<br> " + "It can be applied in almost every field, because it has a lot of modules. " +\
        "It is one of the most popular languages for data processing and analysis. " \
        "It has a lot of modules such as Flask, Django or CherryPy for web applications. \n " +\
        "   Python is also a big help in Artificial Intelligence and machine learning." \
        "<br> In Python we need to remember that the tabulation is extremly important, there is no {} or other signs" \
        "that would say where starts and end the function. Example of function in Python:" \
        "<br><br><br>temp_list = [1,2,3,4,5] <br> for _in temp_list: <br> &emsp;print _ <br> print temp_list " \
        "<br><br> In that code there is a simple printing each element of the list. But it is" \
        " important to remember that tabulation here makes huge distance"

    query_db_insert("INSERT INTO Theory(name_theory, description) Values('Algorithm','%s')"%theory_alg)
    query_db_insert("INSERT INTO Theory(name_theory, description) Values('Python','%s')"%theory_python)


def create_database():
    conn = sqlite3.connect('inzynierka.db')
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS Users;')
    c.execute('CREATE TABLE Users (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT , role text NOT NULL, login text not NULL, password text not NULL, is_logged bit NOT NULL DEFAULT (0), last_login DATETIME)')
    c.execute('DROP TABLE IF EXISTS Tasks;')
    c.execute('CREATE TABLE Tasks (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name_task text NOT NULL,  task text not NULL, method_for_test text not NULL)')
    c.execute('DROP TABLE IF EXISTS Results;')
    c.execute('CREATE TABLE Results(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, user_id INTEGER, task_id INTEGER, FOREIGN KEY(user_id) REFERENCES Users(ID), FOREIGN KEY(task_id) REFERENCES Tasks(ID))')
    c.execute('DROP TABLE IF EXISTS Theory;')
    c.execute('DROP TABLE IF EXISTS Comments;')
    c.execute('CREATE TABLE Comments(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, comment text not NULL)')
    c.execute('CREATE TABLE Theory(ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name_theory text NOT NULL, description text)')
    c.execute("INSERT INTO Users(role, login, password) Values('admin', 'admin', 'admin')")

    conn.commit()
    c.close()
    basic_data_theory()
    basic_data_tasks()

create_database()
query_db_insert("INSERT INTO Theory(name_theory, description) Values('admin1', 'admin1')")
name_theory="admin1"
query_db_insert("delete from Theory where name_theory='%s'" % (name_theory))
print query_db("select * from Theory")