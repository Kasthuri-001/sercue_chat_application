import tkinter as tk
from datetime import datetime

# Send message function
def send_message():

    message = message_entry.get().strip()

    if message:

        current_time = datetime.now().strftime("%H:%M:%S")

        chat_box.insert(
            tk.END,
            f"[{current_time}] Server: {message}\n"
        )

        chat_box.see(tk.END)

        message_entry.delete(0, tk.END)

# Main Window
root = tk.Tk()

root.title("Secure Chat - Server")
root.geometry("700x500")
root.config(bg="#0d1117")

# Title
title = tk.Label(
    root,
    text="🖥️ Secure Chat Server",
    font=("Arial", 18, "bold"),
    fg="#00ff00",
    bg="#0d1117"
)

title.pack(pady=15)

# Chat Box
chat_box = tk.Text(
    root,
    height=20,
    width=75,
    bg="black",
    fg="#00ff00",
    insertbackground="#00ff00",
    font=("Consolas", 11)
)

chat_box.pack(pady=10)

# Input Frame
input_frame = tk.Frame(
    root,
    bg="#0d1117"
)

input_frame.pack(pady=10)

# Message Entry
message_entry = tk.Entry(
    input_frame,
    width=50,
    font=("Arial", 12),
    bg="#161b22",
    fg="white",
    insertbackground="white"
)

message_entry.pack(side="left", padx=10)

# Enter Key
message_entry.bind("<Return>", lambda event: send_message())

# Send Button
send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_message,
    bg="#00ff00",
    fg="black",
    font=("Arial", 11, "bold")
)

send_button.pack(side="left")

root.mainloop()