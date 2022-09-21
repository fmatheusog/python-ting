class Queue:
    def __init__(self):
        self.queue = list()

    def __len__(self):
        self.queue.count()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        self.queue.pop()

    def search(self, index):
        result = self.queue[index]

        if (result is None):
            raise IndexError
        else:
            return result
