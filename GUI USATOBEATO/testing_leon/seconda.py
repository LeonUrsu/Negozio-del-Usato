# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'seconda.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_prima(object):
    def setupUi(self, prima):
        prima.setObjectName("prima")
        prima.resize(400, 300)
        self.gototerbtn = QtWidgets.QPushButton(prima)
        self.gototerbtn.setGeometry(QtCore.QRect(150, 130, 93, 28))
        self.gototerbtn.setObjectName("gototerbtn")
        self.gotopribtn = QtWidgets.QPushButton(prima)
        self.gotopribtn.setGeometry(QtCore.QRect(150, 170, 93, 28))
        self.gotopribtn.setObjectName("gotopribtn")
        self.label = QtWidgets.QLabel(prima)
        self.label.setGeometry(QtCore.QRect(150, 90, 55, 16))
        self.label.setObjectName("label")

        self.retranslateUi(prima)
        QtCore.QMetaObject.connectSlotsByName(prima)

    def retranslateUi(self, prima):
        _translate = QtCore.QCoreApplication.translate
        prima.setWindowTitle(_translate("prima", "Form"))
        self.gototerbtn.setText(_translate("prima", "terza"))
        self.gotopribtn.setText(_translate("prima", "prima"))
        self.label.setText(_translate("prima", "seconda"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    prima = QtWidgets.QWidget()
    ui = Ui_prima()
    ui.setupUi(prima)
    prima.show()
    sys.exit(app.exec_())
