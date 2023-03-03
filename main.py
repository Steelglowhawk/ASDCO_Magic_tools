import sys
import pathlib

from datetime import datetime

from PyQt6.QtCore import QRunnable, QThreadPool, QDateTime, QSettings
from PyQt6.QtWidgets import (QApplication,
                             QLabel,
                             QMainWindow,
                             QPushButton,
                             QWidget,
                             QFileDialog,
                             QGridLayout,
                             QVBoxLayout,
                             QLineEdit,
                             QComboBox,
                             QProgressBar,
                             QStatusBar,
                             QSpinBox,
                             QTableWidget,
                             QTableWidgetItem,
                             QMessageBox)
from PyQt6.QtGui import QIcon, QColor


class Worker(QRunnable):  # класс для мультипоточности???
    def run(self):  # мой код
        pass


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # Добавляем файл с настройками
        self.settings = QSettings('settings.ini', QSettings.Format.IniFormat)
        self.setWindowTitle("Magic Trick")  # заголовок главного окна
        self.setMinimumSize(500, 150)  # минимальные размеры главного окна
        self.button_1 = QPushButton('Make a magic', self)
        self.table = QTableWidget()
        self.label_1 = QLabel()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.button_1)
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.label_1)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
        cell_1 = QTableWidgetItem('Cell_A1')
        cell_2 = QTableWidgetItem('Cell_A2')
        cell_3 = QTableWidgetItem('Cell_A3')
        cell_4 = QTableWidgetItem('Cell_B1')
        cell_5 = QTableWidgetItem('Cell_B2')
        cell_6 = QTableWidgetItem('Cell_B3')
        self.table.setRowCount(3)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['First', 'Second', 'Third', 'Forth'])
        self.table.setItem(0, 0, cell_1)
        self.table.setItem(0, 1, cell_2)
        self.table.setItem(0, 2, cell_3)
        self.table.setItem(1, 0, cell_4)
        self.table.setItem(1, 1, cell_5)
        self.table.setItem(1, 2, cell_6)
        # self.table.show()
        self.label_1.setText('Label')
        self.table.itemSelectionChanged.connect(self.print_selected_cell)  # событие изменения выбора в таблице
        # self.table.cellEntered.connect(self.print_selected_cell)

    def print_selected_cell(self):
        items = self.table.selectedItems()  # список выделенных элементов
        for i in items:
            print(i.text())
            print(self.table.row(i))  # выводит индекс строки для выделенной ячейки
        # print(str(items[0].text()))
            self.label_1.setText(i.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
