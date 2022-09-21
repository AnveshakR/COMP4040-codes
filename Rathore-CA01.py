class Node:
    def __init__(self, value):
        # initializing node and its characteristics

        self.value = value # data contained by the node
        self.next = None # pointer to the location of the next node

class Queue:
    def __init__(self):
        # initializing a queue and its characteristics

        self.head = self.tail = None # head and tail point to the front and back of the queue respectively
        self.size = 0 #size of the queue

    def __str__(self):
        # function for traversing and printing the queue

        cursor = self.head
        op = ""
        while cursor:
            op += " - " + (str(cursor.value))[::-1]
            cursor = cursor.next
        return ("(tail) " + op[::-1][:-3] + " (head)")

    def getSize(self):
        # function to get the size of the queue

        return self.size

    def isEmpty(self):
        # function to check if the queue is empty

        return self.size == 0

    def Enqueue(self, item):
        # function to add a node to the tail of the queue

        print("Enqueued")
        node = Node(item)
        self.size += 1
        if self.tail == None:
            self.head = self.tail = node # if queue is empty, make the incoming node both the head and tail

            print("Queue: ", self)
            return

        self.tail.next = node # if queue has items, point the earlier tail node to the new node
        self.tail = node # and then set the queue's tail to the new node

        print("Queue: ", self)
        return

    def DeQueue(self):
        # function to remove the node at the front of the queue

        if self.isEmpty(): # checking if queue is empty because you cant dequeue an empty queue
            print("Queue empty")
            return

        print("Dequeued")

        node = self.head # "relocating" the head node to a different variable
        self.head = node.next # pointing the head of the queue to the "next" node of the former head of the queue

        if self.head == None: # if front of the queue is None, then it means the queue has become empty
            self.rear = None # so we set the rear of the queue as None to match

        print("Queue: ", self)

        self.size -= 1


if __name__ == "__main__":
    q = Queue()
    q.Enqueue(20)
    q.Enqueue(40)
    q.Enqueue(60)
    q.DeQueue()
    q.DeQueue()
    q.Enqueue(100)