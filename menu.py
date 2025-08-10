import os
from task_db import TaskDB, TaskDB_Manager


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_user():
    input("\nPush Enter, to continue...")

def print_menu():
    clear_screen()
    print("===== Task Manager Menu =====")
    print("1. Show tasks")
    print("2. Add new task")
    print("3. Find task")
    print("4. Change task")
    print("5. Mark as done")
    print("6. Mark as not done")
    print("7. Delete task")
    print("0. Exit")
    print("===========================")


def show_all_tasks(manager: TaskDB_Manager):
    clear_screen()
    print("--- All tasks ---")
    tasks = manager.get_all_tasks()
    if not tasks:
        print("List is empty")
    else:
        for task in tasks:
        
            print(task)
    wait_for_user()

def show_done_tasks(manager: TaskDB_Manager):
    clear_screen()
    print("--- All complete tasks ---")
    tasks = manager.get_all_tasks()
    if not tasks:
        print("List is empty")
    else:
        for task in tasks:        
            if task.status == 'done':
                print(task)
    wait_for_user()


def show_not_done_tasks(manager: TaskDB_Manager):
    clear_screen()
    print("--- All complete tasks ---")
    tasks = manager.get_all_tasks()
    if not tasks:
        print("List is empty")
    else:
        for task in tasks:        
            if task.status == 'not done':
                print(task)
    wait_for_user()

def add_new_task(manager: TaskDB_Manager):
    clear_screen()
    print("--- Add new task ---")
    title = input("Enter the title: ")
    description = input("Enter the description: ")
    if title:
        manager.add_task(title, description)
    else:
        print("Title can not be empty!")
    wait_for_user()

def find_task(manager: TaskDB_Manager):
    clear_screen()
    print("--- Task search ---")
    value = input("search: ")
    tasks = manager.find_by_all_parametrs(value)
    if tasks:
        for task in tasks:
            print(task)
        task_id = input("Enter id: ")
        task = manager.get_task_by_id(task_id)
        if task:
            print(task)
        else:
            print("There no task with that id")
    else:
        print("There are nothing")

    wait_for_user()

def update_existing_task(manager: TaskDB_Manager):
    clear_screen()
    print("--- Search task ---")
    value = input("Search: ")
    tasks = manager.find_by_all_parametrs(value)
    if tasks:
        for task in tasks:
            print(task)
        task_id = input("Enter id: ")
        task = manager.get_task_by_id(task_id)
        if task:
            print("Current details:")
            print(task)
            print("\nEnter new details (leave empty to leave unchangable).")
            new_title = input(f"New title (current: '{task.title}'): ")
            new_description = input(f"New description (current: '{task.description}'): ")
            
        
            title_to_update = new_title if new_title else None
            desc_to_update = new_description if new_description else None

            if title_to_update or desc_to_update:
                manager.update_task(value, title=title_to_update, description=desc_to_update)
            else:
                print("no data for updating")
        else:
            print("There no task with that id")
    else:
        print("There are nothing")

    wait_for_user()

def complete_a_task(manager: TaskDB_Manager):
    clear_screen()
    print("--- Mark task as done ---")
    show_not_done_tasks(manager)
    task_id = input("Enter task id for mark it as done: ")
    manager.complete_task(task_id)
    wait_for_user()

def reopen_a_task(manager: TaskDB_Manager):
    clear_screen()
    print("--- Mark task as not done ---")
    show_done_tasks(manager)
    task_id = input("Enter task id for mark it as not done: ")
    manager.reopen_task(task_id)
    wait_for_user()

def delete_a_task(manager: TaskDB_Manager):
    clear_screen()
    print("--- Delete task ---")
    show_all_tasks(manager)
    task_id = input("Enter task id for deleting: ")
    manager.delete_task(task_id)
    wait_for_user()



def main():
    db = TaskDB()
    manager = TaskDB_Manager(db)

    while True:
        print_menu()
        choice = input("Choose option: ")

        if choice == '1':
            show_all_tasks(manager)
        elif choice == '2':
            add_new_task(manager)
        elif choice == '3':
            find_task(manager)
        elif choice == '4':
            update_existing_task(manager)
        elif choice == '5':
            complete_a_task(manager)
        elif choice == '6':
            reopen_a_task(manager)
        elif choice == '7':
            delete_a_task(manager)
        elif choice == '0':
            print("Exit")
            break
        else:
            print("Invalid choice.")
            wait_for_user()

if __name__ == "__main__":
    main()