#!/usr/bin/python
 
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QApplication
import sys

import mainWindow
 
class MainWindowUI(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowUI, self).__init__(parent)
        self.setupUi(self)
        self.buttonClicked.connect(self.on_mybutton_clicked)
        self.pushButton_Choice.clicked.connect(self.on_pushButton_Choice_clicked)

    def on_pushButton_Choice_clicked(self):
            id = self.requestId.value()
            self.sendProbeRequest(id)
 
    def on_mybutton_clicked(self, id):
    	self.sendProbeRequest(id)

    def sendProbeRequest(self, id):
        self.statusBar.showMessage('Probe request sent with Tag {0}'.format(str(id)))
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QApplication(sys.argv)
    windowUI = MainWindowUI()
    windowUI.main()
    app.exec_()