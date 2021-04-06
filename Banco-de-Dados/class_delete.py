import json
from tkinter import *

class delet:
    def __init__(self, master = None):
        #Fonte do form:
        self.fontePadrao = ("Arial", "10")
        #Lista Containers:
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()

        #Atribuindo primeiro container o titulo
        self.titulo = Label(self.primeiroContainer, text="Deletar cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #Atribuindo segundo container campo nome
        self.idLabel = Label(self.segundoContainer,text="Código", font=self.fontePadrao)
        self.idLabel.pack(side=LEFT)

        self.id = Entry(self.segundoContainer)
        self.id["width"] = 30
        self.id["font"] = self.fontePadrao
        self.id.pack(side=LEFT)

        #botao 1 de autenticar
        self.deletar = Button(self.quartoContainer)
        self.deletar["text"] = "Deletar"
        self.deletar["font"] = ("Calibri", "8")
        self.deletar["width"] = 12
        self.deletar["command"] = self.deleteClient
        self.deletar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()


    #Método que realiza exclusão
    def deleteClient(self):
        codigo = self.id.get()

        if codigo != "":
            #ler lista atual:
            fileObject = open("Banco-de-Dados/data.json", "r")
            jsonContent = fileObject.read()
            aList = json.loads(jsonContent)
            for b in aList:
                if b['id'] == codigo:
                    #Deletando Registro # nao funcionou
                    aList.remove(b)
                    arquivo = open('Banco-de-Dados/data.json', 'w')
                    banco = str(aList).replace("'",'"')                
                    arquivo.write(banco)
                    arquivo.close()
                    self.mensagem["text"] = "Cliente deletado!"

        else:
            self.mensagem["text"] = "Campo vazio ou incorreto!"
  

exclui = Tk()
delet(exclui)
exclui.mainloop
