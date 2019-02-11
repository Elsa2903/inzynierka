from database import *


def add_theory(name, theory):
    try:
        query_db_insert("INSERT INTO Theory(name_theory, description) Values('%s','%s')" % (name, theory))
    except:
        return False
    return True


def remove_theory(name_theory):
    print name_theory
    try:
        query_db_insert("delete from Theory where name_theory='%s'"%(name_theory))
        print "its done"
    except:
        return False
    return True


def update_theory(name, theory):
    try:
        query_db_insert("Update Theory set description='%s' where name_theory='%s'" % (theory, name))
    except:
        return False
    return True


def get_text_theory(name_theory):
    text = query_db('select description from Theory where name_theory=\"%s\"'% name_theory)
    try:
        text = text[0][0]
    except:
        text = ""
    return text


def get_list_theory():
    list_tasks = [] 
    for _ in query_db("Select name_theory from Theory"):
        list_tasks.append(_[0])
    
    return list_tasks
