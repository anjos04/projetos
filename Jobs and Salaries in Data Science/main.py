import pandas as pd

leitura = pd.read_csv('C:\\Users\\carlo\\Desktop\\projetos\\Jobs and Salaries in Data Science\\jobs_in_data.csv')
remover = leitura.dropna()
print(remover)