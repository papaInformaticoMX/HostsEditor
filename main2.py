import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout

class HostsEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Editor de archivo Hosts')

        self.textEdit = QTextEdit(self)
        self.textEdit.setVerticalScrollBarPolicy(1) # agregar barra de desplazamiento vertical siempre
        self.textEdit.setSizePolicy(1, 1) # establecer la política de expansión para ocupar todo el espacio vertical disponible

        self.saveBtn = QPushButton('Guardar cambios', self)
        self.saveBtn.clicked.connect(self.saveChanges)

        self.cancelBtn = QPushButton('Cancelar', self)
        self.cancelBtn.clicked.connect(self.cancelChanges)

        self.restoreBtn = QPushButton('Restaurar original', self)
        self.restoreBtn.clicked.connect(self.restoreOriginal)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.saveBtn)
        buttonLayout.addWidget(self.cancelBtn)
        buttonLayout.addWidget(self.restoreBtn)

        layout = QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addLayout(buttonLayout)

        self.setLayout(layout)
        self.loadFile()

    def loadFile(self):
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'r') as file:
            self.textEdit.setText(file.read())

    def saveChanges(self):
        with open('C:\\Windows\\System32\\drivers\\etc\\hosts', 'w') as file:
            file.write(self.textEdit.toPlainText())

    def cancelChanges(self):
        self.close()

    def restoreOriginal(self):
        self.loadFile()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = HostsEditor()
    ex.showMaximized()
    sys.exit(app.exec_())
