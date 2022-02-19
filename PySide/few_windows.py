import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_t28(object):
    def setupUi(self, t28):
        self.verticalLayout = QtWidgets.QVBoxLayout(t28)
        self.image_label = QtWidgets.QLabel("Ui_t28", t28)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t28)
        self.verticalLayout.addWidget(self.control_bt)

