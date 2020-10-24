# PROJETO PYTHON: Conversor de Arquivos

> Um programa que converte arquivo CSV para JSON e JSON para CSV.

# Tecnologias Utilizadas
* **_PyCharm;_**
* **_Python 3;_**

### Saída do programa 'convert_json_to_csv.py'
```
id|name|description|quantity|value|total
1|Camisa|Camisa Social Preta|3|56.5|169.5
2|Regata|Regata 100% Algodão|6|9.99|59.94
3|Saia Rodada|Saia Rodada Rosa|2|29.9|59.8
4|Meia|Meia branca|3|5.0|15.0
5|Gorro|Gorro Preto|1|12.0|12.0
6|Moletom|Moletom Adidas|1|119.95|119.95
7|Bermuda|Bermuda Ciclone|3|35.0|105.0
8|Tênis|Tênis Nike Shox|1|450.0|450.0
Total|||||991.19
```

### Saída do programa 'convert_csv_to_json.py'
```
{
    "order": [
        {
            "ID": "1",
            "Name": "Camisa",
            "Description": "Camisa Social Preta",
            "Quantity": "3",
            "Value": "56.50"
        },
        {
            "ID": "2",
            "Name": "Regata",
            "Description": "Regata 100% Algodão",
            "Quantity": "6",
            "Value": "9.99"
        },
        {
            "ID": "3",
            "Name": "Saia Rodada",
            "Description": "Saia Rodada Rosa",
            "Quantity": "2",
            "Value": "29.90"
        },
        {
            "ID": "4",
            "Name": "Meia",
            "Description": "Meia branca",
            "Quantity": "3",
            "Value": "5.00"
        },
        {
            "ID": "5",
            "Name": "Gorro",
            "Description": "Gorro Preto",
            "Quantity": "1",
            "Value": "12.00"
        },
        {
            "ID": "6",
            "Name": "Moletom",
            "Description": "Moletom Adidas",
            "Quantity": "1",
            "Value": "119.95"
        },
        {
            "ID": "7",
            "Name": "Bermuda",
            "Description": "Bermuda Ciclone",
            "Quantity": "3",
            "Value": "35.00"
        },
        {
            "ID": "8",
            "Name": "Tênis",
            "Description": "Tênis Nike Shox",
            "Quantity": "1",
            "Value": "450.00"
        }
    ],
    "Total": 991.19
}
```

### Biblioteca Python Utilizada.

```
import pandas as pd
import csv
import json
```

### Gráfico da Quantidade pedida de cada Produto.
![Quantidade_Produtos](https://github.com/ThiagoLozano/intern-python-test/blob/main/gerados/Gr%C3%A1ficos/Quantidade_Produtos.png)
