
        
class Queue:
    def __init__(self):
        self.queue=[]

    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return  len(self.queue)==0
    
    def enque(self,item):
        self.queue.append(item)
        print("item appended")

    def deque(self):
        if not self.is_empty():
            self.queue.pop(0)
            print("item removed")
        else:
            print("Queue is empty ")

    def search(self,item):
        if item in self.queue:
            print(f"{item} found at index:{self.queue.index(item)}")

    def peek(self):
        if not self.is_empty():
            print("the First in the queue is:",self.queue[0])



def q_stats(q):
    print("size of queue:",q.size())
    print("Is the queue empty:",q.is_empty())
daily_queue=Queue()
daily_queue.enque("akash")
daily_queue.enque("avhijith")
daily_queue.enque("arjun")
daily_queue.enque("ashin")
q_stats(daily_queue)
daily_queue.search("ashin")
daily_queue.deque()
q_stats(daily_queue)
daily_queue.peek()

# PS C:\Users\303372\Documents\UST Tasks> & C:\Users\303372\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/303372/Documents/UST Tasks/DAY4/Queue"
# item appended
# item appended
# item appended
# item appended
# size of queue: 4
# Is the queue empty: False
# ashin found at index:3
# item removed
# size of queue: 3
# Is the queue empty: False
# the First in the queue is: avhijith