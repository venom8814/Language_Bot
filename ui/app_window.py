import customtkinter as ctk
from ui.chat_bubble import ChatBubble
from ui.styles import (
    COLOR_BG, COLOR_ENTRY_BG
)


class AppWindow:


    def __init__(self, chatbot, history_manager):
        self.chatbot = chatbot
        self.history_manager = history_manager

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = ctk.CTk()
        self.root.title("🌍 LangBot — Изучение языков")
        self.root.geometry("800x620")
        self.root.minsize(600, 480)
        self.root.configure(fg_color=COLOR_BG)

        self._build_ui()
        self._load_history()

    def _build_ui(self):

        header = ctk.CTkLabel(
            self.root,
            text="🌍 LangBot — Твой помощник в изучении языков",
            font=ctk.CTkFont(family="Segoe UI", size=16, weight="bold"),
            text_color="#60AFFF",
        )
        header.pack(pady=(14, 4), padx=20, anchor="w")

        subtitle = ctk.CTkLabel(
            self.root,
            text="Переводи, исправляй ошибки, тренируйся — всё офлайн!",
            font=ctk.CTkFont(family="Segoe UI", size=12),
            text_color="#8899AA",
        )
        subtitle.pack(padx=20, anchor="w")

        self.scroll_frame = ctk.CTkScrollableFrame(
            self.root,
            fg_color="#1A1F2E",
            corner_radius=12,
        )
        self.scroll_frame.pack(fill="both", expand=True, padx=16, pady=(10, 6))

        input_frame = ctk.CTkFrame(self.root, fg_color=COLOR_BG, height=60)
        input_frame.pack(fill="x", padx=16, pady=(0, 14))
        input_frame.pack_propagate(False)

        self.entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Введи сообщение (например: переведи «кошка»)...",
            font=ctk.CTkFont(family="Segoe UI", size=13),
            fg_color=COLOR_ENTRY_BG,
            border_color="#2D3A50",
            border_width=2,
            height=44,
            corner_radius=10,
        )
        self.entry.pack(side="left", fill="both", expand=True, padx=(0, 10))
        self.entry.bind("<Return>", self._on_send)

        self.send_btn = ctk.CTkButton(
            input_frame,
            text="➤ Отправить",
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="bold"),
            width=130,
            height=44,
            corner_radius=10,
            fg_color="#1F6FEB",
            hover_color="#1558C0",
            command=self._on_send,
        )
        self.send_btn.pack(side="right")

        hint = ctk.CTkLabel(
            self.root,
            text='💡 Попробуй: "переведи cat"· "упражнение" · "помощь"',
            font=ctk.CTkFont(family="Segoe UI", size=11),
            text_color="#556070",
        )
        hint.pack(pady=(0, 8))

    def _on_send(self, event=None):
        text = self.entry.get().strip()
        if not text:
            return

        self._add_bubble(text, role="user")
        self.entry.delete(0, "end")

        response = self.chatbot.respond(text)
        self._add_bubble(response, role="bot")

        self.history_manager.add(user_msg=text, bot_msg=response)

    def _add_bubble(self, text: str, role: str):

        bubble = ChatBubble(self.scroll_frame, text=text, role=role)
        bubble.pack(fill="x", pady=3, padx=6)
        self.root.after(50, self._scroll_to_bottom)

    def _scroll_to_bottom(self):
        if hasattr(self.scroll_frame, '_parent_canvas'):
            self.scroll_frame._parent_canvas.yview_moveto(1.0)
        elif hasattr(self.scroll_frame, 'canvas'):
            self.scroll_frame.canvas.yview_moveto(1.0)

    def _load_history(self):
        history = self.history_manager.load()
        if not history:
            welcome = (
                "Привет! 👋 Я LangBot — твой помощник в изучении языков.\n\n"
                "Что я умею:\n"
                "🔤 Переводить слова и фразы (RU ↔ EN)\n"
                "✅ Проверять грамматику и орфографию\n"
                "📝 Генерировать упражнения\n"
                "📖 Объяснять правила грамматики\n\n"
                "Напиши \'помощь\' чтобы увидеть все команды."
            )
            self._add_bubble(welcome, role="bot")
        else:
            for entry in history:
                self._add_bubble(entry["user"], role="user")
                self._add_bubble(entry["bot"], role="bot")

    def run(self):
        self.root.mainloop()