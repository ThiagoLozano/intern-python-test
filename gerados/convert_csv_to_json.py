import csv
import json


class Conversor:
    # Método Construtor.
    def __init__(self):
        self.arquivo_csv = 'shopping.csv'
        self.arquivo_json = 'resultado.json'
        self.soma_total = 0

    def Converter_para_JSON(self):
        # Abre para leitura o arquivo CSV.
        with open(self.arquivo_csv, 'r', encoding='utf-8') as arq_csv:
            # Faz a leitura sem o caracter '|'.
            leitor = csv.reader(arq_csv, delimiter='|')

            # 'Pula' a primeira linha.
            next(leitor)

            # Cria um dicionário com a lista de pedidos(order).
            dados = {"order": []}

            # Passa pelas linhas do arquivo.
            for c in leitor:

                # Multiplica a Quantidade(Quantity) pelo Valor(Value) e soma com o próximo.
                self.soma_total += float(c[3]) * float(c[4])

                # Adiciona os valor de cada coluna nas linhas correspondentes.
                dados['order'].append(
                    {"ID": c[0], "Name": c[1], "Description": c[2], "Quantity": c[3], "Value": c[4]})
                dados['Total'] = self.soma_total

        # Cria um arquivo JSON.
        with open(self.arquivo_json, 'w', encoding='utf-8') as arq_json:
            # Faz um dump dos dados dentro do arquivo criado.
            # Faz uma identação com uma correção da liguagem.
            json.dump(dados, arq_json, ensure_ascii=False, indent=4)

        print('Convertido com sucesso!')


usuario = Conversor()
usuario.Converter_para_JSON()
