from database import  *


def add_user():
    pass


def get_user_password(user_name):
    passwd = query_db("select password from Users where login=\"%s\"" % user_name)
    print passwd
    return passwd[0][0]


def set_password(password, user_name):
    pass


def check_password(password, user_name):
    print (get_user_password(user_name) == password)
    return (get_user_password(user_name) == password)


def set_is_login(user_name):
    try:
        query_db_insert("update Users set is_logged=1 where login=\"%s\"" % user_name)
    except:
        return False
    return True


def loging(user_name, password):
    print "test"
    if check_password(password, user_name):
        return set_is_login(user_name)
    return False


def logout(user_name):
    try:
        query_db_insert("update Users set is_logged=0 where login=\"%s\"" % user_name)
    except:
        return False
    return True


def if_logged(user_name):
    logged = query_db("select is_logged from Users where login=\"%s\"" % user_name)
    print logged
    return logged[0][0]



