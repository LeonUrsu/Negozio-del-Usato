# Classe per la gestione di una ricevuta
import copy
import json
from datetime import date

from Database.PathDatabase import PathDatabase
from MVC.model.Interfacce.servizioInterface.RicevutaInterface import RicevutaInterface
from MVC.model.Interfacce.servizioInterface.ServizioInterface import ServizioInterface
from MVC.model.SistemService.File import File


class Ricevuta(ServizioInterface, RicevutaInterface):

    # Costruttore della classe, create() in EA
    def __init__(self):
        self.Id = None
        self.datetime = None
        self.prodotti = None

    # Metodo per aggiungere dei proidotti alla ricevuta
    def aggiungiProdotti(self, prodotti):
        date_format = '%d/%m/%Y'
        today = date.today()
        self.Id = self.newId()
        self.datetime = today.strftime(date_format)
        self.prodotti = prodotti

    # Metodo che permette di clonare un'istanza della classe
    # return Ricevuta
    def clone(self):
        deepCopy = copy.deepcopy(self)
        return deepCopy

    # metodo overiding dell'interfaccia JsonObjectToPythonObject
    # contenuto list
    # return dictionary
    def dictionaryEndcoder(self, contenuto):
        dict = json.dumps([self.__dict__ for self in contenuto])
        return dict

    # Medoto che prende una lsita di ricevute e le salva su un file
    def salvaRicevuta(self):
        fileName = PathDatabase().ricevuteTxt
        ricevuteList = File().deserializza(fileName)
        ricevuteList.append(self)
        fileName = PathDatabase().ricevuteTxt
        File().serializza(fileName, ricevuteList)

    # Metodo che legge un file serializzato e deserializza le ricevute dal file
    def recuperaListaOggetti(self):
        fileName = PathDatabase().ricevuteTxt
        listRicevute = File().deserializza(fileName)
        return listRicevute

    # Metodo che ritorna il nuovo id da assegnare alla Ricevuta da inserire
    # return = nuovo ID per la Ricevuta
    def newId(self):
        fileName = PathDatabase().parametriTxt
        letto = File().leggi(fileName)
        dictLetto = json.loads(letto)
        newId = int(dictLetto['lastIdRicevuta'] + 1)
        dictLetto['lastIdRicevuta'] = newId
        File().scrivi(fileName, json.dumps(dictLetto))
        return newId

    # metodo che dato un prodotto recupera le informazione come: prezzo, idProdotto, nomeProdotto
    def getInfoProdotto(self, prodotto):
        infoProdotto = {}
        infoProdotto['prezzoCorrente'] = prodotto.prezzoCorrente
        infoProdotto['idProdotto'] = prodotto.idProdotto
        infoProdotto['nomeProdotto'] = prodotto.nomeProdotto
        return infoProdotto
