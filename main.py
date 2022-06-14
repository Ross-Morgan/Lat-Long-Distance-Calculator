from __future__ import annotations

import sys

from PyQt6 import QtCore, QtGui, QtWidgets

from app_functions import haversine


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, size: tuple[int, int],
                 title: str, icon: QtGui.QIcon):
        super().__init__()

        self.setFixedSize(*size)
        self.setWindowTitle(title)
        self.setWindowIcon(icon)

        self.setup_ui()

    def on_calculate(self):
        lat_1 = self.lat_1.toPlainText()
        lat_2 = self.lat_2.toPlainText()
        lon_1 = self.lon_1.toPlainText()
        lon_2 = self.lon_2.toPlainText()


        if not all([lat_1, lat_2, lon_1, lon_2]):
            self.output.setText("----")
            return

        lat_1 = float(lat_1.strip())
        lat_2 = float(lat_2.strip())
        lon_1 = float(lon_1.strip())
        lon_2 = float(lon_2.strip())

        is_radians = self.radian_box.isChecked()
        unit = self.unit_button.text()


        if all([lat_1, lat_2, lon_1, lon_2]):
            distance = haversine(lat_1, lon_1, lat_2, lon_2, is_radians, unit)
            self.output.setText(f"{distance:.3f} {unit}")
        else:
            self.output.setText("Error")

    def on_unit_swap(self, *_): 
        text = self.unit_button.text()

        if text == "KM":
            self.unit_button.setText("MI")

        elif text == "MI":
            self.unit_button.setText("NM")

        elif text == "NM":
            self.unit_button.setText("KM")

        self.on_calculate()

    def on_text_change(self, widget: QtWidgets.QTextEdit, ):
        def inner(*_):
            text = widget.toPlainText()

            if len(text) > 9:
                widget.setText(text[:9])
                widget.moveCursor(QtGui.QTextCursor.MoveOperation.End)

        return inner

    def setup_ui(self):
        font = QtGui.QFont()
        font.setPointSize(20)

        self.lat_1 = QtWidgets.QTextEdit(self)
        self.lat_2 = QtWidgets.QTextEdit(self)
        self.lon_1 = QtWidgets.QTextEdit(self)
        self.lon_2 = QtWidgets.QTextEdit(self)

        self.lat_1.setGeometry(100, 20, 150, 50)
        self.lat_2.setGeometry(350, 20, 150, 50)
        self.lon_1.setGeometry(100, 80, 150, 50)
        self.lon_2.setGeometry(350, 80, 150, 50)

        self.lat_1.setFont(font)
        self.lat_2.setFont(font)
        self.lon_1.setFont(font)
        self.lon_2.setFont(font)

        self.lat_1_label = QtWidgets.QLabel(self)
        self.lat_2_label = QtWidgets.QLabel(self)
        self.lon_1_label = QtWidgets.QLabel(self)
        self.lon_2_label = QtWidgets.QLabel(self)

        self.lat_1_label.setGeometry(20, 20, 61, 51)
        self.lat_2_label.setGeometry(270, 20, 61, 51)
        self.lon_1_label.setGeometry(20, 80, 71, 51)
        self.lon_2_label.setGeometry(270, 80, 71, 51)

        self.output = QtWidgets.QTextEdit(self)
        self.output.setGeometry(100, 200, 232, 50)
        self.output.setReadOnly(True)
        self.output.setFont(font)

        self.output_label = QtWidgets.QLabel(self)
        self.output_label.setGeometry(20, 200, 71, 51)

        self.lat_1.textChanged.connect(self.on_text_change(self.lat_1))
        self.lat_2.textChanged.connect(self.on_text_change(self.lat_2))
        self.lon_1.textChanged.connect(self.on_text_change(self.lon_1))
        self.lon_2.textChanged.connect(self.on_text_change(self.lon_2))

        self.radian_box = QtWidgets.QCheckBox(self)
        self.radian_box.setGeometry(100, 140, 150, 50)
        self.radian_box.setFont(font)
        self.radian_box.setIconSize(QtCore.QSize(48, 48))

        self.push_button = QtWidgets.QPushButton(self)
        self.push_button.setGeometry(350, 140, 150, 50)

        self.unit_button = QtWidgets.QPushButton(self)
        self.unit_button.setGeometry(258, 140, 75, 50)
        self.unit_button.clicked.connect(self.on_unit_swap)

        self.push_button.setFont(font)
        self.push_button.setCheckable(False)
        self.push_button.clicked.connect(self.on_calculate)

        self.retranslate_ui()

    def retranslate_ui(self):
        self.lat_1_label.setText("LATITUDE 1")
        self.lon_1_label.setText("LONGITUDE 1")
        self.lon_2_label.setText("LONGITUDE 2")
        self.lat_2_label.setText("LATITUDE 2")

        self.output_label.setText("OUTPUT")
        self.output.setText("----")

        self.radian_box.setText("Radians")
        self.push_button.setText("Calculate")
        self.unit_button.setText("KM")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    size = 520, 270
    title = "Lat-Long Distance Calculator"
    icon = QtGui.QIcon()

    ui = MainWindow(size, title, icon)
    ui.show()

    app.exec()
