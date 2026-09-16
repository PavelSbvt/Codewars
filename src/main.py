import sys

from PyQt6.QtWidgets import QApplication

from gui.main_window import MainWindow
from utils.output_rich import Rich


def run() -> None:
    """
    Функция для запуска файлов с решениями задач с codewars

    :return: None
    """

    App = QApplication(sys.argv)
    App.setApplicationName("Codewars decisions")
    Win = MainWindow()
    Win.show()
    sys.exit(App.exec())

if __name__ == "__main__":
    run()