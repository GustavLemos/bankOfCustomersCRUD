import json
from tkinter import *

class search:
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
        self.titulo = Label(self.primeiroContainer, text="Pesquisar Cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #Atribuindo segundo container campo nome
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        self.dataLabel = Label(self.segundoContainer, text="Data:", font=self.fontePadrao)
        self.dataLabel.pack(side=LEFT)

        self.data = Entry(self.segundoContainer)
        self.data["width"] = 30
        self.data["font"] = self.fontePadrao
        self.data.pack(side=LEFT)

        #botao 1 de pesquisar
        self.pesquisar = Button(self.terceiroContainer)
        self.pesquisar["text"] = "Pesquisar"
        self.pesquisar["font"] = ("Calibri", "8")
        self.pesquisar["width"] = 12
        self.pesquisar["command"] =  self.searchClient
        self.pesquisar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

    #Método que realiza cadastro
    def searchClient(self):
       
        cliente = str(self.nome.get())
        data = self.data.get()
        self.mensagem["text"] = ""

        #Ler DataBase:
        fileObject = open("Banco-de-Dados/data.json" , "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)
        string = []
        
        if cliente or data != "":
            #Buscadores:
            for b in aList:
                #Nome:
                if b['nome'] != "":
                    if cliente.lower() == b['nome'].lower():
                        string.append("\n\n Código: "+ b['id'] +"\nCliente: "+ b['nome'] +"\n" +"Contato: "+ b['contato']+"\n" +"E-mail: "+ b['email']+"\n" +"Serviço: "+ b['servico']+"\n" +"Vencimento: "+ b['dataDeFechamento']+"\n" +"Valor: "+ b['valor'] + "\n") 
                       
                #Data:
                if b['dataDeFechamento'] != "":
                    if data.lower() == b['dataDeFechamento'].lower():
                        string.append("\n\n Código: "+ b['id'] +"\nCliente: "+ b['nome'] +"\n" +"Contato: "+ b['contato']+"\n" +"E-mail: "+ b['email']+"\n" +"Serviço: "+ b['servico']+"\n" +"Vencimento: "+ b['dataDeFechamento']+"\n" +"Valor: "+ b['valor'] + "\n") 
                
                self.mensagem["text"]  = string 
            
        else:
            self.mensagem["text"] = "Cliente não encontrado !"

obter = Tk()
search(obter)
obter.mainloop
