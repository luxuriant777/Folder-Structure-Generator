import os
import tkinter as tk
from tkinter import messagebox, filedialog
import json

example_structure = """{
  "name": "project_name",
  "files": [
    "manage.py"
  ],
  "subdirectories": [
    {
      "name": "project_name",
      "files": [
        "__init__.py",
        "settings.py",
        "urls.py",
        "wsgi.py"
      ],
      "subdirectories": [
        {
          "name": "apps",
          "files": [],
          "subdirectories": [
            {
              "name": "app1",
              "files": [
                "__init__.py",
                "models.py",
                "views.py"
              ],
              "subdirectories": []
            },
            {
              "name": "app2",
              "files": [
                "__init__.py",
                "models.py",
                "views.py"
              ],
              "subdirectories": []
            }
          ]
        },
        {
          "name": "templates",
          "files": [],
          "subdirectories": []
        },
        {
          "name": "static",
          "files": [],
          "subdirectories": [
            {
              "name": "css",
              "files": [],
              "subdirectories": []
            },
            {
              "name": "js",
              "files": [],
              "subdirectories": []
            }
          ]
        }
      ]
    }
  ]
}"""

def create_structure():
    structure_json = txt.get('1.0', 'end')
    root_dir = filedialog.askdirectory(title="Select Root Directory")
    if not root_dir:
        return
    structure = json.loads(structure_json)
    create_directory_structure(structure, root_dir)
    messagebox.showinfo("Success", "Directory structure created successfully!")

def create_directory_structure(directory, parent_path):
    directory_name = directory["name"]
    path = os.path.join(parent_path, directory_name)
    os.makedirs(path, exist_ok=True)

    for file in directory.get("files", []):
        file_path = os.path.join(path, file)
        open(file_path, 'a').close()

    for subdir in directory.get("subdirectories", []):
        create_directory_structure(subdir, path)

window = tk.Tk()
window.title("Directory Structure Creator")
window.geometry('800x600')

lbl = tk.Label(window, text="Enter Directory Structure (JSON). " + 
    "Please ensure that you adhere to the format provided in the example:")
lbl.grid(column=0, row=0, padx=15, pady=5, sticky="W")

txt = tk.Text(window, width=40, height=10)
txt.grid(column=0, row=1, padx=15, pady=5, sticky="nsew")
txt.insert(tk.END, example_structure)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)

btn_submit = tk.Button(window, text="Create Structure", command=create_structure)
btn_submit.grid(column=0, row=2, padx=15, pady=15, sticky="W")

window.mainloop()
