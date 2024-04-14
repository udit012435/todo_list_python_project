class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, due_date=None, priority=None):
        self.tasks.append({"task": task, "due_date": due_date, "priority": priority})

    def view_tasks(self):
        if self.tasks:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task['task']}")
                if task['due_date']:
                    print(f"   Due Date: {task['due_date']}")
                if task['priority']:
                    print(f"   Priority: {task['priority']}")
        else:
            print("No tasks.")

    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            del self.tasks[index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task: ")
            due_date = input("Enter due date (optional): ")
            priority = input("Enter priority (optional): ")
            todo_list.add_task(task, due_date, priority)
        elif choice == '2':
            print("\nTasks:")
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter task index to delete: "))
            todo_list.delete_task(index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
