from ui.app_window import AppWindow
from bot.chatbot import ChatBot
from services.translator import Translator
from services.exercise_generator import ExerciseGenerator
from services.intent_detector import IntentDetector
from storage.history_manager import HistoryManager


def main():
    translator = Translator()
    exercise_gen = ExerciseGenerator(translator)
    intent_detector = IntentDetector()
    history_manager = HistoryManager()

    chatbot = ChatBot(
        translator=translator,
        corrector=None,
        exercise_gen=exercise_gen,
        intent_detector=intent_detector,
    )

    app = AppWindow(chatbot=chatbot, history_manager=history_manager)
    app.run()


if __name__ == "__main__":
    main()
