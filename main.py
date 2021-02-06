from Main_window import Ui_MainWindow
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog , QApplication
import requests
import time
t = -1

class downloader_class(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.ui.Browse.clicked.connect(self.browse_file)
        self.ui.Start_download.clicked.connect(self.start_download)
        self.ui.cancelall.clicked.connect(self.cancelalldownload)
        self.ui.pauseall.clicked.connect(self.pausealldownload)
        self.ui.resumeall.clicked.connect(self.resumealldownlaod)

        # self.ui.gridLayout_3 = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents)
        # self.ui.gridLayout_3.setObjectName("gridLayout_3")

        self.MainWindow.show()
        sys.exit(self.app.exec_())
    def start_download(self):
            # file_link = self.ui.File_link.text()
            # file_location = self.ui.File_location.text()
            # self.ui.File_location.setText('')
            # self.ui.File_link.setText('')
            # self.ui.gridLayout_3 = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents_2)
            # self.ui.gridLayout_3.setObjectName("gridLayout_3")
            a = download_requests()
            a.do_download(self.ui,self.ui.File_link,self.ui.File_location)
            # self.ui.gridLayout_3 = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents_2)
            # self.ui.gridLayout_3.setObjectName("gridLayout_3")
            # self.ui.out_file_location = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_2)
            # self.ui.out_file_location.setObjectName("out_file_location")
            # self.ui.gridLayout_3.addWidget(self.ui.out_file_location, 0, 5, 5, 5)
            # self.ui.out_file_location.setText("FILE LOCATION->{}".format(file_location))
            # self.ui.gridLayout_3 = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents_2)
            # self.ui.gridLayout_3.setObjectName("gridLayout_3")
            # self.File_location = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            # self.File_location.setObjectName("File_location")
            # self.gridLayout_2.addWidget(self.File_location, 3, 1, 1, 1)

    def cancelalldownload(self):
        print("Hello Cancel")
    def pausealldownload(self):
        print("Hello Pause")
    def resumealldownlaod(self):
        print("Hello Resume")
    def browse_file(self):
        self.open_dialog_box()

    def open_dialog_box(self):
        file_location = QFileDialog.getSaveFileName()
        self.ui.File_location.setText(file_location[0])


class  download_requests(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def do_download(self,ui,File_link,File_location):
        global t
        t = t + 1
        file_link = File_link.text()
        file_location = File_location.text()
        File_location.setText('')
        File_link.setText('')
        print(file_location,file_link,t)
        # self.ui.gridLayout_3 = QtWidgets.QGridLayout(self.ui.scrollAreaWidgetContents_2)
        # self.ui.gridLayout_3.setObjectName("gridLayout_3")
        # self.ui.out_file_location = QtWidgets.QLabel(self.ui.scrollAreaWidgetContents_2)
        # self.ui.out_file_location.setObjectName("out_file_location")
        # self.ui.gridLayout_3.addWidget(self.ui.out_file_location, 0, 5, 5, 5)
        # self.ui.out_file_location.setText("FILE LOCATION->{}".format(file_location))
        ui.gridLayout_3 = QtWidgets.QGridLayout(ui.scrollAreaWidgetContents_2)
        ui.gridLayout_3.setObjectName("gridLayout_3")
        ui.out_file_location = QtWidgets.QLabel(ui.scrollAreaWidgetContents_2)
        ui.out_file_location.setObjectName("out_file_location")
        ui.gridLayout_3.addWidget(ui.out_file_location , 0 , 5 , 5 , 5)
        ui.out_file_location.setText("FILE LOCATION->{}".format(file_location))
if __name__ == "__main__":
    downloader_class()