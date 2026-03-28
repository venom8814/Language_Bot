import re


DICTIONARY_RU_EN: dict[str, str] = {
    "кошка": "cat", "кот": "cat", "собака": "dog", "пёс": "dog",
    "птица": "bird", "рыба": "fish", "конь": "horse", "лошадь": "horse",
    "корова": "cow", "свинья": "pig", "курица": "chicken", "медведь": "bear",
    "волк": "wolf", "лиса": "fox", "заяц": "rabbit", "мышь": "mouse",
    "слон": "elephant", "тигр": "tiger", "лев": "lion", "обезьяна": "monkey",

    "дерево": "tree", "цветок": "flower", "трава": "grass", "вода": "water",
    "огонь": "fire", "земля": "earth", "небо": "sky", "солнце": "sun",
    "луна": "moon", "звезда": "star", "море": "sea", "река": "river",
    "гора": "mountain", "лес": "forest", "снег": "snow", "дождь": "rain",

    "человек": "person", "мужчина": "man", "женщина": "woman",
    "мальчик": "boy", "девочка": "girl", "ребёнок": "child", "дети": "children",
    "мама": "mom", "папа": "dad", "брат": "brother", "сестра": "sister",
    "бабушка": "grandmother", "дедушка": "grandfather", "друг": "friend",

    "дом": "house", "комната": "room", "стол": "table", "стул": "chair",
    "кровать": "bed", "окно": "window", "дверь": "door", "книга": "book",
    "ручка": "pen", "карандаш": "pencil", "телефон": "phone",
    "компьютер": "computer", "машина": "car",

    "хлеб": "bread", "молоко": "milk", "яйцо": "egg", "яблоко": "apple",
    "банан": "banana", "апельсин": "orange", "чай": "tea", "кофе": "coffee",
    "сок": "juice", "суп": "soup", "мясо": "meat", "рыба": "fish",
    "сыр": "cheese", "масло": "butter", "соль": "salt", "сахар": "sugar",

    "красный": "red", "синий": "blue", "зелёный": "green", "жёлтый": "yellow",
    "белый": "white", "чёрный": "black", "серый": "gray", "розовый": "pink",
    "оранжевый": "orange", "фиолетовый": "purple", "коричневый": "brown",

    "один": "one", "два": "two", "три": "three", "четыре": "four",
    "пять": "five", "шесть": "six", "семь": "seven", "восемь": "eight",
    "девять": "nine", "десять": "ten", "сто": "hundred", "тысяча": "thousand",

    "понедельник": "monday", "вторник": "tuesday", "среда": "wednesday",
    "четверг": "thursday", "пятница": "friday", "суббота": "saturday",
    "воскресенье": "sunday",

    "время": "time", "час": "hour", "минута": "minute", "секунда": "second",
    "день": "day", "неделя": "week", "месяц": "month", "год": "year",
    "сегодня": "today", "завтра": "tomorrow", "вчера": "yesterday",

    "говорить": "to speak", "читать": "to read", "писать": "to write",
    "видеть": "to see", "слышать": "to hear", "знать": "to know",
    "любить": "to love", "хотеть": "to want", "идти": "to go",
    "бежать": "to run", "есть": "to eat", "пить": "to drink",
    "спать": "to sleep", "работать": "to work", "учиться": "to study",
    "помогать": "to help", "думать": "to think", "жить": "to live",

    "большой": "big", "маленький": "small", "хороший": "good",
    "плохой": "bad", "новый": "new", "старый": "old", "быстрый": "fast",
    "медленный": "slow", "красивый": "beautiful", "умный": "smart",
    "длинный": "long", "короткий": "short", "высокий": "tall",
    "лёгкий": "easy", "трудный": "hard", "горячий": "hot", "холодный": "cold",

    "привет": "hello", "здравствуй": "hello", "пока": "goodbye",
    "до свидания": "goodbye", "спасибо": "thank you", "пожалуйста": "please",
    "да": "yes", "нет": "no", "может быть": "maybe",
    "извини": "sorry", "прости": "sorry",
}

DICTIONARY_EN_RU: dict[str, str] = {v: k for k, v in DICTIONARY_RU_EN.items()}


class Translator:

    def translate(self, text: str) -> dict:

        clean = text.strip().strip("«»\"\' ")
        lang = self._detect_language(clean)

        if lang == "ru":
            translated = self._translate_ru_en(clean)
            direction = "RU → EN"
        else:
            translated = self._translate_en_ru(clean)
            direction = "EN → RU"

        return {
            "original":   clean,
            "translated": translated,
            "direction":  direction,
            "source_lang": lang,
        }

    def _detect_language(self, text: str) -> str:
        ru_chars = sum(1 for c in text if "а" <= c.lower() <= "я" or c.lower() == "ё")
        return "ru" if ru_chars > 0 else "en"

    def _translate_ru_en(self, text: str) -> str:
        lower = text.lower().strip()

        if lower in DICTIONARY_RU_EN:
            return DICTIONARY_RU_EN[lower]

        words = lower.split()
        translated_words = []
        i = 0
        while i < len(words):
            if i + 1 < len(words):
                pair = f"{words[i]} {words[i+1]}"
                if pair in DICTIONARY_RU_EN:
                    translated_words.append(DICTIONARY_RU_EN[pair])
                    i += 2
                    continue
            word = words[i]
            translated_words.append(DICTIONARY_RU_EN.get(word, f"[{word}]"))
            i += 1

        result = " ".join(translated_words)
        return result if result != text.lower() else f"[Слово не найдено в словаре]"

    def _translate_en_ru(self, text: str) -> str:
        lower = text.lower().strip()

        if lower in DICTIONARY_EN_RU:
            return DICTIONARY_EN_RU[lower]

        words = lower.split()
        translated_words = []
        i = 0
        while i < len(words):
            if i + 1 < len(words):
                pair = f"{words[i]} {words[i+1]}"
                if pair in DICTIONARY_EN_RU:
                    translated_words.append(DICTIONARY_EN_RU[pair])
                    i += 2
                    continue
            word = words[i]
            translated_words.append(DICTIONARY_EN_RU.get(word, f"[{word}]"))
            i += 1

        result = " ".join(translated_words)
        return result if result != text.lower() else f"[Word not found in dictionary]"
