import customtkinter as ctk

class LogixDesktop(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Logix.ai Desktop App")
        self.geometry("800x500")
        ctk.set_appearance_mode("dark")

        # Sidebar
        self.sidebar = ctk.CTkFrame(self, width=160, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")
        self.label = ctk.CTkLabel(self.sidebar, text="LOGIX.AI", font=("Arial", 20, "bold"))
        self.label.pack(pady=20)

        # Chat display
        self.textbox = ctk.CTkTextbox(self, width=600, height=350)
        self.textbox.pack(pady=20, padx=20)
        self.textbox.insert("0.0", "Logix.ai: System Ready.\n\n")
        self.textbox.configure(state="disabled")

        # Input
        self.input_field = ctk.CTkEntry(self, placeholder_text="Enter command...", width=500)
        self.input_field.pack(side="left", padx=(120, 10), pady=10)
        self.input_field.bind("<Return>", lambda e: self.send_msg())

        self.btn = ctk.CTkButton(self, text="Send", command=self.send_msg)
        self.btn.pack(side="left")

    def send_msg(self):
        text = self.input_field.get()
        if text:
            self.textbox.configure(state="normal")
            self.textbox.insert("end", f"You: {text}\nLogix: Analyzing command...\n\n")
            self.textbox.configure(state="disabled")
            self.input_field.delete(0, 'end')

if __name__ == "__main__":
    app = LogixDesktop()
    app.mainloop()
