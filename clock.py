import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QInputDialog, QMessageBox
from PyQt5.QtCore import QTimer, QTime

class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        self.timeLabel = QLabel(self)
        self.timeLabel.setStyleSheet('font-size: 50px')
        self.showTime()

        self.alarmButton = QPushButton('알림 설정', self)
        self.alarmButton.clicked.connect(self.setAlarm)

        layout = QVBoxLayout()
        layout.addWidget(self.timeLabel)
        layout.addWidget(self.alarmButton)

        self.setLayout(layout)
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('시계 알림')
        self.show()

    def showTime(self):
        time = QTime.currentTime()
        timeString = time.toString('hh:mm:ss')
        self.timeLabel.setText(timeString)

    def setAlarm(self):
        alarmTime, ok = QInputDialog.getText(self, '알림 설정', '알림 시간 (HHMM):')
        if ok:
            self.alarmTime = alarmTime
            self.timer.timeout.connect(self.checkAlarm)

    def checkAlarm(self):
        time = QTime.currentTime()
        timeString = time.toString('HHmm')
        if timeString == self.alarmTime:
            QMessageBox.information(self, '알림', '알림이 울립니다.')
            self.timer.timeout.disconnect(self.checkAlarm)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    sys.exit(app.exec_())