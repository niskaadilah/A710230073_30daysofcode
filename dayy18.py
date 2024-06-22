import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Simple Example')
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.show_message)

        layout.addWidget(self.button)

        self.setLayout(layout)

    def show_message(self):
        QMessageBox.information(self, "Message", "You clicked the button!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
