import json
import os
from datetime import datetime


HISTORY_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "chat_history.json"
)

MAX_HISTORY_SIZE = 200


class HistoryManager:


    def __init__(self, filepath: str = HISTORY_FILE):
        self.filepath = filepath
        self._history: list[dict] = []

    def add(self, user_msg: str, bot_msg: str) -> None:
        entry = {
            "user":      user_msg,
            "bot":       bot_msg,
            "timestamp": datetime.now().isoformat(),
        }
        self._history.append(entry)

        if len(self._history) > MAX_HISTORY_SIZE:
            self._history = self._history[-MAX_HISTORY_SIZE:]

        self._save()

    def load(self) -> list[dict]:
        if not os.path.exists(self.filepath):
            return []

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            self._history = data if isinstance(data, list) else []
        except (json.JSONDecodeError, IOError):
            self._history = []

        return self._history

    def clear(self) -> None:
        self._history = []
        self._save()

    def _save(self) -> None:
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(self._history, f, ensure_ascii=False, indent=2)
        except IOError as e:
            print(f"[HistoryManager] Ошибка сохранения: {e}")
