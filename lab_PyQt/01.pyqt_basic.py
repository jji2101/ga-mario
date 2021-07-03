#pyqt 기본

import sys
from PyQt5.QtWidgets import QApplication, QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기
        self.setfixedsize(1024,768)
        #창 제목
        self.setWindowTitle('GA Mario')
        #창 띄우기
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyApp()
    sys.exit(app.exec_())