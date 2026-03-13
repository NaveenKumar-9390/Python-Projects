from collections import OrderedDict

class DynamicLRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        
        # Mark as recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # Update & mark as recent
            self.cache.move_to_end(key)

        self.cache[key] = value

        # Evict if over capacity
        while len(self.cache) > self.capacity:
            removed = self.cache.popitem(last=False)
            print("Evicted:", removed)

    def set_capacity(self, new_capacity):
        print(f"Changing capacity from {self.capacity} -> {new_capacity}")
        self.capacity = new_capacity

        # Remove extra items if new capacity is smaller
        while len(self.cache) > self.capacity:
            removed = self.cache.popitem(last=False)
            print("Evicted due to resize:", removed)

    def display(self):
        print("Cache:", self.cache)


# ------------------ Demo ------------------
if __name__ == "__main__":
    lru = DynamicLRUCache(3)

    lru.put(1, "A")
    lru.put(2, "B")
    lru.put(3, "C")
    lru.display()

    lru.get(1)   # access 1 → most recent
    lru.display()

    # Increase capacity dynamically
    lru.set_capacity(5)
    lru.put(4, "D")
    lru.put(5, "E")
    lru.display()

    # Decrease capacity dynamically
    lru.set_capacity(2)
    lru.display()