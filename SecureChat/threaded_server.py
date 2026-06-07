import tkinter as tk
import socket
import threading

# Function to receive messages
def receive_messages():

    while True:

        try:

            message = client.recv(1024).decode()

            chat_box.insert(
                tk.END,
                f"Client: {message}\n"
            )

            chat_box.see(tk.END)

        except:
            break

# Start server
def start_server():

    global client

    server = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM
    )

    server.bind(("127.0.0.1", 5555))

    server.listen(1)

    chat_box.insert(
        tk.END,
        "Waiting for client...\n"
    )

    client, address = server.accept()

    chat_box.insert(
        tk.END,
        f"Connected: {address}\n"
    )

    thread = threading.Thread(
        target=receive_messages,
        daemon=True
    )

    thread.start()

# Send message
def send_message():

    message = message_entry.get()

    if message:

        client.send(
            message.encode()
        )

        chat_box.insert(
            tk.END,
            f"Server: {message}\n"
        )

        message_entry.delete(0, tk.END)

# GUI
root = tk.Tk()

root.title("Threaded Server")
root.geometry("700x500")

chat_box = tk.Text(
    root,
    height=20,
    width=75
)

chat_box.pack(pady=10)

message_entry = tk.Entry(
    root,
    width=50
)

message_entry.pack(side="left", padx=10)

send_button = tk.Button(
    root,
    text="Send",
    command=send_message
)

send_button.pack(side="left")

# Start server thread
threading.Thread(
    target=start_server,
    daemon=True
).start()

root.mainloop()