import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class Graficos:
    # Método Construtor.
    def __init__(self):
        self.arq_csv = pd.read_csv('shopping.csv', delimiter='|')

    def Cria_Coluna_Total(self):
        # Cria a coluna 'Total' como os valores correspondentes.
        self.arq_csv['Total'] = self.arq_csv['Quantity'] * self.arq_csv['Value']

        # Chama a função 'Graficos'
        self.Quantidade_Pedida()

    def Quantidade_Pedida(self):
        # Criando uma figure, axes
        fig, ax = plt.subplots(figsize=(8, 6))

        # Criando o gráfico de Barras
        sns.barplot(x=self.arq_csv['Name'], y=self.arq_csv['Quantity'], ax=ax, data=self.arq_csv)

        # Configurações do Gráfico.
        plt.title('Quantidade pedida de cada Produto', fontdict={'fontsize': 15})
        plt.xlabel('Produtos', fontdict={'fontsize': 13})
        plt.ylabel('Quantidade Pedida', fontdict={'fontsize': 13})

        # Apaga aos axes do Top e da Direita.
        for axis in ['top', 'right']:
            ax.spines[axis].set_color(None)

        # Otimizar espaço da figure
        fig.tight_layout()
        plt.show()


usuario = Graficos()
usuario.Cria_Coluna_Total()
