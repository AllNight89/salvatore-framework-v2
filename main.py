import tkinter as tk
from tkinter import ttk
import json
import os
import salvatore  # Your framework

class AIApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Salvatore Juggernaut Apex")
        self.geometry("600x400")
        self.chat_history = []
        self.history_file = "data/chats.json"
        os.makedirs("data", exist_ok=True)
        self.load_history()

        # Chat area (shows conversation)
        self.chat_display = tk.Text(self, state="disabled")
        self.chat_display.pack(padx=10, pady=10, fill="both", expand=True)

        # Input box (where you type)
        self.input_field = ttk.Entry(self)
        self.input_field.pack(padx=10, pady=5, fill="x")
        self.send_button = ttk.Button(self, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=5)
        self.input_field.bind("<Return>", lambda event: self.send_message())

    def load_history(self):
        if os.path.exists(self.history_file):
            with open(self.history_file, "r") as f:
                self.chat_history = json.load(f)
            self.chat_display.config(state="normal")
            for entry in self.chat_history:
                self.chat_display.insert(tk.END, f"You: {entry['user']}\nAI: {entry['ai']}\n")
            self.chat_display.config(state="disabled")

    def save_history(self, user_input, ai_response):
        self.chat_history.append({"user": user_input, "ai": ai_response})
        with open(self.history_file, "w") as f:
            json.dump(self.chat_history, f, indent=2)

    def send_message(self):
        user_input = self.input_field.get()
        if user_input:
            self.chat_display.config(state="normal")
            self.chat_display.insert(tk.END, f"You: {user_input}\n")
            self.send_button.config(text="Loading...", state="disabled")
            self.update()
            ai_response = self.call_framework(user_input)
            self.chat_display.insert(tk.END, f"AI: {ai_response}\n")
            self.chat_display.config(state="disabled")
            self.input_field.delete(0, tk.END)
            self.send_button.config(text="Send", state="normal")
            self.save_history(user_input, ai_response)

    def call_framework(self, input_text):
        try:
            # Call your framework's analyze_query
            return str(salvatore.analyze_query(input_text))
        except Exception as e:
            return f"Error: {e}"

if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
