from PyQt5 import QtWidgets, QtCore, QtGui
from browser import Ui_Form
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import sys


class moveWidget(QtWidgets.QWidget):
    def __init__(self):
        super(moveWidget, self).__init__()

    def mousePressEvent(self, event: QtGui.QMouseEvent):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        if event.buttons() == QtCore.Qt.MouseButton.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class Browser(moveWidget, Ui_Form):
    def __init__(self):
        super(Browser, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(lambda: self.showMinimized())
        self.pushButton_3.clicked.connect(lambda: self.winShowMaximized())
        self.pushButton.clicked.connect(lambda: sys.exit())
        self.pushButton_4.clicked.connect(self.refresh)
        self.pushButton_5.clicked.connect(self.forward)
        self.pushButton_6.clicked.connect(self.backward)
        self.lineEdit.returnPressed.connect(self.load)

    def load(self):
        url = QtCore.QUrl.fromUserInput(self.lineEdit.text())
        if url.isValid():
            self.webEngineView.load(url)

    def backward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Back)
        
    def forward(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Forward)

    def refresh(self):
        self.webEngineView.page().triggerAction(QWebEnginePage.WebAction.Reload)

    def winShowMaximized(self):
        if self.pushButton_3.isChecked():
            self.setWindowState(QtCore.Qt.WindowState.WindowMaximized)
        else:
            self.setWindowState(QtCore.Qt.WindowState.WindowActive)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    form = Browser()
    form.show()
    sys.exit(app.exec_())
