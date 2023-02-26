import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon

class HostsEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Editor de archivo Hosts')

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(['URL', 'Comentario'])

        self.addRow('127.0.0.1', 'localhost')
        self.addRow('0.0.0.0', 'example.com')

        self.addBtn = QPushButton('Agregar URL')
        self.addBtn.clicked.connect(self.addRow)

        self.saveBtn = QPushButton('Guardar cambios')
        self.saveBtn.clicked.connect(self.saveChanges)

        hbox = QHBoxLayout()
        hbox.addWidget(self.addBtn)
        hbox.addWidget(self.saveBtn)

        vbox = QVBoxLayout()
        vbox.addWidget(self.table)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def addRow(self, url=None, comment=None):
        rowPosition = self.table.rowCount()
        self.table.insertRow(rowPosition)

        urlItem = QTableWidgetItem(url)
        commentItem = QTableWidgetItem(comment)

        self.table.setItem(rowPosition, 0, urlItem)
        self.table.setItem(rowPosition, 1, commentItem)

    def saveChanges(self):
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'w') as file:
            for row in range(self.table.rowCount()):
                url = self.table.item(row, 0).text()
                comment = self.table.item(row, 1).text()
                isChecked = self.table.item(row, 2).checkState() == 2
                file.write(f'{url} #{comment}' if isChecked else url)
                file.write('\n')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HostsEditor()
    ex.show()
    sys.exit(app.exec_())
