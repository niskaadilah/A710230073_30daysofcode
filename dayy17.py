from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title
        self.setWindowTitle("PyQt Widget Example")

        # Create layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Create label
        self.label = QLabel("Hello, world!")
        self.layout.addWidget(self.label)

        # Create button
        self.button = QPushButton("Click Me!")
        self.button.clicked.connect(self.on_click)
        self.layout.addWidget(self.button)

    def on_click(self):
        # Function to handle button click
        self.label.setText("Button clicked!")


if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
