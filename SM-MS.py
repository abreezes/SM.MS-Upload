# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests
import json

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        # 大小
        Form.resize(360, 390)

        # 按钮1
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")

        # 按钮2
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 340, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")

        # 结果显示
        self.plainTextEdit = QtWidgets.QTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(40, 60, 271, 271))
        self.plainTextEdit.setObjectName("plainTextEdit")

        # 结果
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 54, 12))
        self.label.setObjectName("label")

        # 提示信息
        self.label_1=QtWidgets.QLabel(Form)
        self.label_1.setGeometry(QtCore.QRect(110, 20, 190, 16))
        self.label_1.setObjectName("label")

        self.timer = QtCore.QTimer()

        # 调用retranslateUI
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "SM.MS图床上传助手"))
        self.label_1.setText(_translate("Form", "请勿上传违规违法图片"))
        self.pushButton.setText(_translate("Form", "浏览并上传"))
        self.pushButton_3.setText(_translate("Form", "CopyURL"))
        self.label.setText(_translate("Form", "结果"))

        # 信号
        self.pushButton.clicked.connect(self.openfiles)
        self.pushButton_3.clicked.connect(self.copyURL)

    def openfiles(self):
        # 打开文件
        try:
            file_name, file_type = QFileDialog.getOpenFileName(self,"选取文件",'',
                                                            r"All Files (*);;Image files(*.PNG *.JPEG *.JPG *.GIF)")
            # 上传文件
            self.upload(file_name)
        except Exception:
            pass

    def upload(self,file_name=None):
        # 上传文件
        global response
        url = "https://sm.ms/api/upload"
        name=file_name[file_name.rindex('/')+1:]
        files = {'smfile': ("%s" % name, open(r'%s'%file_name, 'rb'), 'image/png')}
        response=requests.post(url=url,data={'ssl':1},files=files).json()
        self.plainTextEdit.setText(json.dumps(response,separators=(',\n',':')))

    def copyURL(self):
        # 复制URl
        try:
            if response != None:
                url=response.get('data').get('url')

            else:
                url=''
            clipboard = QApplication.clipboard()
            clipboard.setText('![](%s)' %url)
        except Exception:
            pass





class MyImages(QtWidgets.QWidget,Ui_Form):
    def __init__(self):
        super(MyImages,self).__init__()
        self.setupUi(self)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyImages()
    myshow.show()
    sys.exit(app.exec_())

