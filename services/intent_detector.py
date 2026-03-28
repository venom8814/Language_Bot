import re
from enum import Enum, auto


class Intent(Enum):
    TRANSLATE = auto()
    CORRECT   = auto()
    EXERCISE  = auto()
    EXPLAIN   = auto()
    HELP      = auto()
    UNKNOWN   = auto()


class IntentDetector:


    PATTERNS: list[tuple[Intent, list[str]]] = [
        (Intent.HELP, [
            r"помощ", r"help", r"что умеешь", r"команд",
        ]),
        (Intent.EXERCISE, [
            r"упражнени", r"задани", r"тест", r"практик",
            r"потренир", r"викторин", r"quiz",
        ]),
        (Intent.CORRECT, [
            r"проверь", r"исправь", r"correct", r"check",
            r"ошибк", r"grammar check", r"грамматик",
        ]),
        (Intent.TRANSLATE, [
            r"перевед", r"переводи", r"translate",
            r"как будет", r"как сказать", r"что значит",
            r"what does", r"what is",
        ]),
        (Intent.EXPLAIN, [
            r"объясни", r"расскаж", r"explain",
            r"что такое", r"правило", r"rule",
        ]),
    ]

    EXTRACT_PATTERNS = {
        Intent.TRANSLATE: [
            r"""перевед[ии]?\s*[:\-«"'"]?\s*(.+)""",
            r"""переводи\s*[:\-«"'"]?\s*(.+)""",
            r"""translate\s*[:\-]?\s*(.+)""",
            r"""как будет\s+[а-яёa-z ]+[:\-]?\s*(.+)""",
            r"""что значит\s*[:\-«"'"]?\s*(.+)""",
        ],
        Intent.EXPLAIN: [
            r"""объясни\s*[:\-«"'"]?\s*(.+)""",
            r"""расскажи\s+про\s*(.+)""",
            r"""explain\s*[:\-]?\s*(.+)""",
            r"""что такое\s*(.+)""",
        ],
    }

    def detect(self, text: str) -> tuple[Intent, str | None]:
        lower = text.lower().strip()

        detected_intent = Intent.UNKNOWN
        for intent, patterns in self.PATTERNS:
            if any(re.search(p, lower) for p in patterns):
                detected_intent = intent
                break

        payload = self._extract_payload(detected_intent, text)

        return detected_intent, payload

    def _extract_payload(self, intent: Intent, text: str) -> str | None:
        patterns = self.EXTRACT_PATTERNS.get(intent, [])
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                raw = match.group(1).strip()
                return raw.strip("«»\"\' ")
        return None
