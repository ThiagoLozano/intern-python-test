import csv
import json


class ConversorCSV:
    # Método Construtor.
    def __init__(self):
        try:
            with open("shopping.csv", 'r', encoding='utf_8') as f:
                self.pedidos = csv.reader(f, delimiter='|')
                next(self.pedidos)
                self.Converter_para_JSON()
        except Exception as erro:
            print("Erro: {}".format(erro))
            exit(0)

    # Método que converte em JSON.
    def Converter_para_JSON(self):
        # Cria um Dicionário que armazena os pedidos.
        dados = {"order": []}

        # Cria uma lista que armazena os valores de cada pedido.
        valores = []

        for pedido in self.pedidos:
            # Cria o total de cada pedido.
            total_order = float(pedido[3]) * float(pedido[4])
            valores.append(total_order)
            
            # Inseri no dicionário.
            dados['order'].append({"ID": pedido[0], "Name": pedido[1], "Description": pedido[2], "Quantity": pedido[3],
                                   "Value": pedido[4], "Total": str(total_order)})
            dados['Total'] = sum(valores)
        
        # Cria o JSON.
        with open("result_csv_to_json.json", "w") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)


usuario = ConversorCSV()
