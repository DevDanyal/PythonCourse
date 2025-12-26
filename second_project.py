def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully")

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(i, task)

def delete_task():
    num = int(input("Enter task number to delete: "))
    tasks.pop(num - 1)

while True:
    print("1. Add  2. Show  3. Delete  4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        break
