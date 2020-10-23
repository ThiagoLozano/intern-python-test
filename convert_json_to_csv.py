# Importa a Biblioteca Pandas.
import pandas as pd
import csv


class Conversor:
    # Método Construtor.
    def __init__(self):
        self.arquivo_json = pd.read_json('shopping.json')
        self.contador = 0
        self.total_l = 0

    # Função que cria a coluna 'total' e inseri o valor total de cada produto.
    def Criar_Coluna_Total(self):
        
        # Atribui o arquivo com a chave principal em uma variável 'arq'.
        arq = self.arquivo_json['order']

        # Contador de linhas.
        for c in arq:
            self.contador += 1

        # Inseri o valor total de cada produto.
        for c in range(self.contador):
            arq[c]['total'] = arq[c]['quantity'] * arq[c]['value']

        # Chama a função 'Converter_para_CSV'.
        self.Converter_para_CSV(arq)

    # Função que cria um arquivo CSV com os valores do JSON.
    def Converter_para_CSV(self, arq):

        # Faz a soma de todos os valores totais.
        for c in range(self.contador):
            self.total_l += arq[c]['total']

        # Cria um arquivo CSV.
        with open('resultado.csv', 'w') as arquivo_csv:
            columns = ['id', 'name', 'description', 'quantity', 'value', 'total']
            writer = csv.DictWriter(arquivo_csv, fieldnames=columns, delimiter='|', lineterminator='\n')
            writer.writeheader()

            # Inseri os valores em cada linha do CSV.
            for v in range(self.contador):
                writer.writerow(arq[v])

            # Escreve por último a linha 'Total'.
            writer.writerow(
                {'id': 'Total', 'name': '', 'description': '', 'quantity': '', 'value': '', 'total': self.total_l})


usuario = Conversor()
usuario.Criar_Coluna_Total()
