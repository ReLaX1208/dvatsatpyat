import tkinter as tk
import requests
import json

class JsonPlaceholderApp:
    def __init__(self, master):
        self.master = master
        self.master.title("JSON Placeholder API")

        tk.Label(self.master, text="Enter ID:").pack()
        self.id_entry = tk.Entry(self.master)
        self.id_entry.pack()

        tk.Button(self.master, text="Get Data", command=self.get_data).pack()

        self.result_text = tk.Text(self.master, height=10)
        self.result_text.pack()

    def get_data(self):
        id_value = self.id_entry.get()
        response = requests.get(f"https://jsonplaceholder.typicode.com/todos/{id_value}")
        data = response.json()

        file_path = f"data_{id_value}.json"
        with open(file_path, "w") as file:
            json.dump(data, file, indent=2)

        self.result_text.insert(tk.END, f"Data saved to {file_path}\n")

root = tk.Tk()
my_app = JsonPlaceholderApp(root)
root.mainloop()