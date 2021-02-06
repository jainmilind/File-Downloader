import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import requests
import time
t = -1
class  download_requests():
    def do_download(self,ui,File_link,File_location):
        global t
        t = t+ 1

        def canceldownload():
            print("Hi cancel1")
        def pausedownload():
            print("Hi Pause1")
        def resumedownload():
            print("Hi Resume1")
        file_link = File_link.text()
        file_location = File_location.text()
        File_location.setText('')
        File_link.setText('')
        print(file_location,file_link,t)
        ui.out_file_location = QtWidgets.QLabel(ui.scrollAreaWidgetContents_2)
        ui.out_file_location.setObjectName("out_file_location")
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(100)
        ui.out_file_location.setFont(font)
        ui.progressBar1 = QtWidgets.QProgressBar(ui.scrollAreaWidgetContents_2)
        ui.progressBar1.setProperty("value", 0)
        ui.progressBar1.setObjectName("progressBar1")

        ui.cancel1 = QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        ui.cancel1.setFont(font)
        ui.cancel1.setObjectName("cancel1")
        ui.cancel1.setText("CANCEL DOWNLOAD")
        ui.cancel1.clicked.connect(canceldownload)

        ui.pause1 = QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        ui.pause1.setFont(font)
        ui.pause1.setObjectName("pause1")
        ui.pause1.setText("PAUSE DOWNLOAD")
        ui.pause1.clicked.connect(pausedownload)

        ui.resume1 = QtWidgets.QPushButton(ui.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        ui.resume1.setFont(font)
        ui.resume1.setObjectName("resume1")
        ui.resume1.setText("RESUME DOWNLOAD")
        ui.resume1.clicked.connect(resumedownload)

        ui.downloaded1 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_2)
        ui.downloaded1.setObjectName("downloaded1")
        #ui.downloaded1.setFont(font)

        ui.TimeTaken1 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_2)
        ui.TimeTaken1.setObjectName("TimeTaken1")
        #ui.TimeTaken1.setFont(font)

        ui.DownloadSpeed1 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_2)
        ui.DownloadSpeed1.setObjectName("DownloadSpeed1")
        #ui.DownloadSpeed1.setFont(font)

        ui.timeremaning1 = QtWidgets.QLabel(ui.scrollAreaWidgetContents_2)
        ui.timeremaning1.setObjectName("timeremaning1")
        #ui.timeremaning1.setFont(font)

        ui.gridLayout_3.addWidget(ui.out_file_location ,  (t*5), 0 , 1, 6)
        ui.gridLayout_3.addWidget(ui.progressBar1, (t * 5)+1, 0, 1, 6)
        ui.gridLayout_3.addWidget(ui.cancel1, (t *5) + 2, 0, 1, 1)
        ui.gridLayout_3.addWidget(ui.pause1, (t * 5) + 2, 1, 1, 1)
        ui.gridLayout_3.addWidget(ui.resume1, (t * 5) + 2, 2, 1, 1)
        ui.gridLayout_3.addWidget(ui.downloaded1, (t * 5) + 2, 3, 1, 3)
        ui.gridLayout_3.addWidget(ui.TimeTaken1, (t * 5) + 3, 0, 1, 2)
        ui.gridLayout_3.addWidget(ui.DownloadSpeed1, (t * 5) + 3, 2, 1, 2)
        ui.gridLayout_3.addWidget(ui.timeremaning1, (t * 5) + 3, 4, 1, 2)


        ui.out_file_location.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        ui.TimeTaken1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        ui.DownloadSpeed1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        ui.timeremaning1.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        ui.out_file_location.setText(str(t+1)+" . FILE LOCATION->{}".format(file_location))
        # ui.downloaded1.setText("DOWNLOADED->")
        # ui.TimeTaken1.setText("time atken")
        # ui.DownloadSpeed1.setText('downlaoda seep')
        # ui.timeremaning1.setText('time remain')
        with open(file_location, 'wb') as f:
            response = requests.get(file_link, allow_redirects=True, stream=True)
            total_length = response.headers.get("content-length")
            start = time.time()
            if total_length is None:
                f.write(response.content)
                ui.progressBar1.setValue(100)
                ui.downloaded1.setText("DOWNLOADED-> 1/1")
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
                    ui.downloaded1.setText("DOWNLOADED->{}MB/{}MB".format(str(dl / (1024 * 1024))[:8],
                                                                            str(total_length / (1024 * 1024))[:8]))
                    # time.sleep(0.1)
                    if time.time() != start:
                        speed = (dl // (time.time() - start))
                        try:
                            remain = (total_length - dl) / (speed)
                            if remain > 60:
                                remain_min = remain // 60
                                remain_sec = remain - (remain_min * 60)
                                ui.timeremaning1.setText(
                                    "TIME REMAIN->{}min{}sec".format(str(remain_min), str(remain_sec)[:2]))
                            else:
                                ui.timeremaning1.setText("TIME REMAIN->{}sec".format(remain[:2]))

                        except:
                            ui.timeremaning1.setText("TIME REMAIN->{}".format('9999999999'))
                        if speed > (1024 * 1024):
                            ui.DownloadSpeed1.setText('DOWNLOAD SPEED->{}MBps'.format(str(speed / (1024 * 1024))[:6]))
                        else:
                            ui.DownloadSpeed1.setText("DOWNLOAD SPEED->{}KBps".format(str(speed / 1024)[:5]))
                    temp = time.time() - start
                    if (temp) > 60:
                        ui.TimeTaken1.setText(
                            "TIME TAKEN->{}min{}sec".format(str(temp // 60), str(temp - temp // 60)[:2]))
                    else:
                        ui.TimeTaken1.setText('TIME TAKEN->{}sec'.format(str(temp)[:2]))
                    ui.progressBar1.setValue(done)
                    QApplication.processEvents()
                ui.progressBar1.setValue(100)
                ui.downloaded1.setText("DOWNLOADED->{}/{}".format(str(total_length), str(total_length)))
        QApplication.processEvents()

