import tkinter as tk
from tkinter import filedialog
import subprocess
import os

print('Welcome to Latte 1.0.0')

def choose_directory():
    selected_directory = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, selected_directory)

def create_project():
    project_path = path_entry.get()
    project_name = name_entry.get()
    project_author = author_entry.get()

    if not project_path or not project_name or not project_author:
        result_label.config(text="Please fill in all fields.")
    else:

        project_directory = os.path.join(project_path, 'com', project_author, project_name, 'latte', 'project', 'main')
        project_directory_2 = os.path.join(project_path, 'com', project_author, project_name, 'latte', 'libs')
        main_file_path = os.path.join(project_directory, "main.py")
        main_file_path_2 = os.path.join(project_directory_2, "builtins.py")
        project_xml = os.path.join(project_path, "project.xml")
        result_label.config(text=f"Project Path: {main_file_path}")

        try:
            if not os.path.exists(project_directory):
                os.makedirs(project_directory)
            if not os.path.exists(project_directory_2):
                os.makedirs(project_directory_2)

            with open(main_file_path, 'w') as main_file:
                main_file.write(f"""from com.{project_author}.{project_name}.latte.libs.builtins import *

console.out('Welcome to Latte.')""")

            with open(main_file_path_2, 'w') as main_file:
                main_file.write(f"""class Console:
    def out(self, *args):
        return print(*args)
    def put(self, *args):
        return input(*args)

console = Console()

On = True
Off = False""")

            with open(project_xml, 'w') as main_file:
                main_file.write(f"""<?xml version="1.0" encoding="UTF-8"?>
<project>
    <name>{project_name}</name>
    <version>1.0.0</version>
    <description>Nothing is here.</description>
    <main>com.{project_author}.{project_name}.latte.project.main</main>
    <authors>
        <author>{project_author}</author>
    </authors>
</project>""")

            project_path_edited = project_path.replace("/", "\\")

            subprocess.Popen(fr'explorer /open,"{project_path_edited}"')

            root.quit()

        except Exception as e:
            result_label.config(text=f"Error: {str(e)}")

root = tk.Tk()
root.title("New Latte Project")

title_label = tk.Label(root, text="New Latte Project", font=("Consolas", 24))
title_label.grid(row=0, column=0, columnspan=2, pady=20)

input_frame = tk.Frame(root)
input_frame.grid(row=1, column=0, columnspan=2, padx=10)

path_label = tk.Label(input_frame, text="Project Path", font=("Consolas", 14))
path_label.grid(row=0, column=0, padx=5, pady=5)
path_entry = tk.Entry(input_frame, font=("Consolas", 12), width=40)
path_entry.grid(row=0, column=1, padx=5, pady=5)
choose_button = tk.Button(input_frame, text="Choose Directory", font=("Consolas", 12), command=choose_directory)
choose_button.grid(row=0, column=2, padx=5, pady=5)

name_label = tk.Label(input_frame, text="Project Name", font=("Consolas", 14))
name_label.grid(row=1, column=0, padx=5, pady=5)
name_entry = tk.Entry(input_frame, font=("Consolas", 12), width=40)
name_entry.grid(row=1, column=1, padx=5, pady=5)

author_label = tk.Label(input_frame, text="Project Author", font=("Consolas", 14))
author_label.grid(row=2, column=0, padx=5, pady=5)
author_entry = tk.Entry(input_frame, font=("Consolas", 12), width=40)
author_entry.grid(row=2, column=1, padx=5, pady=5)

create_button = tk.Button(root, text="Create New Project", font=("Consolas", 12), command=create_project)
create_button.grid(row=2, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="", font=("Consolas", 12))
result_label.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
