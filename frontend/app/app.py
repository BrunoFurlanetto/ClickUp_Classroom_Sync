from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet


class App(QApplication):
    def __init__(self):
        super().__init__()
        self.setFont(QFont("Times New Roman", 12))
        self.__stylesheet = apply_stylesheet(self, theme='dark_red.xml')
