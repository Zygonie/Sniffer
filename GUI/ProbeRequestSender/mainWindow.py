# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Mon Apr 04 16:24:35 2016
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal

class Ui_MainWindow(object):
    #Define new signal with parameter
    buttonClicked = pyqtSignal(int, name="buttonClicked")

    #Fonts
    font20 = QtGui.QFont()
    font20.setPointSize(20)

    def on_button_clicked(self):
        sender = self.sender()
        self.buttonClicked.emit(int(sender.text()))

    def setupUi(self, MainWindow):
        #Main Window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)

        #Main Widget
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        
        #Layout
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 231))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")

        #Tag buttons
        for i in xrange(6):                        
            self.createButton(i)

        #Choice Button
        self.pushButton_Choice = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_Choice.setMinimumSize(QtCore.QSize(0, 50))
        
        #Choice button
        self.pushButton_Choice.setFont(self.font20)
        self.pushButton_Choice.setObjectName("pushButton_Choice")
        self.gridLayout.addWidget(self.pushButton_Choice, 1, 2, 1, 1)

        #Id on SpinBox
        self.requestId = QtWidgets.QSpinBox(self.gridLayoutWidget)
        self.requestId.setFont(self.font20)
        self.requestId.setObjectName("requestId")
        self.gridLayout.addWidget(self.requestId, 0, 2, 1, 1)
        
        #MenuBar
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        #ToolBar
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def createButton(self, n):
        row = n % 3
        col = n / 3
        button = QtWidgets.QPushButton(self.gridLayoutWidget)
        button.setMinimumSize(QtCore.QSize(0, 50))
        button.setFont(self.font20)
        button.setText(str(n + 1))
        button.setObjectName("pushButton_" + str(n + 1))
        button.clicked.connect(self.on_button_clicked)
        self.gridLayout.addWidget(button, row, col, 1, 1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Send Probe Request with Tag"))
        self.pushButton_Choice.setText(_translate("MainWindow", "Custom Tag"))