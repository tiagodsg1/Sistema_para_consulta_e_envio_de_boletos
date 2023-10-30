import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from Front_End.ui.Main_Window import Ui_UpHouse
from Front_End.page_functions.Home import Home
from tkinter import messagebox

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_UpHouse()
        self.ui.setupUi(self)
        
        self.home_bnt = self.ui.home_button

        self.menu_btns_dict = {
            self.home_bnt: Home
        }

        self.show_home_window()

    def show_home_window(self):
        result = self.open_tab_flag(self.home_bnt)
        self.set_bnt_checked(self.home_bnt)

        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = self.home_bnt.text()
            curIndex = self.ui.tabWidget.addTab(Home(), tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def set_bnt_checked(self, btn):
        for button in self.menu_btns_dict.keys():
            if button == btn:
                button.setChecked(False)
            else:
                button.setChecked(True)

    def show_selected_window(self):
        button = self.sender()
        result = self.open_tab_flag(button.text())
        self.set_bnt_checked(button)
        if result[0]:
            self.ui.tabWidget.setCurrentIndex(result[1])
        else:
            tab_title = button.text()
            curIndex = self.ui.tabWidget.addTab(self.menu_btns_dict[button](), tab_title)
            self.ui.tabWidget.setCurrentIndex(curIndex)
            self.ui.tabWidget.setVisible(True)

    def open_tab_flag(self, btn_text):
        open_tab_count = self.ui.tabWidget.count()
        for i in range(open_tab_count):
            tab_title = self.ui.tabWidget.tabText(i)
            if tab_title == btn_text:
                return True, i
            else:
                continue
        return False, None
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
