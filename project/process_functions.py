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

def worker(run):
    count = 0
    ch = True
    while ch:
        if run.value == 2:
            count = do_work(count)
        elif run.value == 0:
            return
        elif run.value == 1:
            pass
        
if __name__ == "__main__":
    run = Value("i", 2)
    p = Process(target=worker, args=(run,))
    p.start()
    while True:
        process = int(input("0, 1, 2\n"))
        run.value = process
        if process == 0:
            print("Terminated")
            p.join()
            break