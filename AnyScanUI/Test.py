from attack.AttackObject import AttackObject

from attack.AttackBase import AttackBase
import  threading,Queue,time

threads_queue = Queue.Queue(maxsize = 10)


class Attacker2(threading.Thread):
    def run(self):
        print 2
        threads_queue.get()

class Attacker1(threading.Thread):
    def run(self):
        print 1
        threads_queue.get()

if __name__ == "__main__":
    for i in range(0,10):
        threads_queue.put("")
    print threads_queue.qsize()
    threads_queue.queue.clear()
    print threads_queue.qsize()