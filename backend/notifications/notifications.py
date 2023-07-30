from plyer import notification


class Alert:
    def __init__(self, title, message):
        self.title = title
        self.message = message
        self.__icon = None

    def __notify(self):
        notification.notify(
            title=self.title,
            message=self.message,
            app_icon=self.__icon,
        )

    def success(self):
        self.__icon = r'notifications/icons/success.ico'
        self.__notify()

    def warning(self):
        self.__icon = r'notifications/icons/warning.ico'
        self.__notify()

    def error(self):
        self.__icon = r'notifications/icons/error.ico'
        self.__notify()
