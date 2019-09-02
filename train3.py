from PyQt5 import QtWidgets
import sys
class Mainwindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('This is my first app')
        self.setGeometry(200,200,400,200)
        self.central_widget=QtWidgets.QWidget(self)
        menubar=self.menuBar()
        exit_Action = QtWidgets.QAction('Exit', self)
        exit_Action.triggered.connect(QtWidgets.qApp.quit)
        file_menu=menubar.addMenu('File')
        file_menu.addAction(exit_Action)
        self.setCentralWidget(self.central_widget)
        self.show()
if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    main_window=Mainwindow()
    app.exec_()
