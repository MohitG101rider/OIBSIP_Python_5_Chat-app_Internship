import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

class ChatApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("💬 Chat Messenger")
        self.window.geometry("500x550")
        self.window.configure(bg="#0f172a")

        self.username = simpledialog.askstring("Login", "Enter your username:")
        if not self.username:
            messagebox.showerror("Error", "Username is required")
            self.window.destroy()
            return

        try:
            client.connect((HOST, PORT))
        except:
            messagebox.showerror("Connection Failed", f"Can't connect to {HOST}:{PORT}")
            self.window.destroy()
            return

        self.build_gui()
        self.receive_thread = threading.Thread(target=self.receive_messages)
        self.receive_thread.start()
        self.window.mainloop()

    def build_gui(self):
        self.window.rowconfigure(1, weight=1)
        self.window.columnconfigure(0, weight=4)
        self.window.columnconfigure(1, weight=1)

        header = tk.Label(self.window, text=f"👤 {self.username} | Chat Room", bg="#1e293b", fg="white",
                          font=("Segoe UI", 14, "bold"))
        header.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=(10, 5))

        #chat
        self.chat_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, font=("Segoe UI", 11),
                                                   bg="#f8fafc", fg="#0f172a")
        self.chat_area.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=10, pady=5)
        self.chat_area.config(state='disabled')

        #message
        self.message_entry = tk.Entry(self.window, font=("Segoe UI", 11))
        self.message_entry.grid(row=2, column=0, padx=(10, 5), pady=10, sticky="ew")
        self.message_entry.bind("<Return>", lambda event: self.send_message())

        #send button
        self.send_button = tk.Button(self.window, text="Send", command=self.send_message,
                                     bg="#4f46e5", fg="white", font=("Segoe UI", 10, "bold"))
        self.send_button.grid(row=2, column=1, padx=(5, 10), pady=10, sticky="ew")

    def receive_messages(self):
        while True:
            try:
                message = client.recv(1024).decode("utf-8")
                if message == "USERNAME":
                    client.send(self.username.encode("utf-8"))
                else:
                    self.display_message(message)
            except:
                break

    def send_message(self):
        message = self.message_entry.get().strip()
        if message:
            client.send(message.encode("utf-8"))
            self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.chat_area.config(state="normal")
        self.chat_area.insert(tk.END, message + "\n")
        self.chat_area.yview(tk.END)
        self.chat_area.config(state="disabled")

ChatApp()
