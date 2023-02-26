import ctypes
import sys

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QHBoxLayout, QVBoxLayout
from HostsEditorLogic import HostsEditorLogic
from main2 import HostsEditor;

def run_as_admin():
    """
    Reinicia el script con permisos elevados de administrador.
    """
    if ctypes.windll.shell32.IsUserAnAdmin():
        # Si ya se están ejecutando con permisos de administrador, no hacer nada.
        return

    # Reinicia el script con permisos elevados de administrador.
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

if __name__ == '__main__':
    run_as_admin()
    config_path = 'config.txt'
    logic = HostsEditorLogic(config_path)
    app = QApplication(sys.argv)
    ex = HostsEditor(logic)
    ex.showMaximized()
    sys.exit(app.exec_())

    # El código que requiere permisos elevados de administrador debe ir aquí.
