import pandas as pd
import random
from datetime import timedelta
from faker import Faker

fake = Faker("pt_BR")

# Listas de valores possíveis
taxas = ["1.6", "1.8", "2.3", "2.6", "3.0"]
lista_parcelas = ["1", "3", "6", "12", "24", "36"]
lista_periodicidade = ["1", "3", "6"]

# Gerando os dados fictícios
dados = []
for i in range(0, 50):
    numero_contrato = random.randint(1000000000, 9999999999)
    valor_contrato = random.randint(1, 200) * 1000
    liberacao = fake.date_between(start_date="-2y", end_date="today")
    taxa = random.choice(taxas)
    parcelas = random.choice(lista_parcelas)
    vencimento = liberacao + timedelta(days=random.randint(1, 10))
    periodicidade = random.choice(lista_periodicidade)

    dados.append([numero_contrato, valor_contrato, liberacao, taxa, parcelas, vencimento, periodicidade])

# Criando o DataFrame
colunas = ["PROPOSTA", "VALOR", "LIBERACAO", "TAXA", "PARCELAS", "VENCIMENTO", "PERIODICIDADE"]

df_propostas = pd.DataFrame(dados, columns=colunas)

# Exibindo as primeiras linhas
print(df_propostas.head())
df_propostas.to_excel("propostas.xlsx", index=False)