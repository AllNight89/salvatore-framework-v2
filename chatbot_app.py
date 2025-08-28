import tkinter as tk
from tkinter import scrolledtext, ttk
import asyncio
from salvatore import SAL

class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salvatore Juggernaut Apex")
        self.root.geometry("600x600")

        # Chat display
        self.chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20)
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input field and send button
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(fill=tk.X, padx=10, pady=10)
        self.input_entry = tk.Entry(self.input_frame)
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input_entry.bind("<Return>", self.send_message)
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT)

    def add_message(self, role, content):
        self.chat_display.config(state='normal')
        tag = "user" if role == "user" else "assistant"
        self.chat_display.insert(tk.END, f"{role.capitalize()}: {content}\n\n", tag)
        self.chat_display.tag_config("user", foreground="blue", justify="right")
        self.chat_display.tag_config("assistant", foreground="green", justify="left")
        self.chat_display.config(state='disabled')
        self.chat_display.see(tk.END)

    def send_message(self, event=None):
        query = self.input_entry.get().strip()
        if not query:
            return
        self.add_message("user", query)
        self.input_entry.delete(0, tk.END)
        asyncio.run_coroutine_threadsafe(self.get_ai_response(query), asyncio.get_event_loop())

    async def get_ai_response(self, query):
        try:
            sal = SAL("JuggernautApex")
            result = await sal.run(query)
            # Simplify output for display
            summary = f"Summary: {result.get('NARRATIVE', {}).get('story', 'No narrative')}\nLie Flag: {result.get('EVIDENCE', {}).get('what', 'No evidence').split(', ')[1] if 'EVIDENCE' in result else 'N/A'}\nFull JSON saved to ~/salvatore_export_juggernautapex.json"
            self.add_message("assistant", summary)
        except Exception as e:
            self.add_message("assistant", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    loop = asyncio.get_event_loop()
    root.mainloop()
