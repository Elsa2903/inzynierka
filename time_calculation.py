import timeit
import datetime
import random
import math
import matplotlib.pyplot as plot
from subprocess import Popen, PIPE
import os
import numpy 
from timeit import default_timer as timer


def exec_command(cmd, data):
    start = timer()
    exec(cmd)
    exec_time1 = timer() - start
    return round(exec_time1, 4)


def random_gen(n, a, b):
    temp = []
    for _ in range(n):
        temp.append(random.randint(a, b))
    return temp


def testing_command(cmd, name):
    test_ranges = [10,100,1000,10000, 100000]
    comment = ""
    exec_time_list = []
    for _ in test_ranges:
        data = random_gen(_, 0, 1000)
        exec_time = exec_command(cmd, data)
        time_expected_worst_case = _ * math.log(_)
        exec_time_list.append(exec_time)
        comment = comment + "time of execution: %s  and it should be:  %s\n " % (str(exec_time),str(time_expected_worst_case))
    print exec_time_list   
    try:
        os.remove("../static/figure.png")
        print "removed"
    except:
        print "go on"
    s = plot.plot(test_ranges, exec_time_list)
    print exec_time_list
    print s
    plot.savefig("./static/figure.png")
    plot.clf()
    return ([comment, plot])



"""
dane = random_gen(100, 0, 100)
start = time.time()
function(dane)
exec_time = time.time() - start

start = time.time()
function1(dane)
exec_time1 = ti
ame.time() - start
print(str(exec_time) + "\n" + str(exec_time1))
"""

#, 0, 1 if exec_time_list >= 0.1 else max(exec_time_list)*10