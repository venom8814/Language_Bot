import customtkinter as ctk
from ui.styles import (
    get_fonts,
    COLOR_USER_BG, COLOR_BOT_BG,
    COLOR_USER_TEXT, COLOR_BOT_TEXT,
    COLOR_USER_LABEL, COLOR_BOT_LABEL,
)


class ChatBubble(ctk.CTkFrame):

    def __init__(self, parent, text: str, role: str, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self._build(text, role)

    def _build(self, text: str, role: str):
        is_user = (role == "user")

        fonts = get_fonts()

        bg_color  = COLOR_USER_BG   if is_user else COLOR_BOT_BG
        txt_color = COLOR_USER_TEXT if is_user else COLOR_BOT_TEXT
        lbl_color = COLOR_USER_LABEL if is_user else COLOR_BOT_LABEL
        label_txt = "Вы" if is_user else "🤖 LangBot"
        font      = fonts["user"] if is_user else fonts["bot"]
        anchor    = "e" if is_user else "w"
        side      = "right" if is_user else "left"

        bubble_frame = ctk.CTkFrame(
            self,
            fg_color=bg_color,
            corner_radius=14,
        )
        bubble_frame.pack(anchor=anchor, pady=2, padx=4)

        name_label = ctk.CTkLabel(
            bubble_frame,
            text=label_txt,
            font=ctk.CTkFont(family="Segoe UI", size=10, weight="bold"),
            text_color=lbl_color,
            anchor=anchor,
        )
        name_label.pack(anchor=anchor, padx=10, pady=(6, 0))

        msg_label = ctk.CTkLabel(
            bubble_frame,
            text=text,
            font=font,
            text_color=txt_color,
            wraplength=520,
            justify="left",
            anchor="w",
        )
        msg_label.pack(anchor="w", padx=12, pady=(2, 8))