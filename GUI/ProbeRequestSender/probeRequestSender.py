#!/usr/bin/python
 
from PyQt5.QtWidgets import QMainWindow, QWidget, QMessageBox, QApplication
import sys
from packetBuilder import PacketBuilder

import mainWindow
 
class MainWindowUI(QMainWindow, mainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindowUI, self).__init__(parent)
        self.setupUi(self)
        self.buttonClicked.connect(self.on_mybutton_clicked)
        self.pushButton_Choice.clicked.connect(self.on_pushButton_Choice_clicked)
        self.packetBuilder = PacketBuilder()

    def on_pushButton_Choice_clicked(self):
        id = self.requestId.value()
        self.sendProbeRequest(id)
 
    def on_mybutton_clicked(self, id):
        self.sendProbeRequest(id)

    def sendProbeRequest(self, id):
        id_str = '%0.4X' % id
        id_str_1 = id_str[:2]
        id_str_2 = id_str[2:]
        self.packetBuilder.ProbeReq(count=10, source='00:00:00:00:{}:{}'.format(id_str_1, id_str_2))
        self.statusBar.showMessage('Probe request sent with Tag {0}'.format(str(id)))
 
    def main(self):
        self.show()
 
if __name__=='__main__':
    app = QApplication(sys.argv)
    windowUI = MainWindowUI()
    windowUI.main()
    app.exec_()