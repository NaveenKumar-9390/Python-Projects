class MemoryAllocator:

    def __init__(self, size):
        self.memory = [0] * size
        self.size = size


    def allocate(self, block_size):

        count = 0
        start = -1

        for i in range(self.size):

            if self.memory[i] == 0:

                if count == 0:
                    start = i

                count += 1

                if count == block_size:

                    for j in range(start, start + block_size):
                        self.memory[j] = 1

                    print("Allocated at index:", start)
                    return start

            else:
                count = 0

        print("Not enough memory")
        return -1


    def free(self, start, block_size):

        for i in range(start, start + block_size):

            if i < self.size:
                self.memory[i] = 0

        print("Memory freed")


    def show_memory(self):

        print("Memory:", self.memory)


def main():

    allocator = MemoryAllocator(20)

    while True:

        print("\n1 Allocate")
        print("2 Free")
        print("3 Show Memory")
        print("4 Exit")

        choice = input("Choice: ")

        if choice == "1":

            size = int(input("Block size: "))
            allocator.allocate(size)

        elif choice == "2":

            start = int(input("Start index: "))
            size = int(input("Block size: "))
            allocator.free(start, size)

        elif choice == "3":

            allocator.show_memory()

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
