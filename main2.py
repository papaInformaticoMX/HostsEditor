import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout
from HostsEditorLogic import HostsEditorLogic

class HostsEditor(QWidget):
    def __init__(self, logic):
        super().__init__()
        self.logic = logic
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Editor de archivo Hosts')

        self.textEdit = QTextEdit(self)
        self.textEdit.setText(self.logic.load_file())

        self.saveBtn = QPushButton('Guardar cambios', self)
        self.saveBtn.clicked.connect(self.save_changes)

        self.cancelBtn = QPushButton('Cancelar', self)
        self.cancelBtn.clicked.connect(self.cancel_changes)

        self.restoreBtn = QPushButton('Restaurar original', self)
        self.restoreBtn.clicked.connect(self.restore_original)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.saveBtn)
        buttonLayout.addWidget(self.cancelBtn)
        buttonLayout.addWidget(self.restoreBtn)

        topLayout = QVBoxLayout()
        topLayout.addLayout(buttonLayout)
        topLayout.addWidget(self.textEdit)

        layout = QVBoxLayout()
        layout.addLayout(topLayout)

        self.setLayout(layout)

    def save_changes(self):
        self.logic.write_file(self.textEdit.toPlainText())
        self.close()

    def cancel_changes(self):
        self.close()

    def restore_original(self):
        self.textEdit.setText(self.logic.restore_original())

if __name__ == '__main__':
    config_path = 'config.txt'
    logic = HostsEditorLogic(config_path)
    app = QApplication(sys.argv)
    ex = HostsEditor(logic)
    ex.showMaximized()
    sys.exit(app.exec_())
