import sys
from datetime import datetime
from dateutil.relativedelta import relativedelta
from Database.PathDatabase import PathDatabase
from MVC.model.Attività.Account import Account
from MVC.model.Interfacce.sistemServiceInterface.FiltriInterface import FiltriInterface
from MVC.model.Servizio.Categoria import Categoria
from MVC.model.Servizio.Prodotto import Prodotto
from MVC.model.SistemService.File import File


class Filtri(FiltriInterface):

    # Costruttore della classe
    def __init__(self):
        self.filtrati = None

    # Metodo di filtraggio dei prodotti in base all prezzo
    # prezzoMin = prezzo minimo di filtraggio
    # prezzoMax = prezzo massimo di filtraggio
    def filtraPrezzo(self, prezzoMin, prezzoMax, fileName):
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if prezzoMin <= int(prodotto.prezzoCorrente) and int(prodotto.prezzoCorrente) <= prezzoMax:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList

    # Metodo di filtraggio dei prodotti in base alla data di esposione
    # dataInizio = data di inizio filtraggio
    # dataFine = data di fine filtraggio
    def filtraDataEsposizione(self, dataInizio, dataFine, fileName):
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = list()
        for prodotto in prodottiList:
            if dataInizio <= prodotto.dataEsposizione and prodotto.dataEsposizione <= dataFine:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList

    # Metodo di filtraggio dei prodotti in base alla categoria
    # idCategoria = codice della categoria su cui fare la selezione
    # file = nome del file da cui prelecare i prodotti e filtrarli
    def filtraCategoria(self, idCategoria, fileName):
        prodottiList = File().deserializza(fileName)
        prodottiFiltratiList = []
        for prodotto in prodottiList:
            if idCategoria == prodotto.idCategoria:
                prodottiFiltratiList.append(prodotto)
        self.filtrati = prodottiFiltratiList
        return prodottiFiltratiList

    # Metodo che filtra gli account in base al nome a al cognome
    # nome = nome del account
    # cognome = nome del account
    def filtraClienti(self, nome, cognome):
        listClientiBase = Account().recuperaListaOggetti()
        listClienti = list(listClientiBase)
        listClientiFiltrati = list()
        nome = str(nome).lower()
        cognome = str(cognome).lower()
        if nome != "":
            for cliente in listClienti:
                if nome in cliente.nome.lower():
                    listClientiFiltrati.append(cliente)
        if cognome != "":
            toFilter = list(listClientiFiltrati)
            listClientiFiltrati = list()
            for cliente in toFilter:
                if cognome in cliente.cognome.lower():
                    listClientiFiltrati.append(cliente)
        if listClientiFiltrati:
            return listClientiFiltrati
        return None

    # Metodo che cerca il prodotto in base al nome passato e alle opzion scelte nella tendina
    def elaboraCercaProdottoBtnClicked(self, name, textData, textPrezzo, textCategoria):
        listaCorrispondentiData = self.ifFiltraPerDataSelected(textData)
        listaCorrispondentiPrezzo = self.ifFiltraPerPrezzo(textPrezzo)
        listaCorrispondentiCategoria = self.ifFiltraPerCategoria(textCategoria)
        listaCorrispondenti = list()
        for prodottoData in listaCorrispondentiData:
            for prodottoPrezzo in listaCorrispondentiPrezzo:
                for prodottoCategoria in listaCorrispondentiCategoria:
                    if prodottoData.idProdotto == prodottoPrezzo.idProdotto == prodottoCategoria.idProdotto:
                        listaCorrispondenti.append(prodottoData)
        if name != "":
            temp = list()
            for prodotto in listaCorrispondenti:
                if name.upper() in prodotto.nomeProdotto.upper():
                    temp.append(prodotto)
            listaCorrispondenti = temp
        return listaCorrispondenti

    # Metodo che filtra i prodotti in base al periodo scelto
    # textData = parametro di filtraggio dei prodotti
    def ifFiltraPerDataSelected(self, textData):
        lista = Prodotto().recuperaListaProdottiInVendita()
        if textData == "0":
            pass
        elif textData == "1":
            lista = self.filtraDataEsposizione(datetime.today() - relativedelta(days=7),
                                               datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "2":
            lista = self.filtraDataEsposizione(datetime.today() - relativedelta(months=1),
                                               datetime.today(), PathDatabase().inVenditaTxt)
        elif textData == "3":
            lista = self.filtraDataEsposizione(datetime.today() - relativedelta(months=3),
                                               datetime.today(), PathDatabase().inVenditaTxt)
        return lista

    # Metodo che filtra i prodotti in base al prezzo massimo scelto
    # textPrezzo = parametro di filtraggio dei prodotti
    def ifFiltraPerPrezzo(self, textPrezzo):
        lista = Prodotto().recuperaListaProdottiInVendita()
        if textPrezzo == "0":
            pass
        elif textPrezzo == "1":
            lista = list(self.filtraPrezzo(0, 10, PathDatabase().inVenditaTxt))
        elif textPrezzo == "2":
            lista = list(self.filtraPrezzo(10, 20, PathDatabase().inVenditaTxt))
        elif textPrezzo == "3":
            lista = list(self.filtraPrezzo(20, 50, PathDatabase().inVenditaTxt))
        elif textPrezzo == "4":
            lista = list(self.filtraPrezzo(50, sys.maxsize, PathDatabase().inVenditaTxt))
        return lista

    # Metodo che filtra i prodotti in base alla categoria scelta nella tendina della view
    # textCategoria = parametro di filtraggio dei prodotti
    def ifFiltraPerCategoria(self, textCategoria):
        listaProdotti = Prodotto().recuperaListaProdottiInVendita()
        if textCategoria == "Tutte le Categorie" or textCategoria == "":
            return listaProdotti
        categoriaIdFiltro = None
        categorieList = Categoria().recuperaListaOggetti()
        for categoria in categorieList:
            if textCategoria == categoria.nome:
                categoriaIdFiltro = categoria.idCategoria
        listaProdottiTrovati = list()
        if categoriaIdFiltro == None: listaProdotti
        for prodotto in listaProdotti:
            if prodotto.idCategoria == categoriaIdFiltro:
                listaProdottiTrovati.append(prodotto)
        if listaProdottiTrovati:
            return listaProdottiTrovati
        else:
            return list()
