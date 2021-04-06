import json
from tkinter import *
from class_create import create
from class_search import search
from class_edit import edit
from class_delete import delet
from class_export import export

class Application:
    def __init__(self, master=None):
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
        self.terceiroContainer["pady"] = 40
        self.terceiroContainer.pack()

        #Atribuindo primeiro container o titulo
        self.titulo = Label(self.primeiroContainer, text="Banco de Clientes")
        self.titulo["font"] = ("Arial", "25", "bold")
        self.titulo.pack()

        #botao 1 de criar registro
        self.criar = Button(self.terceiroContainer)
        self.criar["text"] = "Criar"
        self.criar["font"] = ("Calibri", "15")
        self.criar["width"] = 12
        self.criar["command"] = create
        self.criar.pack()

        #botao 2 de obter registro
        self.obter = Button(self.terceiroContainer)
        self.obter["text"] = "Obter"
        self.obter["font"] = ("Calibri", "15")
        self.obter["width"] = 12
        self.obter["command"] = search
        self.obter.pack()

        #botao 3 de editar registro
        self.edit = Button(self.terceiroContainer)
        self.edit["text"] = "Editar"
        self.edit["font"] = ("Calibri", "15")
        self.edit["width"] = 12
        self.edit["command"] = edit
        self.edit.pack()

        #botao 4 de deletar registro
        self.delete = Button(self.terceiroContainer)
        self.delete["text"] = "Excluir"
        self.delete["font"] = ("Calibri", "15")
        self.delete["width"] = 12
        self.delete["command"] = delet
        self.delete.pack()

        #botao 5 de exportar dataBase
        self.delete = Button(self.terceiroContainer)
        self.delete["text"] = "Exportar Banco"
        self.delete["font"] = ("Calibri", "15")
        self.delete["width"] = 12
        self.delete["command"] = export
        self.delete.pack()

        #botao 2 de sair
        self.sair = Button(self.terceiroContainer)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "15")
        self.sair["width"] = 5
        self.sair["command"] = self.primeiroContainer.quit
        self.sair.pack()

root = Tk("Banco de Dados")
Application(root)
root.mainloop()
