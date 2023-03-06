from widgets.login import *
from widgets.regist import *
from PyQt6.QtWidgets import *
from widgets.about import *
from widgets.menu import SignSignal
from widgets.curs import *
from widgets.signal import*
from widgets.feedback import *
from widgets.pay import *
from widgets.menu import *
import sys
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # regWn.show()
    ui = Ui_regist()
    regMainWindow = QtWidgets.QMainWindow()
    ui.setupUic(regMainWindow)
    
    rg=Ui_login()
    logMainWindow = QtWidgets.QMainWindow()
    rg.setupUi(logMainWindow)

    rg.s_up.sign_up_signal.connect(regMainWindow.show)
    ui.back.back_signal.connect(logMainWindow.show)
    cr=Ui_curswindow()
    cur=QtWidgets.QMainWindow()
    cr.setupUicur(cur)
    menu=Ui_MenuWindow()
    sig=SignSignal()
    men=QtWidgets.QMainWindow()
    menu.setupUimenu(men)
    fikr=Ui_feedWindow()
    
    fik=QtWidgets.QMainWindow()
    fikr.setupUifikr(fik)

    about=Ui_aboutWindow()
    abt=QtWidgets.QMainWindow()
    about.setupUiabout(abt)
    rg.kirish_sig.kirish_signal.connect(men.show)

    ui.s_up.sign_up_signal.connect(men.show)
    
    pay=Ui_payWindow()
    py=QtWidgets.QMainWindow()
    pay.setupUipay(py)

    menu.s_up.sign_up_signal.connect(cur.show)
    menu.fikr_signal.fikr_up.connect(fik.show)
    menu.about_up.about_signal.connect(abt.show)
    cr.cur_up.curbuy_signal.connect(py.show)
    cr.back_up.back_signal.connect(men.show)
    logMainWindow.show()
    app.exec()


# import sys
# from PyQt6.QtWidgets import QApplication

# from registratsiya import Ui_MainWindow
# from singing import Ui_singing
# from asosiy import Ui_asosiy
# from test import Ui_Iphone
# from samsung import Ui_samsung

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window1 = Ui_MainWindow()
#     window1.show()

#     window2 = Ui_singing()
#     window3 = Ui_asosiy()
#     window4 = Ui_Iphone()
#     window5 = Ui_samsung()
#     window1.signal.singing.connect(window2.show)
#     window1.signal.asosiy.connect(window3.show)
#     window2.signal.asosiy.connect(window3.show)
#     window4.signal.asosiy.connect(window3.show)
#     window5.signal.asosiy.connect(window3.show)
#     window3.signal.test.connect(window4.show)
#     window3.signal.samsung.connect(window5.show)


















    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_login()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec())