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


class Ui_t210(object):
    def setupUi(self, t210):
        self.verticalLayout = QtWidgets.QVBoxLayout(t210)
        self.image_label = QtWidgets.QLabel("Ui_t210", t210)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t210)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t216(object):
    def setupUi(self, t216):
        self.verticalLayout = QtWidgets.QVBoxLayout(t216)
        self.image_label = QtWidgets.QLabel("Ui_t216", t216)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t216)
        self.verticalLayout.addWidget(self.control_bt)

        
class Ui_t82(object):
    def setupUi(self, t82):
        self.verticalLayout = QtWidgets.QVBoxLayout(t82)
        self.image_label = QtWidgets.QLabel("Ui_t82", t82)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t82)
        self.verticalLayout.addWidget(self.control_bt)
        

class Ui_t810(object):
    def setupUi(self, t810):
        self.verticalLayout = QtWidgets.QVBoxLayout(t810)
        self.image_label = QtWidgets.QLabel("Ui_t810", t810)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t810)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t816(object):
    def setupUi(self, t816):
        self.verticalLayout = QtWidgets.QVBoxLayout(t816)
        self.image_label = QtWidgets.QLabel("Ui_t816", t816)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t816)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t102(object):
    def setupUi(self, t102):
        self.verticalLayout = QtWidgets.QVBoxLayout(t102)
        self.image_label = QtWidgets.QLabel("Ui_t102", t102)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t102)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t108(object):
    def setupUi(self, t108):
        self.verticalLayout = QtWidgets.QVBoxLayout(t108)
        self.image_label = QtWidgets.QLabel("Ui_t108", t108)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t108)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t1016(object):
    def setupUi(self, t1016):
        self.verticalLayout = QtWidgets.QVBoxLayout(t1016)
        self.image_label = QtWidgets.QLabel("Ui_t1016", t1016)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t1016)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t162(object):
    def setupUi(self, t162):
        self.verticalLayout = QtWidgets.QVBoxLayout(t162)
        self.image_label = QtWidgets.QLabel("Ui_t162", t162)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t162)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t168(object):
    def setupUi(self, t168):
        self.verticalLayout = QtWidgets.QVBoxLayout(t168)
        self.image_label = QtWidgets.QLabel("Ui_t168", t168)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t168)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Ui_t1610(object):
    def setupUi(self, t1610):
        self.verticalLayout = QtWidgets.QVBoxLayout(t1610)
        self.image_label = QtWidgets.QLabel("Ui_t1610", t1610)
        self.verticalLayout.addWidget(self.image_label)
        self.control_bt = QtWidgets.QPushButton("Next", t1610)
        self.verticalLayout.addWidget(self.control_bt)
        
        
class Main(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.tasks = [
            't28', 't210', 't216', 
            't82', 't810', 't816', 
            't102', 't108', 't1016', 
            't162', 't128', 't1610'
        ]        
        self.uis = [
            Ui_t28(), Ui_t210(), Ui_t216(), 
            Ui_t82(), Ui_t810(), Ui_t816(), 
            Ui_t102(), Ui_t108(), Ui_t1016(), 
            Ui_t162(), Ui_t168(), Ui_t1610()
        ]
        
        self.pushButton_13 = QtWidgets.QPushButton("pushButton_13", self)
        self.pushButton_13.clicked.connect(self.bPall)
        
    def bPnextTask(self, _task):
        while 1:
            task = random.randint(0, 11)
            if task != _task: break
                
        self.tasks[task] = QtWidgets.QWidget()
        widget = self.tasks[task]               
        widget.setWindowTitle(str(task)*10)
        widget.resize(300, 200)
        ui = self.uis[task]                    
        ui.setupUi(widget)
        widget.move(0+(50*task), 0+(35*task))
        widget.show()
        ui.control_bt.clicked.connect(lambda ch, _task=task: self.bPnextTask(_task))
        
        
    def bPall(self):
        task = random.randint(0, 11)
        self.tasks[task] = QtWidgets.QWidget()
        widget = self.tasks[task]             
        widget.setWindowTitle(str(task)*10)
        widget.resize(300, 200)
        ui = self.uis[task]                  
        ui.setupUi(widget)
        widget.move(0+(50*task), 0+(35*task))
        widget.show()
        ui.control_bt.clicked.connect(lambda ch, _task=task: self.bPnextTask(_task))
        

    def closeEvent(self, event):
        for w in self.tasks:
            if isinstance(w, QtWidgets.QWidget):
                w.close()

                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Main()
    ex.setGeometry(900, 200, 150, 100)
    ex.show()
    sys.exit(app.exec_())
