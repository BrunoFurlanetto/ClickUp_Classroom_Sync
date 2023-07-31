from PySide6.QtUiTools import QUiLoader

from frontend.app.app import App
from frontend.main_window.main_window import MainWindow

app = App()
main_window = MainWindow()

if __name__ == '__main__':
    app.exec()
