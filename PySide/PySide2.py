#  PySide2 - Python bindings for the Qt cross-platform application and UI framework

# PyPi: https://pypi.org/project/PySide2/
# Docs: https://wiki.qt.io/Qt_for_Python
# Quick start: https://doc.qt.io/qtforpython-5/quickstart.html

# pip install PySide2
#  For the latest version on PyPi
# pip install PySide2
# For a specific version
# pip install PySide2==5.15.0

# Requirements:
# Python  3.5+
# Recommend using a virtual environment, such as venv or virtualenv
"""
$ python -m venv env/       # Your binary is maybe called 'python3'
$ source env/bin/activate   # for Linux and macOS
$ env\Scripts\activate.bat  # for Windows
"""

# Test Installation:
# To print version information:

import PySide2.QtCore

# Prints PySide2 version
print(PySide2.__version__)

# Prints the Qt version used to compile PySide2
print(PySide2.QtCore.__version__)


#  Create a Simple Application

# Create a new file named app.py

import sys
import random
from PySide2 import QtCore, QtWidgets, QtGui


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
    
    
# Example 2
import sys
from main import Ui_Dialog
from PySide2 import QtCore, QtGui, QtWidgets


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


#  Example 3
import sys
from main import Ui_Dialog
from PySide2 import QtCore, QtGui, QtWidgets


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # here code ...
    self.textEdit.setPlainText("Some text")

    self.pushButton.clicked.connect(self.onClicked)
    self.pushButton_2.clicked.connect(self.onClicked)
    self.pushButton_3.clicked.connect(self.onClicked)
        
        
    def onClicked(self):
        sender = self.sender()
        self.textEdit.setPlainText(sender.text())

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())
    
    
# How to delete widget 
self.next_btn.hide()
self.next_btn.deleteLater()

