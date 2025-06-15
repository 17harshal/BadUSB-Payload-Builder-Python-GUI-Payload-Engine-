# main.py

import tkinter as tk
from tkinter import filedialog
from payload_sender import run_payload

def build_gui():
    root = tk.Tk()
    root.title("BadUSB Payload Builder")

    text = tk.Text(root, height=20, width=60)
    text.pack()

    def run_script():
        lines = text.get("1.0", tk.END).strip().split("\n")
        run_payload(lines)

    def save_script():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        with open(file_path, "w") as f:
            f.write(text.get("1.0", tk.END))

    def load_script():
        file_path = filedialog.askopenfilename()
        with open(file_path, "r") as f:
            text.delete("1.0", tk.END)
            text.insert(tk.END, f.read())

    tk.Button(root, text="▶ Run", command=run_script).pack(side=tk.LEFT, padx=5)
    tk.Button(root, text="💾 Save", command=save_script).pack(side=tk.LEFT, padx=5)
    tk.Button(root, text="📂 Load", command=load_script).pack(side=tk.LEFT, padx=5)

    root.mainloop()

if __name__ == "__main__":
    build_gui()
