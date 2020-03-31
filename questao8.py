# -*- coding: utf-8 -*-
# O comentário acima é para garantir a correta leitura do arquivo que está em UTF-8
# Vamos importar o arquivo csv
import csv

# Criar uma classe para ficar melhor para tratar as informações do arquivo
class CarroInfo:
    def __init__(self, modelo, valor, impostos, consumo_medio, seguro_custo):
        self.modelo = modelo
        self.valor = float(valor)
        self.impostos = float(impostos)
        self.consumo_medio = float(consumo_medio)
        self.seguro_custo = float(seguro_custo)
        self.valor_consumo = float((10000 / self.consumo_medio) * 4.51)
        self.gasto_total = float(self.valor + self.impostos + self.valor_consumo + self.seguro_custo)
    def __str__(self):
        return self.modelo


def carrega_dados():
    arquivo = open("dados-veiculo.csv", 'r+')
    registros = csv.reader(arquivo, delimiter=',', quotechar='"')
    carros_lista = []

    for registro in registros:
        if registro[0] != "Modelo do veiculo":
            registro = CarroInfo(registro[0], registro[1], registro[2], registro[3], registro[4])
            carros_lista.append(registro)
    return carros_lista

def mostra_informacoes(carros_info):
    carros_info.sort(key=lambda c: c.gasto_total)
    # Sort pega a lista de carros_info e ordena pelo menor valor de gasto_total
    for carro_info in carros_info:
        print(carro_info.modelo + " -> R$ " + str(round(carro_info.gasto_total,2)))
    # Para imprimir o carro com menor gasto:
    menor_gasto = str(carros_info[0])
    print("\nO carro com menor gasto é o " + menor_gasto)

carros_info = carrega_dados()
mostra_informacoes(carros_info)

