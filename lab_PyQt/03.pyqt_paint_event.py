# 03.pyqt_paint_event.py
# paint event
import sys
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(200, 300)
        self.setWindowTitle('GA Mario')
        self.show()

    # 창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        # 그리기 도구
        painter = QPainter()
        # 그리기 시작
        painter.begin(self)

        # 펜 설정 (테두리)
        painter.setPen(QPen(Qt.black, 2.0, Qt.SolidLine))

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0, 0, 0), 1.0, Qt.SolidLine))


        # 파랑 직사각형
        painter.setBrush(QBrush(Qt.blue))
        painter.drawRect(0, 0, 50, 50)
        # 빨강 직사각형
        painter.setBrush(QBrush(Qt.red))
        painter.drawRect(50, 50, 50, 50)
        # 빈 직사각형
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(0, 50, 50, 50)
        # 빈 직사각형
        painter.setBrush(QBrush(Qt.white))
        painter.drawRect(50, 0, 50, 50)

        # 파랑선
        painter.setPen(QPen(Qt.blue, 2.0, Qt.SolidLine))
        painter.drawLine(75, 175, 75, 250)
        # 빨강선
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        painter.drawLine(30, 175, 75, 250)
        # 빨강선2
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        painter.drawLine(120, 175, 75, 250)


        painter.setPen(QPen(Qt.black, 1.0, Qt.SolidLine))
        # 청록원1
        painter.setBrush(QBrush(QColor.fromRgb(0, 255, 255)))
        painter.drawEllipse(15, 150, 30, 30)
        # 청록원2
        painter.setBrush(QBrush(QColor.fromRgb(0, 255, 255)))
        painter.drawEllipse(100, 150, 30, 30)
        # 하얀원
        painter.setBrush(QBrush(QColor.fromRgb(255, 250, 250)))
        painter.drawEllipse(60, 150, 30, 30)
        # 회색원
        painter.setBrush(QBrush(QColor.fromRgb(128, 128, 128)))
        painter.drawEllipse(60, 230, 30, 30)


        painter.end()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   window = MyApp()
   sys.exit(app.exec_())