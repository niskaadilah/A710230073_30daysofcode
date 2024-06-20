import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Layout vertikal utama
        vbox = QVBoxLayout()

        # Layout horizontal pertama
        hbox1 = QHBoxLayout()
        btn1 = QPushButton('Button 1', self)
        btn2 = QPushButton('Button 2', self)
        hbox1.addWidget(btn1)
        hbox1.addWidget(btn2)

        # Layout horizontal kedua
        hbox2 = QHBoxLayout()
        btn3 = QPushButton('Button 3', self)
        btn4 = QPushButton('Button 4', self)
        hbox2.addWidget(btn3)
        hbox2.addWidget(btn4)

        # Menambahkan layout horizontal ke layout vertikal utama
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        # Mengatur layout vertikal utama sebagai layout jendela
        self.setLayout(vbox)

        self.setWindowTitle('PyQt5 Layout Example')
        self.setGeometry(300, 300, 300, 200)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
