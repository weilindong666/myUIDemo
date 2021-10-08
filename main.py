# --coding:utf-8--
'''
@File: main.py
@Author:魏林栋（welindong）
@Time: 2021年10月03日  16:55
'''
from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile, Qt
from PySide2.QtGui import QIcon


class MainPage(object):
    def __init__(self):
        qfile_stats = QFile('ui/learnUI.ui')
        qfile_stats.open(QFile.ReadOnly)
        qfile_stats.close()

        self.ui = QUiLoader().load(qfile_stats)
        self.ui.pushButton_1.clicked.connect(self.lastOne)
        self.ui.pushButton_2.clicked.connect(self.again)
        self.ui.pushButton_3.clicked.connect(self.nextOne)


    def lastOne(self):
        self.setWordText('Good Morning')
        self.setTransText('早上好！')

    def setWordText(self, word):
        self.ui.label_1.setText(word)
        self.ui.label_1.setAlignment(Qt.AlignCenter)

    def setTransText(self, info):
        self.ui.label_2.setText(info)
        self.ui.label_2.setAlignment(Qt.AlignCenter)


    def nextOne(self):
        self.setWordText('computer')
        self.setTransText('电脑')


    def again(self):
        pass



if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon('111.png'))
    stats = MainPage()
    stats.ui.show()
    app.exec_()