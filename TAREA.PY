import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        
        # Crear los widgets de la interfaz
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.grid(row=1, column=1, padx=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, rowspan=2, padx=10, pady=10)

        # Eventos adicionales
        self.task_entry.bind("<Return>", lambda event: self.add_task())  # Añadir tarea con Enter
        self.task_listbox.bind("<Double-1>", lambda event: self.complete_task())  # Completar tarea con doble clic

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede añadir una tarea vacía")

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"[Completada] {task}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminarla")

# Inicializar la aplicación
root = tk.Tk()
app = TaskManager(root)
root.mainloop()
