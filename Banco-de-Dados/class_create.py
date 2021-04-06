import json
from tkinter import *

class create:
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
        self.titulo = Label(self.primeiroContainer, text="Cadastar cliente")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        #Atribuindo segundo container campo nome
        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)

        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)


        self.contatoLabel = Label(self.segundoContainer, text="Contato:", font=self.fontePadrao)
        self.contatoLabel.pack(side=LEFT)

        self.contato = Entry(self.segundoContainer)
        self.contato["width"] = 30
        self.contato["font"] = self.fontePadrao
        self.contato.pack(side=LEFT)


        self.emailLabel = Label(self.segundoContainer, text="E-mail", font=self.fontePadrao)
        self.emailLabel.pack(side=LEFT)

        self.email = Entry(self.segundoContainer)
        self.email["width"] = 30
        self.email["font"] = self.fontePadrao
        self.email.pack(side=LEFT)


        self.servicoLabel = Label(self.terceiroContainer, text="Serviço", font=self.fontePadrao)
        self.servicoLabel.pack(side=LEFT)

        self.servico = Entry(self.terceiroContainer)
        self.servico["width"] = 30
        self.servico["font"] = self.fontePadrao
        self.servico.pack(side=LEFT)


        self.valorLabel = Label(self.terceiroContainer, text="Valor", font=self.fontePadrao)
        self.valorLabel.pack(side=LEFT)

        self.valor = Entry(self.terceiroContainer)
        self.valor["width"] = 5
        self.valor["font"] = self.fontePadrao
        #mascarndo input
        #self.valor["show"] = "*"
        self.valor.pack(side=LEFT)

        self.dataLabel = Label(self.terceiroContainer, text="Data de Fechamento", font=self.fontePadrao)
        self.dataLabel.pack(side=LEFT)

        self.data = Entry(self.terceiroContainer)
        self.data["width"] = 10
        self.data["font"] = self.fontePadrao
        #mascarndo input
        #self.valor["show"] = "*"
        self.data.pack(side=LEFT)


        #botao 1 de CREATE
        self.criar = Button(self.quartoContainer)
        self.criar["text"] = "Cadastrar"
        self.criar["font"] = ("Calibri", "8")
        self.criar["width"] = 12
        self.criar["command"] = self.createClient
        self.criar.pack()

        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()


    #Método que realiza cadastro
    def createClient(self):
        cliente = self.nome.get()
        contato = self.contato.get()
        eMail = self.email.get()
        servico = self.servico.get()
        valor = self.valor.get()
        dataDeFechamento = self.data.get()
        #Conferindo preenchimento e validando os campos
        if cliente != "" and contato != "" and eMail != "" and servico != "" and valor != "" and dataDeFechamento != "":
            #Cadastrando
            fileObject = open("Banco-de-Dados/data.json", "r")
            jsonContent = fileObject.read()
            numeroId = generateId(jsonContent)
            #Adicionando cliente a super string do banco
            aList = str(jsonContent).replace("]"," ")
            instancia = '{"id":"'+ numeroId +'","nome":"'+ cliente +'","contato":"'+ contato +'","email":"'+ eMail +'","servico":"'+ servico +'","dataDeFechamento":"'+ dataDeFechamento +'","valor":"'+ valor +'"}' 
            aList = aList + "," + instancia + "]"

            arquivo = open('Banco-de-Dados/data.json', 'w')
            arquivo.write(aList)
            arquivo.close()
            self.primeiroContainer.quit
            self.mensagem["text"] = "Cliente cadastrado!"
        else:
            self.mensagem["text"] = "Campo vazio ou incorreto!"

def generateId(banco):
    listIds = json.loads(banco)
    maior = 0
    for x in listIds:
        instancia = int(x['id'])
        if instancia > maior:
            maior = instancia
    return str(maior + 1)         

creat = Tk()
create(creat)
creat.mainloop
