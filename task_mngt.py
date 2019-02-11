from database import *


def add_task(task_name, task_description, task_method_test):
    try:
        query_db_insert("INSERT INTO Tasks(name_task, task, method_for_test) Values(\"%s\",\"%s\", \"%s\")" %(task_name, task_description, task_method_test))
    except:
        return False
    return True

def update_task(task_name, task_description, task_method_test):
    try:
        query_db_insert("Update Tasks set task=\"%s\" where name_task='%s' " %(task_description, task_name))
        query_db_insert("Update Tasks set method_for_test=\"%s\" where name_task='%s' " %(task_method_test, task_name))

    except:
        return False
    return True

def get_test_method(task_name):
    test_method = query_db('select method_for_test from Tasks where name_task=\"%s\"' % task_name)
    try:
        test_method = test_method[0][0]
    except:
        test_method = ""
    return test_method


def remove_task(task_name):
    try:
        print "test"
        query_db_insert("delete from Tasks where name_task=\"%s\"" %task_name)
    except:
        return False
    return True

def execute_task():
    pass


def add_result_to_db():
    pass


def get_results_from_db():
    pass


def analyse_of_results():
    pass


def create_report():
    pass

def get_text_task(name_task):
    text = query_db('select task from Tasks where name_task=\"%s\"'% name_task)
    try:
        text = text[0][0]
    except:
        text = ""
    return text

def get_list_tasks():
    list_tasks = [] 
    for _ in query_db("Select name_task from Tasks"):
        list_tasks.append(_[0])
    
    return list_tasks

def generate_data():
    pass


def check_if_ok():
    pass

