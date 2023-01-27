from queue import Queue
from functools import partial

eventloop = None

class Eventloop(Queue):
    def start(self):
        function = self.get()
        function()

def do_hello():
    global eventloop
    print("Hello")
    eventloop.put(do_world)

def do_world():
    global eventloop
    print("world")
    eventloop.put(do_hello)

if __name__ == "__main__":
    eventloop = Eventloop()
    eventloop.put(do_hello)
    eventloop.start()
