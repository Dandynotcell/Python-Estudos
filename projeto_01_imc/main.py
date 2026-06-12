from datetime import datetime

from calculos import calcular_imc, classificar_imc
from historico import carregar_historico, salvar_historico


try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    registro = {
        "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "peso": peso,
        "altura": altura,
        "imc": round(imc, 2),
        "classificacao": classificacao
    }

    historico = carregar_historico()
    historico.append(registro)
    salvar_historico(historico)

    print()
    print("Resultado do IMC")
    print("----------------")
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")
    print()
    print("Registro salvo no histórico com sucesso.")

except ValueError as erro:
    print()
    print("Erro:")
    print(erro)
    print("Digite peso e altura usando números válidos.")