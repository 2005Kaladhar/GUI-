from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ui_newuiDesign import Ui_MainWindow as mainScreen
import sys

class MainApplication(QMainWindow):
    def __init__(self):
        super(MainApplication, self).__init__()
        self.ui = mainScreen()
        self.ui.setupUi(self)

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)

        self.ui.Minimizebtn.clicked.connect(lambda: self.showMinimized())
        self.ui.Maximizebtn.clicked.connect(self.maxi)
        self.ui.CloseButton.clicked.connect(lambda: quit())

        self.windowDimension = QApplication.desktop().screenGeometry()



        def moveWindow(e):
            screenGeo = QApplication.desktop().screenGeometry()
            fullscreen = (self.height(), self.width()) == (screenGeo.height(), screenGeo.width())

            if not fullscreen:
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
            else:
                self.setGeometry(self.prevGeo.x(), e.globalPos().y(), self.prevGeo.width(),
                                 self.prevGeo.height())
                # self.setGeometry(self.prevGeo)

        self.ui.BottomDrag.mouseMoveEvent = moveWindow
        self.ui.TopDragFrame.mouseMoveEvent = moveWindow

        QSizeGrip(self.ui.QSizeGrip_botto_right)

        self.show()

    def mousePressEvent(self,event):
        self.clickPosition = event.globalPos()

    def maxi(self,extra=None):
        screenGeo = QApplication.desktop().screenGeometry()
        fullscreen = (self.height(), self.width() )==(613, 914)
        # print(f"is it fullscreen ??? : {fullscreen}")

        if fullscreen :
            # self.setGeometry(self.prevGeo)
            self.resizeWindowAnimation(expand=False)
        else:
            self.prevGeo = self.geometry()
            # self.setGeometry(screenGeo)
            self.resizeWindowAnimation(expand=True)


    def resizeWindowAnimation(self, expand=True):
        start_Val = self.geometry()
        end_val = self.windowDimension
        duration = 80
        easingCurve = QEasingCurve.InBack

        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(duration)

        if not expand:
            start_Val = self.geometry()
            end_val = self.prevGeo
            easingCurve = QEasingCurve.InQuad

        self.animation.setEasingCurve(easingCurve)
        self.animation.setStartValue(start_Val)
        self.animation.setEndValue(end_val)
        self.animation.start()

if __name__ == '__main__':
    app = QApplication()
    window = MainApplication()
    sys.exit(app.exec_())

