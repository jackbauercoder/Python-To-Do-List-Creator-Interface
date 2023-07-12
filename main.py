import tkinter as tk

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.todo_list = ToDoList()

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=10)

        add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        add_button.pack(pady=5)

        remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        remove_button.pack(pady=5)

        self.task_listbox = tk.Listbox(self.root, width=50)
        self.task_listbox.pack()

        self.update_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)

    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task = self.task_listbox.get(selected_task)
            self.todo_list.remove_task(task)
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        tasks = self.todo_list.get_tasks()
        for task in tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
