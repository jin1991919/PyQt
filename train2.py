from PyQt5 import QtWidgets
import sys
class PegGameWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setGeometry(200,200,400,200)
        self.setWindowTitle('Triangle Peg Game')
        self.setToolTip("Play the triangle")
        self.central_widget = QtWidgets.QWidget(self)
        self.new_button=StartNewGameBtn(self.central_widget)
        self.quit_button=QuitBtn(self.central_widget)
        self.setCentralWidget(self.central_widget)
        exit_action=QtWidgets.QAction('Exit',self)
        exit_action.triggered.connect(QtWidgets.qApp.quit)
        menu_bar=self.menuBar()
        file_menu=menu_bar.addMenu('File')
        file_menu.addAction(exit_action)
        self.quit_button.clicked.connect(self.closeEvent)
        self.show()
    def closeEvent(self,event):
        reply=QuitMessage().exec_()
        if reply==QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

class QuitMessage(QtWidgets.QMessageBox):
    def __init__(self):
        QtWidgets.QMessageBox.__init__(self)
        self.setText("Do you really want to quit?")
        self.addButton(self.No)
        self.addButton(self.Yes)
class StartNewGameBtn(QtWidgets.QPushButton):
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self,parent)
        self.setText("Start New Game")
        self.move(20,160)
class QuitBtn(QtWidgets.QPushButton):
    def __init__(self,parent):
        QtWidgets.QPushButton.__init__(self,parent)
        self.setText("Quit")
        self.move(150,160)
        self.setToolTip("Close the triangle peg game.")
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    main_window=PegGameWindow()
    app.exec_()
