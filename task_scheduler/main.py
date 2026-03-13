import time
from datetime import datetime

tasks = []


def add_task():

    name = input("Task name: ")
    run_time = input("Run time (HH:MM): ")

    tasks.append({
        "name": name,
        "time": run_time,
        "done": False
    })

    print("Task added")


def list_tasks():

    if not tasks:
        print("No tasks scheduled")
        return

    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(i + 1, task["name"], "|", task["time"], "|", status)


def run_scheduler():

    print("Scheduler started...")

    while True:

        now = datetime.now().strftime("%H:%M")

        for task in tasks:

            if task["time"] == now and not task["done"]:

                print("\nRunning task:", task["name"])
                task["done"] = True

        time.sleep(30)


def main():

    while True:

        print("\n1 Add Task")
        print("2 List Tasks")
        print("3 Start Scheduler")
        print("4 Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            run_scheduler()

        elif choice == "4":
            break


if __name__ == "__main__":
    main()
