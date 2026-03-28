import random
from services.translator import DICTIONARY_RU_EN


class ExerciseGenerator:


    def __init__(self, translator):
        self.translator = translator

    def generate(self) -> dict:

        generators = [
            self._translate_ru_to_en,
            self._translate_en_to_ru,
            self._fix_sentence,
            self._fill_in_blank,
        ]
        return random.choice(generators)()

    def _translate_ru_to_en(self) -> dict:
        word_ru, word_en = random.choice(list(DICTIONARY_RU_EN.items()))
        return {
            "type": "Перевод RU → EN",
            "question": f"Переведи на английский:\n\n  🇷🇺 «{word_ru}»",
            "answer": word_en,
            "explanation": f"💡 «{word_ru}» переводится как «{word_en}».",
        }

    def _translate_en_to_ru(self) -> dict:
        word_ru, word_en = random.choice(list(DICTIONARY_RU_EN.items()))
        return {
            "type": "Перевод EN → RU",
            "question": f"Переведи на русский:\n\n  🇬🇧 «{word_en}»",
            "answer": word_ru,
            "explanation": f"💡 «{word_en}» переводится как «{word_ru}».",
        }

    def _fix_sentence(self) -> dict:
        exercises = [
            {
                "type": "Исправление ошибок",
                "question": "Исправь ошибку в предложении:\n\n  ❌ «Я пишет письмо»",
                "answer": "я пишу письмо",
                "explanation": "💡 С местоимением «Я» глагол «писать» принимает форму «пишу».",
            },
            {
                "type": "Исправление ошибок",
                "question": "Исправь ошибку в предложении:\n\n  ❌ «He don't like coffee»",
                "answer": "he doesn't like coffee",
                "explanation": "💡 С he/she/it используется «doesn't», а не «don't».",
            },
            {
                "type": "Исправление ошибок",
                "question": "Исправь ошибку в предложении:\n\n  ❌ «Красивый девушка»",
                "answer": "красивая девушка",
                "explanation": "💡 Прилагательное согласуется с существительным: «девушка» — женский род → «красивая».",
            },
            {
                "type": "Исправление ошибок",
                "question": "Исправь ошибку в предложении:\n\n  ❌ «They is students»",
                "answer": "they are students",
                "explanation": "💡 С местоимением «they» глагол «to be» принимает форму «are».",
            },
            {
                "type": "Исправление ошибок",
                "question": "Исправь ошибку в предложении:\n\n  ❌ «Я вчера иду в школу»",
                "answer": "я вчера шёл в школу",
                "explanation": "💡 «Вчера» указывает на прошедшее время: «шёл» вместо «иду».",
            },
            {
                "type": "Исправление ошибок",
                "question": "Исправь ошибку в предложении:\n\n  ❌ «I can to swim»",
                "answer": "i can swim",
                "explanation": "💡 После модального глагола «can» инфинитив используется без «to».",
            },
        ]
        return random.choice(exercises)

    def _fill_in_blank(self) -> dict:
        exercises = [
            {
                "type": "Заполни пропуск",
                "question": "Вставь пропущенное слово:\n\n  🇬🇧 «She ___ a student» (быть)",
                "answer": "is",
                "explanation": "💡 С «she» глагол «to be» в Present Simple = «is».",
            },
            {
                "type": "Заполни пропуск",
                "question": "Вставь пропущенное слово:\n\n  🇷🇺 «Я ___ книгу» (читать, наст. время)",
                "answer": "читаю",
                "explanation": "💡 Глагол «читать» с «я» в настоящем времени = «читаю».",
            },
            {
                "type": "Заполни пропуск",
                "question": "Вставь пропущенное слово:\n\n  🇬🇧 «There ___ two cats» (быть)",
                "answer": "are",
                "explanation": "💡 С множественным числом используется «are».",
            },
            {
                "type": "Заполни пропуск",
                "question": "Вставь пропущенное слово:\n\n  🇷🇺 «Он ___ в школу вчера» (идти)",
                "answer": "шёл",
                "explanation": "💡 Прошедшее время от «идти» для мужского рода = «шёл».",
            },
        ]
        return random.choice(exercises)