from __future__ import annotations

from PyQt5 import QtCore, QtGui, QtWidgets
from sqlite3.dbapi2 import DatabaseError
import sqlite3
import sys

from app_functions import haversine

ICON = QtWidgets.QMessageBox.Icon
DATABASE_PATH = "places.db"

def load_database(file_name:str = ":memory:"):
    try:
        DBconnection = sqlite3.connect(file_name)
        DBcursor = DBconnection.cursor()
    except DatabaseError:
        print("Invalid filename")
        return None, None
    else:
        print("Unknown error")
        return None, None
    finally:
        return DBconnection, DBcursor

def message_box(
    title, body,
    icon: ICON = ICON.Information
    ):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(body)
        msg_box.setIcon(icon)
        msg_box.show()


class MainWindow(QtWidgets.QMainWindow):
    locations = {}

    def _load_locations(self, filename: str):
        pass




    def on_open_file(self):
        pass

    def on_save_file(self):
        pass

    def on_save_location(self):
        pass

    def on_open_location(self):
        pass

    def on_calculate(self):
        lat_1 = self.lat_1.toPlainText()
        lat_2 = self.lat_2.toPlainText()
        lon_1 = self.lon_1.toPlainText()
        lon_2 = self.lon_2.toPlainText()


        if not all([lat_1, lat_2, lon_1, lon_2]):
            self.output.setText("Error")
            return

        lat_1 = float(lat_1.strip())
        lat_2 = float(lat_2.strip())
        lon_1 = float(lon_1.strip())
        lon_2 = float(lon_2.strip())
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
        
        self.on_calculate()

    def on_lat_1(self):
        lat_1 = self.lat_1.toPlainText()
        print(len(lat_1))
        if len(lat_1) > 9:
            self.lat_1.setText(lat_1[:9])
            self.lat_1.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def on_lon_1(self):
        lon_1 = self.lon_1.toPlainText()
        print(len(lon_1))
        if len(lon_1) > 9:
            self.lon_1.setText(lon_1[:9])
            self.lon_1.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def on_lat_2(self):
        lat_2 = self.lat_2.toPlainText()
        print(len(lat_2))
        if len(lat_2) > 9:
            self.lat_2.setText(lat_2[:9])
            self.lat_2.moveCursor(QtGui.QTextCursor.MoveOperation.End)

    def on_lon_2(self):
        lon_2 = self.lon_2.toPlainText()
        print(len(lon_2))
        if len(lon_2) > 9:
            self.lon_2.setText(lon_2[:9])
            self.lon_2.moveCursor(QtGui.QTextCursor.MoveOperation.End)


    def setup_ui(self):
        self.setObjectName("MainWindow")
        self.resize(550, 350)
        self.lat_1 = QtWidgets.QTextEdit(self)
        self.lat_1.setGeometry(QtCore.QRect(100, 10, 150, 50))
        self.lat_1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lat_1.setFont(font)
        self.lat_1.setObjectName("lat_1")
        self.lon_1 = QtWidgets.QTextEdit(self)
        self.lon_1.setGeometry(QtCore.QRect(100, 70, 150, 50))
        self.lon_1.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lon_1.setFont(font)
        self.lon_1.setObjectName("lon_1")
        self.label_lat_1 = QtWidgets.QLabel(self)
        self.label_lat_1.setGeometry(QtCore.QRect(20, 10, 61, 51))
        self.label_lat_1.setObjectName("label_lat_1")
        self.label_lon_1 = QtWidgets.QLabel(self)
        self.label_lon_1.setGeometry(QtCore.QRect(20, 70, 71, 51))
        self.label_lon_1.setObjectName("label_lon_1")
        self.lon_2 = QtWidgets.QTextEdit(self)
        self.lon_2.setGeometry(QtCore.QRect(350, 70, 150, 50))
        self.lon_2.setMaximumSize(QtCore.QSize(150, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lon_2.setFont(font)
        self.lon_2.setObjectName("lon_2")
        self.label_lon_2 = QtWidgets.QLabel(self)
        self.label_lon_2.setGeometry(QtCore.QRect(270, 70, 71, 51))
        self.label_lon_2.setObjectName("label_lon_2")
        self.label_lat_2 = QtWidgets.QLabel(self)
        self.label_lat_2.setGeometry(QtCore.QRect(270, 10, 61, 51))
        self.label_lat_2.setObjectName("label_lat_2")
        self.lat_2 = QtWidgets.QTextEdit(self)
        self.lat_2.setGeometry(QtCore.QRect(350, 10, 150, 50))
        self.lat_2.setMaximumSize(QtCore.QSize(150, 50))
        self.output = QtWidgets.QTextEdit(self)
        self.output.setGeometry(QtCore.QRect(100, 190, 200, 50))
        self.output.setReadOnly(True)
        self.output.setFont(font)
        self.output.setObjectName("output")
        self.label_output = QtWidgets.QLabel(self)
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
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(100, 130, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)

        self.checkBox.setFont(font)
        self.checkBox.setIconSize(QtCore.QSize(48, 48))
        self.checkBox.setObjectName("checkBox")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(350, 130, 150, 50))
        self.unitButton = QtWidgets.QPushButton(self)
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
        MainWindow.setCentralWidget(self)
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

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslate_ui(self, MainWindow):
        MainWindow.setWindowTitle("MainWindow")
        self.lat_1.setText("")
        self.lon_1.setText("")
        self.label_lat_1.setText("LATITUDE 1")
        self.label_lon_1.setText("LONGITUDE 1")
        self.lat_2.setText("")
        self.lon_2.setText("")
        self.label_lon_2.setText("LONGITUDE 2")
        self.label_lat_2.setText("LATITUDE 2")
        self.label_output.setText("OUTPUT")
        self.checkBox.setText("Radians")
        self.pushButton.setText("Calculate")
        self.unitButton.setText("KM")
        self.menuFile.setTitle("File")

        self.actionOpen.setText("Open")

        self.actionSave.setText("Save")
        self.actionSave.setStatusTip("Update current file")
        self.actionSave.setShortcut(QtGui.QKeySequence("Ctrl+S"))

        self.actionSave_As.setText("Save As")
        self.actionSave_As.setStatusTip("Save File to new Location")
        self.actionSave_As.setShortcut(QtGui.QKeySequence("Ctrl+Shift+S"))

        self.actionClose.setText("Close")
        self.actionClose.setShortcut(QtGui.QKeySequence("Ctrl+W"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    ui = MainWindow()
    ui.show()

    sys.exit(app.exec())
