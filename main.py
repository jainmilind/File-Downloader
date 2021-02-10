from Main_window import Ui_MainWindow
import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from downloading import download_requests
import concurrent.futures
import threading
count = 0
# import time
# start = time.time()
class downloader_class(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        self.thread = {}
        self.obj = {}
        self.ui.Browse.clicked.connect(self.browse_file)
        self.ui.Start_download.clicked.connect(self.start_download)
        self.ui.cancelall.clicked.connect(self.cancelalldownload)
        self.ui.pauseall.clicked.connect(self.pausealldownload)
        self.ui.resumeall.clicked.connect(self.resumealldownlaod)

        self.MainWindow.show()
        sys.exit(self.app.exec_())

    def start_download(self):
        global count
        count+=1

        # self.obj[count] = download_requests()
        #
        # threading.Thread(target = self.obj[count].do_download,args = [self.ui,self.ui.File_link,self.ui.File_location]).start()
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = download_requests()
        self.worker.moveToThread(self.thread)
        self.worker.do_download(self.ui,self.ui.File_link,self.ui.File_location)
        self.thread.start()
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

if __name__ == "__main__":
    downloader_class()