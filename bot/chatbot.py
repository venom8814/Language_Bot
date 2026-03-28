from services.translator import Translator
from services.exercise_generator import ExerciseGenerator
from services.intent_detector import IntentDetector, Intent


class ChatBot:

    def __init__(
        self,
        translator: Translator,
        corrector: None,
        exercise_gen: ExerciseGenerator,
        intent_detector: IntentDetector,
    ):
        self.translator    = translator
        self.corrector     = corrector
        self.exercise_gen  = exercise_gen
        self.intent_detector = intent_detector

        self._active_exercise: dict | None = None

    def respond(self, user_input: str) -> str:

        text = user_input.strip()

        if self._active_exercise:
            return self._check_exercise_answer(text)

        intent, payload = self.intent_detector.detect(text)

        match intent:
            case Intent.TRANSLATE:
                return self._handle_translate(payload or text)
            case Intent.EXERCISE:
                return self._handle_exercise()
            case Intent.EXPLAIN:
                return self._handle_explain(payload or text)
            case Intent.HELP:
                return self._help_message()
            case _:
                return self._handle_unknown(text)


    def _handle_translate(self, text: str) -> str:
        result = self.translator.translate(text)
        direction = result["direction"]
        translated = result["translated"]
        original   = result["original"]
        return (
            f"🔤 Перевод ({direction}):\n"
            f"  «{original}» → «{translated}»"
        )



    def _handle_exercise(self) -> str:
        exercise = self.exercise_gen.generate()
        self._active_exercise = exercise
        return (
            f"📝 Упражнение ({exercise['type']}):\n\n"
            f"{exercise['question']}\n\n"
            f"_(Введи свой ответ)_"
        )

    def _handle_explain(self, topic: str) -> str:
        from services.grammar_explainer import GrammarExplainer
        explainer = GrammarExplainer()
        return explainer.explain(topic)

    def _handle_unknown(self, text: str) -> str:
        result = self.translator.translate(text)
        if result["translated"] != text:
            return (
                f"🤔 Не совсем понял запрос, но попробовал перевести:\n"
                f"  «{result['original']}» → «{result['translated']}»\n\n"
                f"Напиши \'помощь\' чтобы увидеть все команды."
            )
        return (
            "🤔 Не понял запрос. Попробуй:\n"
            "  • «переведи cat»\n"
            "  • «проверь: я пишет письмо»\n"
            "  • «упражнение»\n"
            "  • «помощь»"
        )

    def _check_exercise_answer(self, user_answer: str) -> str:
        exercise = self._active_exercise
        self._active_exercise = None

        correct = exercise["answer"].strip().lower()
        given   = user_answer.strip().lower()

        if given == correct:
            return (
                f"🎉 Правильно! Отлично!\n\n"
                f"✅ Ответ: «{exercise['answer']}»\n\n"
                f"Хочешь ещё? Напиши «упражнение»."
            )
        else:
            return (
                f"❌ Не совсем верно.\n\n"
                f"Твой ответ:    «{user_answer}»\n"
                f"Правильный:    «{exercise['answer']}»\n\n"
                f"{exercise.get('explanation', '')}\n"
                f"Не расстраивайся! Напиши «упражнение» чтобы попробовать ещё."
            )

    def _help_message(self) -> str:
        return (
            "📖 Что я умею:\n\n"
            "🔤 Перевод:\n"
            "   • «переведи cat» / «translate кошка»\n"
            "   • «как будет по-английски: привет»\n\n"
            "📝 Упражнения:\n"
            "   • «упражнение» / «задание» / «тест»\n\n"
            "📖 Объяснение грамматики:\n"
            "   • «объясни present simple»\n"
            "   • «расскажи про падежи»\n\n"
            "ℹ️  Просто напиши слово или фразу — попробую перевести!"
        )
