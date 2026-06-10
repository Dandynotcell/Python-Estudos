# 1. Entrada: o que o usuario ou sistema Fornece?
nome = input("Digite seu nome:")
# 2. Processamento: que regra será aplicada>
mensagem = f"ola, {nome}! Bem Vindo Ao Python"
# 3. Saida: Qual resutado Aparece?
print (mensagem)

# Bibliotecas Python: O que são e para que servem?
# Bibliotecas são coleções de código pré-escrito que fornecem funcionalidades específicas. Elas permitem que os desenvolvedores reutilizem código, economizando tempo e esforço. As bibliotecas podem incluir funções, classes e módulos que facilitam a realização de tarefas comuns, como manipulação de dados, criação de interfaces gráficas, acesso a bancos de dados, entre outros. Elas são essenciais para o desenvolvimento eficiente e rápido de software em Python.
# Exemplo de uso de biblioteca: importando a biblioteca math para calcular a raiz quadrada
import math 
print (math.sqrt (25))

# importa uma função específica da biblioteca math
from math import sqrt
print (sqrt(25))    

# usa apelido quando o nome é longo ou convencional
import detetime as dt 
print(dt.date.today())