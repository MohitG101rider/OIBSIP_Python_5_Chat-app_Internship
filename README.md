# OIBSIP_Python_5_Chat-app_Internship
As internship project

# Chat Application – Oasis Infobyte Internship

## 🎯 Objective
The objective of this project was to build a **real-time chat application** using Python that allows multiple users to communicate over a network. The focus was on understanding **socket programming** and how client-server communication works in Python.

---

## 🛠 Tools & Technologies Used
- **Python 3.9**
- `socket` – For network communication between client and server
- `threading` – To handle multiple clients simultaneously
- `tkinter` (optional) – For basic graphical interface
- Basic networking concepts (IP address, ports)

---

## 📝 Steps Performed
1. **Implemented server** using `socket` to listen for incoming connections and manage message broadcasting.  
2. **Developed client** program to connect to the server and send/receive messages.  
3. **Used threading** to allow multiple clients to chat simultaneously without blocking each other.  
4. **Basic Tkinter GUI** to provide a simple text interface for messages.  
5. **Tested the application** locally using multiple terminals to simulate multiple users.

---

## 📊 Outcome
- Built a **functional real-time chat application** using Python sockets.  
- Gained practical understanding of **client-server architecture**.  
- Learned to use **multithreading** for handling multiple connections efficiently.  
- Can be extended for encrypted chat or web-based chat systems.

---

## ▶️ How to Run
1. Start the server:
   ```bash
   python server.py
2. Start clients in seperate terminals:
   ```bash
   python client.py
