# To-do list manager
tasks = []

# Function to summarize tasks
def summarize_tasks(tasks):
    completed = sum(1 for task in tasks if task["done"])
    if completed == len(tasks) and tasks:
        print("All tasks completed!")
    return completed

# Lambda to estimate total time based on task count
est_time = lambda num_tasks: num_tasks * 10  # 10 minutes per task

# Main loop
print("Welcome to the To-Do List Manager!")
while True:
    print("\n1. Add task")
    print("2. Mark task as done")
    print("3. View tasks and quit")
    choice = input("Enter your choice (1-3): ")
    
    if choice == "1":
        task_name = input("Enter task name: ")
        tasks.append({"name": task_name, "done": False})
        print(f"Added task: {task_name}")
    
    elif choice == "2":
        if not tasks:
            print("No tasks to mark!")
            continue
        print("Tasks:")
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Not done"
            print(f"{i}. {task['name']} - {status}")
        task_num = input("Enter task number to mark as done: ")
        if not task_num.isdigit() or not 1 <= int(task_num) <= len(tasks):
            print("Invalid task number!")
            continue
        tasks[int(task_num)-1]["done"] = True
        print(f"Marked '{tasks[int(task_num)-1]['name']}' as done.")
    
    elif choice == "3":
        break
    else:
        print("Please enter 1, 2, or 3!")

# Show summary
completed = summarize_tasks(tasks)
print(f"\n--- To-Do List Summary ---")
for i, task in enumerate(tasks, 1):
    status = "Done" if task["done"] else "Not done"
    print(f"Task {i}: {task['name']} - {status}")
print(f"Completed {completed} out of {len(tasks)} tasks")
print(f"Estimated time for remaining tasks: {est_time(len(tasks) - completed)} minutes")