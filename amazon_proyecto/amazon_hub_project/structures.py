from collections import deque

# ARRAY → Inventario fijo
class Inventory:
    def __init__(self):
        self.shelves = [
            "Electrónica",
            "Ropa",
            "Hogar",
            "Libros",
            "Juguetes"
        ]

# COLA → FIFO
class OrderQueue:
    def __init__(self):
        self.queue = deque()

    def receive_order(self, order):
        self.queue.append(order)

    def dispatch_order(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def get_all(self):
        return list(self.queue)

# PILA → LIFO
class TruckStack:
    def __init__(self):
        self.stack = []

    def load_truck(self, order):
        self.stack.append(order)

    def deliver_package(self):
        if self.stack:
            return self.stack.pop()
        return None

    def get_all(self):
        return self.stack