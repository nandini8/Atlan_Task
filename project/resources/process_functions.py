"""
Program to terminate/pause/resume a process
0 signifies TERMINATE
1 signifies START
2 signifies PAUSE
3 signifies RESUME
"""


from multiprocessing import Process, Value
from time import sleep

def worker(run, function, data):
    index = 0
    ch = True
    while ch:
        if run.value == 3 or run.value == 1:
            function(data)
        elif run.value == 0:
            ch = False
            print("Terminated")
            return
        elif run.value == 2:
            print("Paused", index)
            
        
def main_run(function, data, cancel):
    # run = Value("i", cancel)
    run = cancel
    p = Process(target=worker, args=(run, function, data))
    p.start()
    while True:
        if run.value == 0:
            print("Terminated")
            # sleep(1)
            p.terminate()
            p.join()
            break


# if __name__ == '__main__':
#     main_run()