import tkinter as tk
from tkinter import messagebox
import os

# === Color palette ===
BG_COLOR = "#2f2fa2"       # Deep purple
FG_COLOR = "#f2f2f2"       # Light text
ACCENT_COLOR = "#7c83fd"   # Soft blue
BTN_COLOR = "#a29bfe"      # Lighter purple
HIGHLIGHT = "#dcd6f7"      # Light purple/blue for selection

# === Setup the main window ===
root = tk.Tk()
root.title("💜 To-Do List")
root.geometry("420x540")
root.resizable(False, False)
root.config(bg=BG_COLOR)

# === Functions ===

def add_task():
    task = task_input.get()
    if task.strip():
        task_list.insert(tk.END, task)
        task_input.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Empty Input", "Please enter a task.")

def delete_task():
    selected = task_list.curselection()
    if selected:
        task_list.delete(selected)
        save_tasks()
    else:
        messagebox.showinfo("No Selection", "Please select a task to delete.")

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = task_list.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            for line in file:
                task_list.insert(tk.END, line.strip())

# === Widgets ===

# Title
title = tk.Label(root, text="💙 My To-Do List 💜", font=("Helvetica", 20, "bold"), bg=BG_COLOR, fg=FG_COLOR)
title.pack(pady=20)

# Input
task_input = tk.Entry(root, font=("Helvetica", 14), width=25, bg=FG_COLOR, fg=BG_COLOR, relief="flat", justify="center")
task_input.pack(pady=10)

# Buttons Frame
button_frame = tk.Frame(root, bg=BG_COLOR)
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Task", command=add_task, width=12, font=("Helvetica", 12, "bold"),
                    bg=ACCENT_COLOR, fg=FG_COLOR, relief="flat", activebackground=BTN_COLOR)
add_btn.pack(side=tk.LEFT, padx=10)

delete_btn = tk.Button(button_frame, text="Delete Task", command=delete_task, width=12, font=("Helvetica", 12, "bold"),
                       bg=BTN_COLOR, fg=FG_COLOR, relief="flat", activebackground=ACCENT_COLOR)
delete_btn.pack(side=tk.LEFT, padx=10)

# Task List
task_list = tk.Listbox(root, font=("Helvetica", 13), width=35, height=15, bg=FG_COLOR, fg=BG_COLOR,
                       selectbackground=HIGHLIGHT, relief="flat", bd=0)
task_list.pack(pady=20)

# Load previous tasks
load_tasks()

# Run the app
root.mainloop()

