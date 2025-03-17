"""
队列的python实现
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self) -> bool:
        return self.items == []
    
    def size(self) -> int:
        return len(self.items)