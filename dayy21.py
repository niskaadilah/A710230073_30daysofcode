import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSlider, QComboBox
from PyQt5.QtCore import Qt

class ACRemote(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Remote AC')
        self.setGeometry(100, 100, 300, 300)
        
        # Layout utama
        mainLayout = QVBoxLayout()
        
        # Status AC
        self.statusLabel = QLabel('Status: OFF', self)
        mainLayout.addWidget(self.statusLabel)
        
        # Tombol ON/OFF
        self.onOffButton = QPushButton('Turn ON', self)
        self.onOffButton.clicked.connect(self.togglePower)
        mainLayout.addWidget(self.onOffButton)
        
        # Pengaturan suhu
        tempLayout = QHBoxLayout()
        tempLabel = QLabel('Temperature:', self)
        self.tempSlider = QSlider(Qt.Horizontal, self)
        self.tempSlider.setRange(16, 30)
        self.tempSlider.setValue(24)
        self.tempSlider.valueChanged.connect(self.changeTemperature)
        self.tempValueLabel = QLabel('24°C', self)
        tempLayout.addWidget(tempLabel)
        tempLayout.addWidget(self.tempSlider)
        tempLayout.addWidget(self.tempValueLabel)
        mainLayout.addLayout(tempLayout)
        
        # Pengaturan mode
        modeLayout = QHBoxLayout()
        modeLabel = QLabel('Mode:', self)
        self.modeCombo = QComboBox(self)
        self.modeCombo.addItems(['Cool', 'Dry', 'Fan', 'Heat'])
        self.modeCombo.currentIndexChanged.connect(self.changeMode)
        modeLayout.addWidget(modeLabel)
        modeLayout.addWidget(self.modeCombo)
        mainLayout.addLayout(modeLayout)
        
        # Pengaturan kecepatan kipas
        fanSpeedLayout = QHBoxLayout()
        fanSpeedLabel = QLabel('Fan Speed:', self)
        self.fanSpeedCombo = QComboBox(self)
        self.fanSpeedCombo.addItems(['Low', 'Medium', 'High', 'Auto'])
        self.fanSpeedCombo.currentIndexChanged.connect(self.changeFanSpeed)
        fanSpeedLayout.addWidget(fanSpeedLabel)
        fanSpeedLayout.addWidget(self.fanSpeedCombo)
        mainLayout.addLayout(fanSpeedLayout)
        
        self.setLayout(mainLayout)
        
        # Inisialisasi status AC
        self.ac_on = False
        self.current_temperature = 24
        self.current_mode = 'Cool'
        self.current_fan_speed = 'Auto'
    
    def togglePower(self):
        self.ac_on = not self.ac_on
        if self.ac_on:
            self.statusLabel.setText('Status: ON')
            self.onOffButton.setText('Turn OFF')
        else:
            self.statusLabel.setText('Status: OFF')
            self.onOffButton.setText('Turn ON')
        self.updateStatus()
    
    def changeTemperature(self):
        self.current_temperature = self.tempSlider.value()
        self.tempValueLabel.setText(f'{self.current_temperature}°C')
        self.updateStatus()
    
    def changeMode(self):
        self.current_mode = self.modeCombo.currentText()
        self.updateStatus()
    
    def changeFanSpeed(self):
        self.current_fan_speed = self.fanSpeedCombo.currentText()
        self.updateStatus()
    
    def updateStatus(self):
        if self.ac_on:
            status = f'Status: ON | Temp: {self.current_temperature}°C | Mode: {self.current_mode} | Fan: {self.current_fan_speed}'
        else:
            status = 'Status: OFF'
        self.statusLabel.setText(status)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ACRemote()
    ex.show()
    sys.exit(app.exec_())
