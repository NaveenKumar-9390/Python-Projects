class Node:

    def __init__(self, name):
        self.name = name
        self.store = {}

    def put(self, key, value):
        self.store[key] = value

    def get(self, key):
        return self.store.get(key, "Key not found")

    def delete(self, key):
        if key in self.store:
            del self.store[key]
            return "Deleted"
        return "Key not found"

    def show(self):
        print(self.name, ":", self.store)
