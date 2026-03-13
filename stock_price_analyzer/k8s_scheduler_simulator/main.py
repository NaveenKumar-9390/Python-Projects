class Node:

    def __init__(self, name, cpu):
        self.name = name
        self.cpu_total = cpu
        self.cpu_used = 0
        self.tasks = []

    def can_schedule(self, cpu_req):
        return self.cpu_used + cpu_req <= self.cpu_total

    def schedule(self, task):
        self.tasks.append(task["name"])
        self.cpu_used += task["cpu"]

    def show(self):
        print(
            self.name,
            "| CPU:", self.cpu_used, "/", self.cpu_total,
            "| Tasks:", self.tasks
        )


class Scheduler:

    def __init__(self):
        self.nodes = []

    def add_node(self):
        name = input("Node name: ")
        cpu = int(input("CPU capacity: "))
        self.nodes.append(Node(name, cpu))
        print("Node added")

    def schedule_task(self):
        task_name = input("Task name: ")
        cpu_req = int(input("CPU required: "))
        task = {"name": task_name, "cpu": cpu_req}

        for node in self.nodes:
            if node.can_schedule(cpu_req):
                node.schedule(task)
                print("Task scheduled on", node.name)
                return

        print("No node has enough resources")

    def show_cluster(self):
        print("\nCluster Status")
        for node in self.nodes:
            node.show()


def main():

    scheduler = Scheduler()

    while True:

        print("\n1 Add Node")
        print("2 Schedule Task")
        print("3 Show Cluster")
        print("4 Exit")

        choice = input("Choice: ")

        if choice == "1":
            scheduler.add_node()

        elif choice == "2":
            scheduler.schedule_task()

        elif choice == "3":
            scheduler.show_cluster()

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
