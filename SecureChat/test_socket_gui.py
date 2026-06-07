import tkinter as tk

root = tk.Tk()

root.title("Socket GUI Test")
root.geometry("400x300")

label = tk.Label(
    root,
    text="GUI + Networking Test",
    font=("Arial", 16, "bold")
)

label.pack(pady=20)

root.mainloop()