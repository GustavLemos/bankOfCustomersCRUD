import json
from openpyxl import Workbook
from datetime import date

class export:
    def __init__(self):
        #Listas ordenadas
        listNome = []
        listId = []
        listContato = []
        listEmail = []
        listServico = []
        listValor = []
        listData = []


        fileObject = open("Banco-de-Dados/data.json", "r")
        jsonContent = fileObject.read()
        aList = json.loads(jsonContent)

        for b in aList:
            listNome.append(b['nome'])
            listId.append(b['id'])
            listContato.append(b['contato'])
            listEmail.append(b['email'])
            listServico.append(b['servico'])
            listValor.append(b['valor'])
            listData.append(b['dataDeFechamento'])

        cont = 0

        for a in listId:
            if cont == 0:
                arquivo_excel = Workbook()
                planilha1 = arquivo_excel.active
                planilha1.title = "data-" + str(date.today())
                planilha1['A1'] = 'ID'
                planilha1['B1'] = 'NOME'
                planilha1['C1'] = 'CONTATO'
                planilha1['D1'] = 'E-MAIL'
                planilha1['E1'] = 'SERVIÇO'
                planilha1['F1'] = 'VALOR'
                planilha1['G1'] = 'DATA DE FECHAMENTO'
            else:
                planilha1['A'+str(cont+1)] = a
                planilha1['B'+str(cont+1)] = listNome[cont]
                planilha1['C'+str(cont+1)] = listContato[cont]
                planilha1['D'+str(cont+1)] = listEmail[cont]
                planilha1['E'+str(cont+1)] = listServico[cont]
                planilha1['F'+str(cont+1)] = listValor[cont]
                planilha1['G'+str(cont+1)] = listData[cont]

            cont = cont + 1

        arquivo_excel.save("Banco-de-Dados/data.xlsx")  

