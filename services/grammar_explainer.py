GRAMMAR_TOPICS: dict[str, str] = {
    "present simple": (
        "📖 Present Simple (Настоящее простое время)\n\n"
        "Используется для:\n"
        "  • Регулярных действий: «I work every day»\n"
        "  • Общих истин: «The sun rises in the east»\n"
        "  • Расписаний: «The train leaves at 9»\n\n"
        "Формула:\n"
        "  I/You/We/They + V (глагол)\n"
        "  He/She/It      + V + s/es\n\n"
        "Примеры:\n"
        "  ✅ I eat breakfast at 8.\n"
        "  ✅ She eats breakfast at 8.\n"
        "  ❌ She eat breakfast at 8."
    ),

    "present continuous": (
        "📖 Present Continuous (Настоящее длительное)\n\n"
        "Используется для:\n"
        "  • Действий, происходящих прямо сейчас\n"
        "  • Временных ситуаций\n\n"
        "Формула: am/is/are + V-ing\n\n"
        "Примеры:\n"
        "  ✅ I am reading now.\n"
        "  ✅ She is working today.\n"
        "  ❌ She is work today."
    ),

    "past simple": (
        "📖 Past Simple (Прошедшее простое время)\n\n"
        "Используется для:\n"
        "  • Завершённых действий в прошлом\n"
        "  • Последовательности событий в прошлом\n\n"
        "Формула:\n"
        "  Regular verbs: V + ed (worked, played)\n"
        "  Irregular verbs: 2-я форма (went, ate, saw)\n\n"
        "Примеры:\n"
        "  ✅ I worked yesterday.\n"
        "  ✅ She went to school.\n"
        "  ❌ She goed to school."
    ),

    "past continuous": (
        "📖 Past Continuous (Прошедшее длительное)\n\n"
        "Используется для:\n"
        "  • Действий, длившихся в определённый момент прошлого\n"
        "  • Параллельных действий в прошлом\n\n"
        "Формула: was/were + V-ing\n\n"
        "Примеры:\n"
        "  ✅ I was reading at 8 PM yesterday.\n"
        "  ✅ They were talking when I came.\n"
        "  ❌ I was read at 8 PM."
    ),

    "future simple": (
        "📖 Future Simple (Будущее простое время)\n\n"
        "Используется для:\n"
        "  • Спонтанных решений\n"
        "  • Предсказаний\n"
        "  • Обещаний\n\n"
        "Формула: will + V (инфинитив без to)\n\n"
        "Примеры:\n"
        "  ✅ I will call you tomorrow.\n"
        "  ✅ She will arrive at 6 PM.\n"
        "  ❌ She will to arrive."
    ),

    "артикль": (
        "📖 Артикли в английском языке\n\n"
        "A / AN (неопределённый артикль):\n"
        "  • A + согласный звук: a cat, a book\n"
        "  • AN + гласный звук: an apple, an hour\n"
        "  • Используется при первом упоминании\n\n"
        "THE (определённый артикль):\n"
        "  • Когда предмет уже известен: «The cat is nice»\n"
        "  • Уникальные предметы: the sun, the moon\n\n"
        "Без артикля:\n"
        "  • Имена: Mary, Moscow\n"
        "  • Несчитаемые в общем смысле: I like music."
    ),

    "падеж": (
        "📖 Падежи в русском языке (кратко)\n\n"
        "1. Именительный (кто? что?): кошка, стол\n"
        "2. Родительный (кого? чего?): кошки, стола\n"
        "3. Дательный (кому? чему?): кошке, столу\n"
        "4. Винительный (кого? что?): кошку, стол\n"
        "5. Творительный (кем? чем?): кошкой, столом\n"
        "6. Предложный (о ком? о чём?): о кошке, о столе\n\n"
        "Совет: задавай вопрос к существительному, чтобы определить падеж!"
    ),

    "глагол": (
        "📖 Глаголы в русском языке\n\n"
        "Спряжение (I тип, -ать/-ять):\n"
        "  Я читаю, Ты читаешь, Он читает\n"
        "  Мы читаем, Вы читаете, Они читают\n\n"
        "Спряжение (II тип, -ить/-еть):\n"
        "  Я говорю, Ты говоришь, Он говорит\n"
        "  Мы говорим, Вы говорите, Они говорят\n\n"
        "Важно: окончание глагола зависит от лица и числа!"
    ),

    "can could": (
        "📖 Модальные глаголы CAN / COULD\n\n"
        "CAN — настоящее время:\n"
        "  • Умение: I can swim.\n"
        "  • Разрешение: Can I sit here?\n"
        "  ❗ После CAN — инфинитив без TO!\n\n"
        "COULD — прошедшее или вежливая просьба:\n"
        "  • Прошлое умение: I could swim when I was 5.\n"
        "  • Просьба: Could you help me?\n\n"
        "❌ Нельзя: I can to swim. / I can swimming."
    ),

    "there is there are": (
        "📖 Конструкция THERE IS / THERE ARE\n\n"
        "THERE IS — для единственного числа:\n"
        "  ✅ There is a cat in the room.\n"
        "  ✅ There is some water.\n\n"
        "THERE ARE — для множественного числа:\n"
        "  ✅ There are two cats.\n"
        "  ✅ There are many people.\n\n"
        "❌ Нельзя: There is two cats. / There are a cat."
    ),

    "степени сравнения": (
        "📖 Степени сравнения прилагательных\n\n"
        "Сравнительная (comparative):\n"
        "  • Короткие: big → bigger, hot → hotter\n"
        "  • Длинные: interesting → more interesting\n\n"
        "Превосходная (superlative):\n"
        "  • Короткие: big → the biggest\n"
        "  • Длинные: interesting → the most interesting\n\n"
        "Примеры:\n"
        "  ✅ This book is bigger than that one.\n"
        "  ✅ She is the most beautiful girl."
    ),

    "местоимение": (
        "📖 Местоимения в английском языке\n\n"
        "Личные (Subject):\n"
        "  I, you, he, she, it, we, they\n\n"
        "Объектные (Object):\n"
        "  me, you, him, her, it, us, them\n\n"
        "Притяжательные:\n"
        "  my, your, his, her, its, our, their\n\n"
        "Примеры:\n"
        "  ✅ He loves her. (не «He loves she»)\n"
        "  ✅ This is my book. (не «This is me book»)"
    ),
}


class GrammarExplainer:

    def explain(self, topic: str) -> str:
        lower = topic.lower().strip()

        if lower in GRAMMAR_TOPICS:
            return GRAMMAR_TOPICS[lower]

        for key, explanation in GRAMMAR_TOPICS.items():
            key_words = key.split()
            if all(word in lower for word in key_words):
                return explanation

        priority_keywords = {
            "past": ["past simple", "past continuous"],
            "present": ["present simple", "present continuous"],
            "future": ["future simple"],
            "артикль": ["артикль"],
            "падеж": ["падеж"],
            "can": ["can could"],
            "could": ["can could"],
            "there": ["there is there are"],
            "степень": ["степени сравнения"],
            "местоим": ["местоимение"],
        }

        for priority_word, topics in priority_keywords.items():
            if priority_word in lower:
                for topic_key in topics:
                    if topic_key in GRAMMAR_TOPICS:
                        return GRAMMAR_TOPICS[topic_key]

        topics_list = "\n".join(f"  • {t}" for t in GRAMMAR_TOPICS.keys())
        return (
            f"🤔 Не нашёл объяснение по теме «{topic}».\n\n"
            f"📚 Доступные темы:\n{topics_list}\n\n"
            f"Например: «объясни present simple» или «расскажи про past simple»"
        )