import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout Vertikal
        layout = QVBoxLayout()

        # Label
        self.label = QLabel("Tekan tombol di bawah", self)
        layout.addWidget(self.label)

        # Tombol
        btn = QPushButton("Tekan Saya", self)
        btn.clicked.connect(self.on_click)
        layout.addWidget(btn)

        # Set Layout
        self.setLayout(layout)

        # Set Jendela
        self.setWindowTitle('Aplikasi Sederhana')
        self.show()

    def on_click(self):
        self.label.setText("Tombol ditekan!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    sys.exit(app.exec_())
