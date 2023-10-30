from PyQt5.QtWidgets import QWidget
from Front_End.ui.pages.Home.Home import Ui_Form

class Home(QWidget):
    def __init__(self):
        super(Home,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        