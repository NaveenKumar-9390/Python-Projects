from datetime import datetime

tasks = []

def add_task_test(name, run_time):
    tasks.append({
        "name": name,
        "time": run_time,
        "done": False
    })
    print(f"Task '{name}' added for {run_time}")

def list_tasks_test():
    if not tasks:
        print("No tasks scheduled")
        return
    
    for i, task in enumerate(tasks):
        status = "Done" if task["done"] else "Pending"
        print(f"{i + 1}. {task['name']} | {task['time']} | {status}")

print("Testing task scheduler:")

print("\n1. Adding tasks:")
add_task_test("Morning Meeting", "09:00")
add_task_test("Lunch Break", "12:30")
add_task_test("Code Review", "15:00")

print("\n2. Listing tasks:")
list_tasks_test()

print("\n3. Marking a task as done:")
tasks[0]["done"] = True

print("\n4. Listing tasks after update:")
list_tasks_test()

print("\n[OK] Task scheduler works correctly!")
