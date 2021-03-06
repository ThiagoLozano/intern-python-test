import csv
import json


class ConversorJSON:
    # Método Construtor.
    def __init__(self):
        try:
            with open("shopping.json") as f:
                self.pedidos = json.load(f)
            self.Converter_para_CSV()
        except Exception as erro:
            print("Erro: {}".format(erro))

    # Método que converte para CSV.
    def Converter_para_CSV(self):
        # Lista que armazena os valor total de cada pedido.
        values = []

        with open("result_json_to_csv.csv", "w") as f:
            columns = ['ID', 'Name', 'Description', 'Quantity', 'Value', 'Total']
            escrever = csv.DictWriter(f, fieldnames=columns, delimiter='|', lineterminator='\n')
            escrever.writeheader()

            # Pega cada objeto do pedido e inseri no CSV.
            for pedido in self.pedidos['order']:
                id_order = pedido['id']
                name = pedido['name']
                description = pedido['description']
                quantity = pedido['quantity']
                value = pedido['value']
                total_order = value * quantity
                values.append(total_order)
                escrever.writerow(
                    {'ID': id_order, 'Name': name, 'Description': description, 'Quantity': quantity, 'Value': value,
                     'Total': total_order})
            escrever.writerow(
                {'ID': 'Total', 'Name': '', 'Description': '', 'Quantity': '', 'Value': '', 'Total': sum(values)})


usuario = ConversorJSON()
