# ==========================================================
# gui.py
# Professional AI FAQ Chatbot GUI
# ==========================================================

import customtkinter as ctk
from tkinter import END
from datetime import datetime

from chatbot import FAQChatbot


class ChatGUI:

    def __init__(self):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.bot = FAQChatbot()

        self.window = ctk.CTk()

        self.window.title("AI FAQ Chatbot")

        self.window.geometry("1100x700")

        self.window.configure(fg_color="#0f172a")

        self.create_sidebar()

        self.create_main_area()

        self.show_welcome()
            # =====================================
    # Sidebar
    # =====================================

    def create_sidebar(self):

        self.sidebar = ctk.CTkFrame(
            self.window,
            width=220,
            corner_radius=0
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        title = ctk.CTkLabel(
            self.sidebar,
            text="🤖 AI FAQ\nChatbot",
            font=("Arial",26,"bold")
        )

        title.pack(
            pady=30
        )

        self.clear_btn = ctk.CTkButton(
            self.sidebar,
            text="Clear Chat",
            command=self.clear_chat
        )

        self.clear_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.about_btn = ctk.CTkButton(
            self.sidebar,
            text="About",
            command=self.show_about
        )

        self.about_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.exit_btn = ctk.CTkButton(
            self.sidebar,
            text="Exit",
            fg_color="red",
            command=self.window.destroy
        )

        self.exit_btn.pack(
            padx=20,
            pady=10,
            fill="x"
        )
            # =====================================
    # Main Area
    # =====================================

    def create_main_area(self):

        self.main = ctk.CTkFrame(
            self.window
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.chat_box = ctk.CTkTextbox(
            self.main,
            font=("Consolas",15)
        )

        self.chat_box.pack(
            padx=20,
            pady=20,
            fill="both",
            expand=True
        )

        self.chat_box.configure(
            state="disabled"
        )

        self.entry = ctk.CTkEntry(
            self.main,
            height=45,
            placeholder_text="Type your question..."
        )

        self.entry.pack(
            side="left",
            padx=20,
            pady=20,
            fill="x",
            expand=True
        )

        self.entry.bind(
            "<Return>",
            self.send_message
        )

        self.send_btn = ctk.CTkButton(
            self.main,
            text="Send",
            width=120,
            command=self.send_message
        )

        self.send_btn.pack(
            side="right",
            padx=20,
            pady=20
        )
            # =====================================
    # Welcome Message
    # =====================================

    def show_welcome(self):

        self.add_message(
            "Bot",
            "👋 Welcome to the AI FAQ Chatbot!\n\n"
            "Ask me any question from the FAQ dataset."
        )

    # =====================================
    # Add Message
    # =====================================

    def add_message(self, sender, message):

        current_time = datetime.now().strftime("%I:%M %p")

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            END,
            f"\n[{current_time}] {sender}\n"
        )

        self.chat_box.insert(
            END,
            f"{message}\n"
        )

        self.chat_box.insert(
            END,
            "-" * 60 + "\n"
        )

        self.chat_box.configure(state="disabled")

        self.chat_box.see(END)

    # =====================================
    # Send Message
    # =====================================

    def send_message(self, event=None):

        question = self.entry.get().strip()

        if question == "":
            return

        self.add_message("You", question)

        self.entry.delete(0, END)

        self.window.after(
            400,
            lambda: self.bot_reply(question)
        )

    # =====================================
    # Bot Reply
    # =====================================

    def bot_reply(self, question):

        answer = self.bot.get_answer(question)

        self.add_message("Bot", answer)

    # =====================================
    # Typing Animation (Optional)
    # =====================================

    def typing(self):

        self.chat_box.configure(state="normal")

        self.chat_box.insert(
            END,
            "\nBot is typing...\n"
        )

        self.chat_box.configure(state="disabled")

        self.chat_box.see(END)
            # =====================================
    # Clear Chat
    # =====================================

    def clear_chat(self):

        self.chat_box.configure(state="normal")

        self.chat_box.delete("1.0", END)

        self.chat_box.configure(state="disabled")

        self.show_welcome()

    # =====================================
    # About
    # =====================================

    def show_about(self):

        self.add_message(
            "System",
            "AI FAQ Chatbot\n\n"
            "Developed using:\n"
            "• Python\n"
            "• CustomTkinter\n"
            "• NLTK\n"
            "• TF-IDF\n"
            "• Cosine Similarity\n\n"
            "This chatbot answers questions from a predefined FAQ dataset."
        )

    # =====================================
    # Run Application
    # =====================================

    def run(self):

        self.window.mainloop()


# ==========================================
# Main Function
# ==========================================

if __name__ == "__main__":

    app = ChatGUI()

    app.run()