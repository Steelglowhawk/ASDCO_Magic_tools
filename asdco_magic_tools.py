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
                             QMessageBox, QCheckBox, QButtonGroup)
from PyQt6.QtGui import QIcon, QColor


class Worker(QRunnable):  # класс для мультипоточности???
    def run(self):  # мой код
        pass


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        # Переменные
        self.checked_check = []
        # Добавляем файл с настройками
        self.settings = QSettings('settings.ini', QSettings.Format.IniFormat)
        self.setWindowTitle("Magic Trick")  # заголовок главного окна
        self.setMinimumSize(500, 150)  # минимальные размеры главного окна
        self.button_1 = QPushButton('Make a magic', self)
        self.table = QTableWidget()
        self.label_1 = QLabel()
        self.check_1 = QCheckBox('Check 1')
        self.check_2 = QCheckBox('Check 2')
        self.check_3 = QCheckBox('Check 3')
        self.check_4 = QCheckBox('Check 4')
        self.check_5 = QCheckBox('Check 5')

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.table)
        main_layout.addWidget(self.label_1)
        main_layout.addWidget(self.button_1)

        main_layout.addWidget(self.check_1)
        main_layout.addWidget(self.check_2)
        main_layout.addWidget(self.check_3)
        main_layout.addWidget(self.check_4)
        main_layout.addWidget(self.check_5)

        self.check_group = QButtonGroup()
        self.check_group.setExclusive(False)
        self.check_group.addButton(self.check_1, id=1)
        self.check_group.addButton(self.check_2, id=2)
        self.check_group.addButton(self.check_3, id=3)
        self.check_group.addButton(self.check_4, id=4)
        self.check_group.addButton(self.check_5, id=5)

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
        self.check_group.buttonToggled.connect(self.work_with_list_of_checked_checkbox)
        self.button_1.clicked.connect(self.show_checked_checkbox)

    def print_selected_cell(self):
        items = self.table.selectedItems()  # список выделенных элементов
        for i in items:
            print(i.text())
            print(self.table.row(i))  # выводит индекс строки для выделенной ячейки
        # print(str(items[0].text()))
            self.label_1.setText(i.text())

    def work_with_list_of_checked_checkbox(self):
        if self.check_group.checkedId() in self.checked_check:  # надо понять как удалить id из списка если снят чекбокс
            pass
        else:
            self.checked_check.append(self.check_group.checkedId())
        print(self.check_group.checkedId())

    def show_checked_checkbox(self):
        # print(self.check_group.buttons())
        # print(self.check_group.exclusive())
        print(self.checked_check)
        print(self.check_group.checkedButton())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
