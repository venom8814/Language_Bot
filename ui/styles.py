import customtkinter as ctk

COLOR_BG         = "#0F1117"
COLOR_ENTRY_BG   = "#1C2333"
COLOR_USER_BG    = "#1F3A6E"
COLOR_BOT_BG     = "#1E2535"
COLOR_USER_TEXT  = "#D6E8FF"
COLOR_BOT_TEXT   = "#C8D8E8"
COLOR_USER_LABEL = "#60AFFF"
COLOR_BOT_LABEL  = "#4CAF90"

def get_fonts():
    return {
        "user": ctk.CTkFont(family="Segoe UI", size=13),
        "bot": ctk.CTkFont(family="Segoe UI", size=13)
    }