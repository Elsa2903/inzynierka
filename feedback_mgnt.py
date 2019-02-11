from database import *


def add_comment(comment):
    try:
        query_db_insert("INSERT INTO Comments(comment) Values('%s')" % (comment))
    except:
        return False
    return True


def get_comments():
    list_comments = query_db('select comment from Comments')
    comments = []
    if list_comments:
        for _ in list_comments:
            try:
                comments.append(_[0])
            except:
                pass
    return comments if comments else ["no comments"]