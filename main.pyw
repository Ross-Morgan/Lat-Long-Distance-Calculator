from PyQt5 import QtCore, QtGui, QtWidgets

from app_functions import haversine


class Ui_MainWindow(object):
    def on_calculate(self):

        lat_1 = float(self.lat_1.toPlainText().strip())
        lat_2 = float(self.lat_2.toPlainText().strip())
        lon_1 = float(self.lon_1.toPlainText().strip())
        lon_2 = float(self.lon_2.toPlainText().strip())
        is_radians = self.checkBox.isChecked()
        unit = self.unitButton.text()
        if lat_1 and lat_2 and lon_1 and lon_2:
            distance = haversine(lat_1, lon_1, lat_2, lon_2, is_radians, unit)
            self.output.setText(f"{distance:.3f} {unit}")
        else:
            self.output.setText("Error")

    
    def on_unit_swap(self):
        text = self.unitButton.text()

        if text == "KM":
            self.unitButton.setText("MI")

        elif text == "MI":
            self.unitButton.setText("NM")

        elif text == "NM":
            self.unitButton.setText("KM")

    def on_lat_1(self):
        lat_1 = self.lat_1.toPlainText().strip()
        if len(lat_1) > 9:
            self.lat_1.setText(lat_1[:9])
            self.lat_1.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def on_lon_1(self):
        lon_1 = self.lon_1.toPlainText().strip()
        if len(lon_1) > 9:
            self.lon_1.setText(lon_1[:9])
            self.lon_1.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def on_lat_2(self):
        lat_2 = self.lat_2.toPlainText().strip()
        if len(lat_2) > 9:
            self.lat_2.setText(lat_2[:9])
            self.lat_2.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def on_lon_2(self):
        lon_2 = self.lon_2.toPlainText().strip()
        if len(lon_2) > 9:
            self.lon_2.setText(lon_2[:9])
            self.lon_2.moveCursor(QtGui.QTextCursor.MoveOperation.End)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lat_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.lat_1.setGeometry(QtCore.QRect(100, 10, 150, 50))
        self.lat_1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lat_1.setFont(font)
        self.lat_1.setObjectName("lat_1")
        self.lon_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.lon_1.setGeometry(QtCore.QRect(100, 70, 150, 50))
        self.lon_1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lon_1.setFont(font)
        self.lon_1.setObjectName("lon_1")
        self.label_lat_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_lat_1.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.label_lat_1.setObjectName("label_lat_1")
        self.label_lon_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_lon_1.setGeometry(QtCore.QRect(20, 70, 71, 51))
        self.label_lon_1.setObjectName("label_lon_1")
        self.lon_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.lon_2.setGeometry(QtCore.QRect(350, 70, 150, 50))
        self.lon_2.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lon_2.setFont(font)
        self.lon_2.setObjectName("lon_2")
        self.label_lon_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_lon_2.setGeometry(QtCore.QRect(270, 70, 71, 51))
        self.label_lon_2.setObjectName("label_lon_2")
        self.label_lat_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_lat_2.setGeometry(QtCore.QRect(270, 10, 61, 51))
        self.label_lat_2.setObjectName("label_lat_2")
        self.lat_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.lat_2.setGeometry(QtCore.QRect(350, 10, 150, 50))
        self.lat_2.setMaximumSize(QtCore.QSize(150, 50))
        self.output = QtWidgets.QTextEdit(self.centralwidget)
        self.output.setGeometry(QtCore.QRect(100, 190, 200, 50))
        self.output.setReadOnly(True)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(20, 190, 71, 51))
        self.label_output.setObjectName("label_output")

        self.lat_1.textChanged.connect(self.on_lat_1)
        self.lat_2.textChanged.connect(self.on_lat_2)

        self.lon_1.textChanged.connect(self.on_lon_1)
        self.lon_2.textChanged.connect(self.on_lon_2)


        font = QtGui.QFont()
        font.setPointSize(20)
        self.lat_2.setFont(font)
        self.lat_2.setObjectName("lat_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(100, 130, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(48, 48))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 130, 150, 50))
        self.unitButton = QtWidgets.QPushButton(self.centralwidget)
        self.unitButton.setGeometry(QtCore.QRect(258, 130, 75, 50))
        self.unitButton.clicked.connect(self.on_unit_swap)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)

        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_calculate)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lat_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.lon_1.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_lat_1.setText(_translate("MainWindow", "LATITUDE 1"))
        self.label_lon_1.setText(_translate("MainWindow", "LONGITUDE 1"))
        self.lon_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_lon_2.setText(_translate("MainWindow", "LONGITUDE 2"))
        self.label_lat_2.setText(_translate("MainWindow", "LATITUDE 2"))
        self.lat_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_output.setText(_translate("MainWindow", "OUTPUT"))
        self.checkBox.setText(_translate("MainWindow", " Radians"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.unitButton.setText(_translate("MainWindow", "KM"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Update current file"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSave_As.setStatusTip(_translate("MainWindow", "Save File to new Location"))
        self.actionSave_As.setShortcut(_translate("MainWindow", "Ctrl+Shift+S"))
        self.actionClose.setText(_translate("MainWindow", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
