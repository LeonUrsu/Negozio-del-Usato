import os

from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget, QLineEdit

from Database.PathDatabase import PathDatabase
from MVC.controller.Controller import Controller


class LoginView(QWidget):
    def __init__(self, mainPath):
        super().__init__()
        loader = QUiLoader()
        path = os.path.join(PathDatabase().mainDirPath, "resourcesForUsatoBeato", "UserViews", "LoginView.ui")
        file = QFile(path)
        file.open(QFile.ReadOnly)
        self.finestra = loader.load(file)
        file.close()

    def confermaBtn(self, finestra):
        email = finestra.emailEd.text()
        password = finestra.passwordEd.text()
        return Controller().userLoginController(email, password) # ritorna un Account() o None


    #Metodo che permette di visualizzare la password inserita
    def toggleVisibility(self, login):
        if login.finestra.passwordEd.echoMode() == QLineEdit.Normal:
            login.finestra.passwordEd.setEchoMode(QLineEdit.Password)
        else:
            login.finestra.passwordEd.setEchoMode(QLineEdit.Normal)

