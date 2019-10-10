"""
Program to terminate/pause/resume a process
0 signifies TERMINATE
1 signifies PAUSE
2 signifies RESUME
"""


from multiprocessing import Process, Value
from time import sleep

def do_work(count):
    print("Working... ", count)
    count += 1
    sleep(1)
    return count

def worker(run, function, data):
    count = 0
    ch = True
    while ch:
        if run.value == 2:
            function(data)
        elif run.value == 0:
            ch = False
            print("Terminator")
            return
        elif run.value == 1:
            print("Paused")
            pass
        
def main_run(function, data, cancel):
    # run = Value("i", cancel)
    run = cancel
    p = Process(target=worker, args=(run, function, data))
    p.start()
    while True:
        if run.value == 0:
            print("Terminated")
            sleep(1)
            p.terminate()
            p.join()
            break
        if run.value == 1:
            print("AAAAAAAA")

# if __name__ == '__main__':
#     main_run()