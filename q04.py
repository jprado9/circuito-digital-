import sys
import math

def main():
    cidade_num = 1
    while True:
        linha = sys.stdin.readline()
        if not linha:
            break
        N = int(linha.strip())
        if N == 0:
            break

        imoveis = []
        total_pessoas = 0
        total_consumo = 0

        consumo_dict = {}

        for _ in range(N):
            moradores, consumo = map(int, sys.stdin.readline().split())
            consumo_por_pessoa = consumo // moradores

            if consumo_por_pessoa in consumo_dict:
                consumo_dict[consumo_por_pessoa] += moradores
            else:
                consumo_dict[consumo_por_pessoa] = moradores

            total_pessoas += moradores
            total_consumo += consumo

        # ordenar pelo consumo por pessoa
        ordenado = sorted(consumo_dict.items())

        if cidade_num > 1:
            print()

        print(f"Cidade# {cidade_num}:")
        print(' '.join(f"{moradores}-{consumo}" for consumo, moradores in ordenado))

        # consumo médio (com 2 casas decimais, sem arredondamento)
        consumo_medio = total_consumo / total_pessoas
        print(f"Consumo medio: {math.floor(consumo_medio * 100) / 100:.2f} m3.")

        cidade_num += 1

if __name__ == "__main__":
    main()
