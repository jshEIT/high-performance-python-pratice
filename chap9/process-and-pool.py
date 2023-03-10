import multiprocessing
import time

class Process(multiprocessing.Process):
    def __init__(self,id):
        super(Process,self).__init__()
        self.id = id

    def run(self):
        time.sleep(1)
        print("I'm the process with id: {}".format(self.id))


if __name__ == "__main__":
    #p = Process(0)
    #p.start()
    #p.join()

    processes = Process(1), Process(2), Process(3), Process(4)
    [p.start() for p in processes]