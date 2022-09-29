import sys

import PySide2
from Custom_Widgets.Widgets import *
from ui_interface_vuota import *
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtWidgets
from PySide2 import *




class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.mainpage = Ui_MainWindow()
        self.mainpage.setupUi(self)

        self.mainpage.homeBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.home))
        self.mainpage.homeBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.homeBtn.objectName()))


        self.mainpage.prodottiBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.prodotti))
        self.mainpage.prodottiBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.prodottiBtn.objectName()))


        self.mainpage.statisticBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.prodotti))
        self.mainpage.prodottiBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.prodottiBtn.objectName()))


        self.mainpage.accountBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.accounts))
        self.mainpage.accountBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.accountBtn.objectName()))


        self.mainpage.statisticBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.statistiche))
        self.mainpage.statisticBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.statisticBtn.objectName()))


        self.mainpage.loginBtn.clicked.connect(
                lambda: self.mainpage.finestreSecondarie.setCurrentWidget(self.mainpage.login))
        self.mainpage.loginBtn.clicked.connect(lambda: self.changeStyleSheet(self.mainpage.loginBtn.objectName()))


        self.loadData()

        # APPLY JSON STYLESHEET
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.mainpage)
        ########################################################################

        self.show()

    def changeStyleSheet(self,bottone):
        self.mainpage.leftMenu.setStyleSheet(f"#{bottone}"
                                             "\n{"
"background-color:#1a1f39;\n"
"padding : 10px 5px;\n"
"text-align:left;\n"
"border-top-left-radius:25px;\n}\nQPushButton\n{\nbackground-color:#2a2c49;\n"
"border = 0px;\n"
"	padding : 10px 5px;\n"
"	text-align:left;\n"
"	color:#78799c;\n}")

    def loadData(self):
        lista = list()
        row = 0
        for x in range(100):
            dati = {"Nome":"nome"+x.__str__() ,"ID": x.__str__(), "Data": x.__str__(), "Prezzo": x.__str__()}
            lista.append(dati)


        for prodotto in lista:
            self.mainpage.tableWidget.insertRow(0)
            self.mainpage.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(prodotto["Prezzo"]))
            self.mainpage.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(prodotto["ID"]))
            self.mainpage.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(prodotto["Nome"]))
            self.mainpage.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(prodotto["Data"]))
            row = row + 1


# esegui app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
    #end



class Prodotto():

    def __init__(self):
        pass

    def aggiungiProdotto(self, idCategoria, dataEsposizione, idAccount, idProdotto, nomeProdotto,
                         prezzoOriginale, idScaffale):
        self.idCategoria = idCategoria
        self.dataEsposizione = dataEsposizione
        self.idAccount = idAccount
        self.idProdotto = idProdotto
        self.nomeProdotto = nomeProdotto
        self.prezzoCorrente = prezzoOriginale
        self.prezzoOriginale = prezzoOriginale
        self.idScaffale = idScaffale



