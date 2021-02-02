from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog , QApplication
import requests
import time
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(893, 560)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(290, 0, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setObjectName("Heading")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.File_link = QtWidgets.QLineEdit(self.centralwidget)
        self.File_link.setGeometry(QtCore.QRect(440, 60, 431, 21))
        self.File_link.setText("")
        self.File_link.setObjectName("File_link")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.File_location = QtWidgets.QLineEdit(self.centralwidget)
        self.File_location.setGeometry(QtCore.QRect(440, 90, 341, 21))
        self.File_location.setText("")
        self.File_location.setObjectName("File_location")
        self.Browse_Files = QtWidgets.QPushButton(self.centralwidget)
        self.Browse_Files.setGeometry(QtCore.QRect(780, 90, 91, 21))
        self.Browse_Files.clicked.connect(self.browse_file)  ###################3

        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Browse_Files.setFont(font)
        self.Browse_Files.setObjectName("Browse_Files")
        self.Start_Download = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Download.setGeometry(QtCore.QRect(330, 120, 201, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Start_Download.setFont(font)
        self.Start_Download.setAutoDefault(False)
        self.Start_Download.setObjectName("Start_Download")
        self.Start_Download.clicked.connect(self.start_download)  ########################3

        self.pause_all = QtWidgets.QPushButton(self.centralwidget)
        self.pause_all.setGeometry(QtCore.QRect(630, 520, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pause_all.setFont(font)
        self.pause_all.setObjectName("pause_all")
        self.cancel_all = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_all.setGeometry(QtCore.QRect(760, 520, 101, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_all.setFont(font)
        self.cancel_all.setObjectName("cancel_all")
        self.resume_all = QtWidgets.QPushButton(self.centralwidget)
        self.resume_all.setGeometry(QtCore.QRect(500, 520, 111, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.resume_all.setFont(font)
        self.resume_all.setObjectName("resume_all")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(9, 156, 871, 361))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 869, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.progressBar1 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents)
        self.progressBar1.setGeometry(QtCore.QRect(20, 40, 821, 23))
        self.progressBar1.setProperty("value", 0)
        self.progressBar1.setObjectName("progressBar1")
        self.Filename1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Filename1.setGeometry(QtCore.QRect(20, 10, 781, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Filename1.setFont(font)
        self.Filename1.setObjectName("Filename1")
        self.cancel1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.cancel1.setGeometry(QtCore.QRect(270, 70, 121, 28))
        self.cancel1.clicked.connect(self.canceldownload)  ########################3

        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.cancel1.setFont(font)
        self.cancel1.setObjectName("cancel1")
        self.Pause1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Pause1.setGeometry(QtCore.QRect(20, 70, 121, 28))
        self.Pause1.clicked.connect(self.pausedownload)

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Pause1.setFont(font)
        self.Pause1.setObjectName("Pause1")
        self.Resume1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Resume1.setGeometry(QtCore.QRect(140, 70, 131, 28))
        self.Resume1.clicked.connect(self.resumedownlaod)##############################################

        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Resume1.setFont(font)
        self.Resume1.setObjectName("Resume1")
        self.timeremaning1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.timeremaning1.setGeometry(QtCore.QRect(20, 100, 221, 20))
        self.timeremaning1.setObjectName("timeremaning1")
        self.downloaded1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.downloaded1.setGeometry(QtCore.QRect(480, 70, 301, 30))
        self.downloaded1.setObjectName("downloaded1")
        self.TimeTaken1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.TimeTaken1.setGeometry(QtCore.QRect(254, 100, 191, 20))
        self.TimeTaken1.setObjectName("TimeTaken1")
        self.DownlaodSpeed1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DownlaodSpeed1.setGeometry(QtCore.QRect(504, 100, 241, 21))
        self.DownlaodSpeed1.setObjectName("DownlaodSpeed1")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Heading.setText(_translate("MainWindow", "File Downloader "))
        self.label.setText(_translate("MainWindow", "Enter the URL of file you want to download ->"))
        self.File_link.setPlaceholderText(_translate("MainWindow", "Please enter the Link"))
        self.label_2.setText(_translate("MainWindow", "Enter the location of your file to be saved ->"))
        self.File_location.setPlaceholderText(_translate("MainWindow", "Please enter the Location You want to save"))
        self.Browse_Files.setText(_translate("MainWindow", "Browse"))
        self.Start_Download.setText(_translate("MainWindow", "Start The Download "))
        self.pause_all.setText(_translate("MainWindow", "Pause All"))
        self.cancel_all.setText(_translate("MainWindow", "Cancel All"))
        self.resume_all.setText(_translate("MainWindow", "Resume All"))
        self.Filename1.setText(_translate("MainWindow", "FILE LOCATION ->"))
        self.cancel1.setText(_translate("MainWindow", "Cancel Download"))
        self.Pause1.setText(_translate("MainWindow", "Pause Download"))
        self.Resume1.setText(_translate("MainWindow", "Resume Download"))
        self.timeremaning1.setText(_translate("MainWindow", "TIME REMAIN->"))
        self.downloaded1.setText(_translate("MainWindow", "DOWNLOADED->"))
        self.TimeTaken1.setText(_translate("MainWindow", "TIME TAKEN ->"))
        self.DownlaodSpeed1.setText(_translate("MainWindow", "DOWNLOAD SPEED->"))

######################################################################################################################3
    def start_download(self):
        file_link = self.File_link.text()
        file_location = self.File_location.text()
        #import downloading as dow
        self.File_location.setText('')
        self.File_link.setText('')
        self.Filename1.setText("FILE LOCATION ->"+file_location)

        with open(file_location, 'wb') as f:
            response = requests.get(file_link, allow_redirects=True, stream=True)
            total_length = response.headers.get("content-length")
            start = time.time()
            if total_length is None:
                f.write(response.content)
                self.progressBar1.setValue(100)
                self.downloaded1.setText("DOWNLOADED-> 1/1")
            else:
                dl = 0
                total_length = int(total_length)
                for data in response.iter_content(chunk_size=1024):
                    # if canceler:
                    #     os.remove(file_location)
                    # else:
                        dl += len(data)
                        if data:
                            f.write(data)
                            f.flush()
                        done = int(100 * dl / total_length)
                        self.downloaded1.setText("DOWNLOADED->{}MB/{}MB".format(str(dl/(1024*1024))[:8],str(total_length/(1024*1024))[:8]))
                        #time.sleep(0.1)
                        if time.time()!=start:
                            speed = (dl//(time.time()-start))
                            try:
                                remain = (total_length-dl)/(speed)
                                if remain>60:
                                    remain_min = remain//60
                                    remain_sec = remain-(remain_min*60)
                                    self.timeremaning1.setText("TIME REMAIN->{}min{}sec".format(str(remain_min),str(remain_sec)[:2]))
                                else:
                                    self.timeremaning1.setText("TIME REMAIN->{}sec".format(remain[:2]))

                            except:
                                self.timeremaning1.setText("TIME REMAIN->{}".format('9999999999'))
                            if speed>(1024*1024):
                                self.DownlaodSpeed1.setText('DOWNLOAD SPEED->{}MBps'.format(str(speed/(1024*1024))[:6]))
                            else:
                                self.DownlaodSpeed1.setText("DOWNLOAD SPEED->{}KBps".format(str(speed/1024)[:5]))
                        temp = time.time()-start
                        if (temp)>60:
                            self.TimeTaken1.setText("TIME TAKEN->{}min{}sec".format(str(temp//60),str(temp-temp//60)[:2]))
                        else:
                            self.TimeTaken1.setText('TIME TAKEN->{}sec'.format(str(temp)[:2]))
                        self.progressBar1.setValue(done)
                        QApplication.processEvents()
                self.progressBar1.setValue(100)
                self.downloaded1.setText("DOWNLOADED->{}/{}".format(str(total_length),str(total_length)))
    def canceldownload(self):
        print("Hello Cancel")
    def pausedownload(self):
        print("Hello Pause")
    def resumedownlaod(self):
        print("Hello Resume")

    def browse_file(self):
        self.open_dialog_box()
    def open_dialog_box(self):
        file_location = QFileDialog.getSaveFileName()
        self.File_location.setText(file_location[0])
#####################################################################################################################

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
