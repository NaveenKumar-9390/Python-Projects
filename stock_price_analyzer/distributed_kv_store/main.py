import hashlib
from node import Node


nodes = [
    Node("Node1"),
    Node("Node2"),
    Node("Node3")
]


def get_node(key):
    hash_value = int(hashlib.md5(key.encode()).hexdigest(), 16)
    index = hash_value % len(nodes)
    return nodes[index]


def put():
    key = input("Key: ")
    value = input("Value: ")
    node = get_node(key)
    node.put(key, value)
    print("Stored in", node.name)


def get():
    key = input("Key: ")
    node = get_node(key)
    print("Value:", node.get(key))


def delete():
    key = input("Key: ")
    node = get_node(key)
    print(node.delete(key))


def show():
    for n in nodes:
        n.show()


def main():
    while True:
        print("\n1 PUT")
        print("2 GET")
        print("3 DELETE")
        print("4 SHOW NODES")
        print("5 EXIT")

        choice = input("Choice: ")

        if choice == "1":
            put()
        elif choice == "2":
            get()
        elif choice == "3":
            delete()
        elif choice == "4":
            show()
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
