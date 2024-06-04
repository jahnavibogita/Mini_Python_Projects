import tkinter as tk
from tkinter import font  # Import font for customization

class ToDoList:

    def __init__(self, master):
        self.master = master
        master.title("To-Do List")

        # Create task list frame
        self.task_list_frame = tk.Frame(master)
        self.task_list_frame.pack(fill=tk.BOTH, expand=True)

        # Create task list label
        self.task_list_label = tk.Label(
            self.task_list_frame, text="Tasks:", font=font.Font(size=14, weight="bold")
        )
        self.task_list_label.pack(pady=10)

        # Create task list display area (initially empty)
        self.task_list = tk.Listbox(
            self.task_list_frame, font=font.Font(size=12), width=50, height=10
        )
        self.task_list.pack()

        # Create task input frame
        self.task_input_frame = tk.Frame(master)
        self.task_input_frame.pack(fill=tk.X, pady=10)

        # Create task entry field
        self.task_entry = tk.Entry(self.task_input_frame, font=font.Font(size=12))
        self.task_entry.pack(side=tk.LEFT, expand=True)

        # Create add task button
        self.add_button = tk.Button(
            self.task_input_frame,
            text="Add Task",
            font=font.Font(size=12),
            command=self.add_task,
        )
        self.add_button.pack(side=tk.RIGHT)

        # Create controls frame
        self.controls_frame = tk.Frame(master)
        self.controls_frame.pack(fill=tk.X, pady=10)

        # Create mark done button
        self.mark_done_button = tk.Button(
            self.controls_frame,
            text="Mark Done",
            font=font.Font(size=12),
            command=self.mark_task_done,
            state=tk.DISABLED,  # Initially disabled until a task is selected
        )
        self.mark_done_button.pack(side=tk.LEFT)

        # Create exit button
        self.exit_button = tk.Button(
            self.controls_frame, text="Exit", font=font.Font(size=12), command=self.exit
        )
        self.exit_button.pack(side=tk.RIGHT)

        # Task list (data structure)
        self.tasks = []

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"task": task_text, "done": False})
            self.update_list()
            self.task_entry.delete(0, tk.END)  # Clear entry field after adding
            self.mark_done_button.config(state=tk.NORMAL)  # Enable mark done button

    def update_list(self):
        self.task_list.delete(0, tk.END)  # Clear previous list items
        for index, task in enumerate(self.tasks):
            status = "Done" if task["done"] else "Not Done"
            self.task_list.insert(tk.END, f"{index + 1}. {task['task']} - {status}")

    def mark_task_done(self):
        selected_index = self.task_list.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.tasks[index]["done"] = True
            self.update_list()
            self.mark_done_button.config(state=tk.DISABLED)  # Disable if no task selected

    def exit(self):
        self.master.destroy()  # Close the application window

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoList(root)
    root.mainloop
