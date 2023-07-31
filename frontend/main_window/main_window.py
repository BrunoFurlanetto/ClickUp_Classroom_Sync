from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QListWidgetItem

from backend.infra.repository.courses_in_classroom_repository import CoursesInClassroomRepository


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = self.load_window_ui()
        self.courses_list = self.window.classroom_courses
        self.show_courses_synced()
        self.show_window = self.window.show()

    @staticmethod
    def load_window_ui():
        loader = QUiLoader()

        return loader.load('frontend/main_window/main_window.ui')

    def show_courses_synced(self):
        courses = CoursesInClassroomRepository().select_all()

        for course in courses:
            item = QListWidgetItem(course.course_name)
            item.setIcon(QIcon())
            self.courses_list.addItem(item)
