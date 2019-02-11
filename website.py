import flask
import sqlite3
import time_calculation
from user_mngt import *
from database import *
import theory_mngt
import task_mngt
import feedback_mgnt
FLAG_create_database = False
add_seperator= "<br><br><br><br><br><br><br>"


app = flask.Flask(__name__)


@app.route("/")
@app.route("/main_page")
def main():
    return flask.render_template("main_page.html")


@app.route('/submit', methods=['POST', "GET"])
def submit():
    test_description = flask.request.form['text']
    name = flask.request.form['name']
    tasks_list = task_mngt.get_list_tasks()
    print name
    try:
        data = []
        exec(test_description)
    except:
        return flask.render_template("Tasks.html", tasks_list=tasks_list,
                                     text="Couldn't compile it. %s" % add_seperator)

    results = time_calculation.testing_command(test_description, name)
    exec_time = results[0]
    return flask.render_template("report.html", text=exec_time)


@app.route("/main_admin")
def main_admin():
    comments = feedback_mgnt.get_comments()
    if not comments:
        comments = ["No comments"]

    return flask.render_template("main_page_admin.html", comments=comments)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if not if_logged("admin"):
        return flask.render_template("login_page.html")
    else:
        logout("admin")
        return flask.render_template("main_page.html")


@app.route("/create_task", methods=['GET', 'POST'])
def create_task():
    tasks_list = task_mngt.get_list_tasks()
    return flask.render_template("create_task.html", tasks_list=tasks_list)


@app.route("/update_task", methods=['GET', 'POST'])
def update_task():
    tasks_list = task_mngt.get_list_tasks()
    return flask.render_template("pick_update_task.html", tasks_list=tasks_list)


@app.route("/remove_task", methods=['GET', 'POST'])
def remove_task():
    tasks_list = task_mngt.get_list_tasks()
    return flask.render_template("remove_task.html", tasks_list=tasks_list)


@app.route("/add_comment", methods=['GET', 'POST'])
def add_comment():
    try:
        comment_text =  flask.request.form["comments"]
    except:
        return flask.render_template("main_page.html")
    feedback_mgnt.add_comment(comment_text)
    return flask.render_template("main_page.html")


@app.route("/create_theory", methods=['GET', 'POST'])
def create_theory():
    theory_list = theory_mngt.get_list_theory()
    return flask.render_template("create_theory.html", theory_list=theory_list)


@app.route("/remove_theory", methods=['GET', 'POST'])
def remove_theory():
    theory_list = theory_mngt.get_list_theory()
    return flask.render_template("remove_theory.html", theory_list=theory_list)


@app.route("/update_theory", methods=['GET', 'POST'])
def update_theory():
    theory_list = theory_mngt.get_list_theory()
    return flask.render_template("pick_update_theory.html", theory_list=theory_list)


@app.route('/process', methods=['POST'])
def process():
    print "test"
    name = flask.request.form['login']
    password  = flask.request.form['password']
    if loging(name, password):
        return flask.redirect(flask.url_for('main_admin'))
    return flask.redirect(flask.url_for('main'))


@app.route("/tasks", methods=['GET', 'POST'])
def tasks():    
    tasks_list = task_mngt.get_list_tasks()
    if if_logged("admin"):
        return flask.render_template("Tasks-admin.html", tasks_list = tasks_list,
                                     text = "Choose tasks from the list %s "% add_seperator)
    return flask.render_template("Tasks.html", tasks_list = tasks_list,
                                 text = "Choose tasks from the list %s "% add_seperator)


@app.route("/theory", methods=['GET', 'POST'])
def theory():
    theory_list = theory_mngt.get_list_theory()
    if not if_logged("admin"):
        return flask.render_template("Theory.html", theory_list=theory_list)
    else:
        return flask.render_template("Theory-admin.html", theory_list=theory_list)


@app.route('/task_get', methods=['POST', "GET"])
def task_get():
    get_task_name =  flask.request.form['name']
    tasks_list = task_mngt.get_list_tasks()
    task_text =  task_mngt.get_text_task(get_task_name)
    return flask.render_template("Tasks.html", text=task_text, task_name=get_task_name,tasks_list =tasks_list )


@app.route('/theory_get', methods=['POST', "GET"])
def theory_get():
    theory_name = flask.request.form['name']
    theory_list = theory_mngt.get_list_theory()
    theory_text =  theory_mngt.get_text_theory(theory_name)
    return flask.render_template("Theory.html", theory_list=theory_list, text=theory_text)


@app.route('/addtask', methods=['POST', "GET"])
def addtask():
    task_name = flask.request.form['taskname']
    task_description =  flask.request.form['description']
    task_test_method =  flask.request.form['testmethod']
    task_mngt.add_task(task_name, task_description.strip(), task_test_method)

    tasks_list = task_mngt.get_list_tasks()
    print tasks_list
    return flask.render_template("Tasks-admin.html", text="Choose tasks from the list %s " % add_seperator,  tasks_list=tasks_list)


@app.route('/removetask', methods=['POST', "GET"])
def removetask():
    task_name = flask.request.form['name']
    print task_name
    task_mngt.remove_task(task_name)
    tasks_list = task_mngt.get_list_tasks()
    return flask.render_template("Tasks-admin.html", text="Choose tasks from the list %s " % add_seperator, tasks_list=tasks_list)


@app.route('/pick_to_update_task', methods=['POST', "GET"])
def pick_to_update_task():
    task_name = flask.request.form['name']
    task_list = task_mngt.get_list_tasks()
    task_desc = task_mngt.get_text_task(task_name)
    test_method = task_mngt.get_test_method(task_name)
    return flask.render_template("update_task.html", tasks_list=task_list,
                                 text=task_desc, task_name=task_name, test_method=test_method)


@app.route('/updatetask', methods=['POST', "GET"])
def updatetask():
   task_name = flask.request.form['task_name']
   description = flask.request.form['description']
   method_test = flask.request.form['testmethod']
   task_mngt.update_task(task_name, description, method_test)
   tasks_list = task_mngt.get_list_tasks()
   return flask.render_template("Tasks-admin.html", text="Choose tasks from the list %s " % add_seperator,
                                tasks_list=tasks_list)


@app.route('/addtheory', methods=['POST', "GET"])
def addtheory():
    theory_name =  flask.request.form['theory_name']
    description =  flask.request.form['description']
    theory_mngt.add_theory(theory_name, description.strip())
    theory_list = theory_mngt.get_list_theory()
    return flask.render_template("Theory-admin.html" , text="Choose theory from the list",  theory_list=theory_list)


@app.route('/removetheory', methods=['POST', "GET"])
def removetheory():
     theory_name =  flask.request.form['name']
     print theory_name
     theory_mngt.remove_theory(theory_name)
     theory_list = theory_mngt.get_list_theory()
     print theory_list
     return flask.render_template("Theory-admin.html", text="Choose theory from the list", theory_list=theory_list)


@app.route('/pick_to_update', methods=['POST', "GET"])
def pick_to_update():
    theory_name = flask.request.form['name']
    theory_list = theory_mngt.get_list_theory()
    theory_text = theory_mngt.get_text_theory(theory_name)
    return flask.render_template("update_theory.html", theory_list=theory_list,
                                 text=theory_text, theory_name=theory_name)


@app.route('/updatetheory', methods=['POST', "GET"])
def updatetheory():
   theory_name = flask.request.form['name']
   theory_desc = flask.request.form['description']
   theory_mngt.update_theory(theory_name, theory_desc)
   theory_list = theory_mngt.get_list_theory()
   return flask.render_template("Theory-admin.html", text="Choose theory from the list", theory_list=theory_list)


def session():
    pass


if __name__ == "__main__":
    session() 
    if not FLAG_create_database:
        FLAG_create_database = True
        create_database()
    app.run(debug=True)

