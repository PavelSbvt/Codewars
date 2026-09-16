import sys
from pathlib import Path
from typing import Optional, List, Dict, Any

from PyQt6.QtCore import QPoint, Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QTabWidget, QPushButton,
    QProgressBar, QRadioButton, QButtonGroup, QLineEdit, QApplication,
    QMessageBox, QMainWindow, QVBoxLayout, QHBoxLayout, QScrollArea, QSlider)

from utils.output_rich import Rich


class MainWindow(QMainWindow):
    """
    Класс для нового главного окна
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("MainWindow")

        self.setMinimumSize(900, 650)

        self.setStyleSheet("background-color: white;")

    def mousePressEvent(self, event) -> None:
        """
        Обработчик события нажатия кнопки мыши.

        :param event: Принимает event - объект события, содержащий информацию о нажатии
        (какая кнопка, координаты и т.д.).

        :return: None
        """

        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_position = event.globalPosition().toPoint()
            event.accept()


    def mouseMoveEvent(self, event) -> None:
        """
        Обработчик события движения мыши.

        :param event: Принимает event - объект события, содержащий информацию о нажатии
        (какая кнопка, координаты и т.д.).

        :return: None
        """

        if event.buttons() == Qt.MouseButton.LeftButton:
            delta = event.globalPosition().toPoint() - self.drag_position
            self.move(self.pos() + delta)
            self.drag_position = event.globalPosition().toPoint()
            event.accept()

if __name__ == "__main__":

    App = QApplication(sys.argv)
    App.setApplicationName("Codewars decisions")
    Win = MainWindow()
    Win.show()
    sys.exit(App.exec())