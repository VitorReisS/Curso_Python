import sys
from PySide6.QtGui import QIcon
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()