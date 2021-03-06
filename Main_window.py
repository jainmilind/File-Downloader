# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 650)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainscrollarea = QtWidgets.QScrollArea(self.centralwidget)
        self.mainscrollarea.setWidgetResizable(True)
        self.mainscrollarea.setObjectName("mainscrollarea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 976, 575))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.File_location = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.File_location.setObjectName("File_location")
        self.gridLayout_2.addWidget(self.File_location, 3, 1, 1, 1)
        self.Browse = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.Browse.setFont(font)
        self.Browse.setObjectName("Browse")
        self.gridLayout_2.addWidget(self.Browse, 3, 2, 1, 1)
        self.File_link = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.File_link.setObjectName("File_link")
        self.gridLayout_2.addWidget(self.File_link, 2, 1, 1, 2)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.Start_download = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Start_download.setFont(font)
        self.Start_download.setObjectName("Start_download")
        self.gridLayout_2.addWidget(self.Start_download, 4, 1, 1, 2)
        self.downloadscrollarea = QtWidgets.QScrollArea(self.scrollAreaWidgetContents)
        self.downloadscrollarea.setWidgetResizable(True)
        self.downloadscrollarea.setObjectName("downloadscrollarea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 952, 364))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.downloadscrollarea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        for i in range(1,100):
            self.lab = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
            self.lab.setObjectName("lab")
            self.gridLayout_3.addWidget(self.lab,i,0,1,6)
            self.lab.setText('')
        self.gridLayout_2.addWidget(self.downloadscrollarea, 5, 0, 1, 3)
        self.Heading = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.gridLayout_2.addWidget(self.Heading, 1, 0, 1, 1)
        self.cancelall = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cancelall.setFont(font)
        self.cancelall.setObjectName("cancelall")
        self.gridLayout_2.addWidget(self.cancelall, 6, 2, 1, 1)
        self.resumeall = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resumeall.setFont(font)
        self.resumeall.setObjectName("resumeall")
        self.gridLayout_2.addWidget(self.resumeall, 6, 1, 1, 1)
        self.pauseall = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pauseall.setObjectName("pauseall")
        self.gridLayout_2.addWidget(self.pauseall, 6, 0, 1, 1)
        self.mainscrollarea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.mainscrollarea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "File Downloader"))
        self.File_location.setPlaceholderText(_translate("MainWindow", "Please Enter location where you want to save"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.File_link.setPlaceholderText(_translate("MainWindow", "Please enter the link "))
        self.label.setText(_translate("MainWindow", "Enter the location of file to be saved ->"))
        self.label_2.setText(_translate("MainWindow", "Enter the URL Of file you want to download->"))
        self.Start_download.setText(_translate("MainWindow", "START THE DOWNLOAD "))
        self.Heading.setText(_translate("MainWindow", "FILE DOWNLOADER "))
        self.cancelall.setText(_translate("MainWindow", "CANCEL ALL"))
        self.resumeall.setText(_translate("MainWindow", "RESUME ALL"))
        self.pauseall.setText(_translate("MainWindow", "PAUSE ALL"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
