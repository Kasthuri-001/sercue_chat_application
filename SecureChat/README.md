# 🔐 Secure Chat Application

## Overview

Secure Chat Application is a Python-based client-server chat system that enables real-time communication between two users over a network.

The project uses Socket Programming for communication and Tkinter for the graphical user interface (GUI). It demonstrates the fundamentals of networking, multithreading, and secure communication concepts.

This project was developed as a cybersecurity and networking learning project.

---

# Features

✅ Real-Time Chat Communication

✅ Client-Server Architecture

✅ Graphical User Interface (GUI)

✅ Multi-Threaded Communication

✅ Two-Way Messaging

✅ Dark Theme Interface

✅ Timestamped Messages

✅ Send Button Support

✅ Enter Key Support

✅ Easy-to-Use Interface

---

# Technologies Used

- Python
- Tkinter
- Socket Programming
- Threading
- Datetime Module

---

# Project Structure

```text
SecureChat/
│
├── threaded_server.py
├── threaded_client.py
├── gui_server.py
├── gui_client.py
├── server.py
├── client.py
├── key.key
├── README.md
```

---

# How It Works

The application follows a Client-Server architecture.

### Server

- Creates a socket
- Waits for incoming connections
- Receives messages
- Sends replies

### Client

- Connects to the server
- Sends messages
- Receives responses

### Communication Flow

Client → Server

Server → Client

Messages are displayed in real-time through the GUI.

---

# Installation

## Step 1: Install Python

Download Python:

https://www.python.org

---

## Step 2: Clone Repository

```bash
git clone https://github.com/your-username/SecureChat.git
```

---

## Step 3: Open Project Folder

```bash
cd SecureChat
```

---

## Step 4: Run Server

```bash
python threaded_server.py
```

---

## Step 5: Run Client

Open a second terminal:

```bash
python threaded_client.py
```

---

# Usage

1. Start the server application.
2. Start the client application.
3. Wait for connection.
4. Type a message.
5. Click Send or press Enter.
6. Messages appear instantly on both sides.

---

# Screenshots

Add screenshots here.

Example:

```text
screenshots/
├── server-window.png
├── client-window.png
└── chat-demo.png
```

---

# Learning Outcomes

This project helped in understanding:

- Socket Programming
- Client-Server Communication
- GUI Development with Tkinter
- Multithreading
- Event Handling
- Real-Time Messaging Systems
- Cybersecurity Communication Concepts

---

# Advantages

- Lightweight application
- Easy to understand
- Beginner-friendly networking project
- Real-time communication
- Expandable for future encryption features

---

# Future Enhancements

- End-to-End Encryption
- User Authentication
- Multiple Client Support
- File Sharing
- Voice Messaging
- Online Status Indicator
- Matrix Background Animation
- Chat History Storage

---

# Conclusion

The Secure Chat Application successfully demonstrates real-time communication using Python sockets and a graphical user interface. It serves as a foundation for advanced secure communication systems and cybersecurity projects.

---

# Author

Parimala Nagaraj

---

# License

This project is developed for educational and learning purposes.