import pandas as pd
df1 = pd.read_csv('https://raw.githubusercontent.com/IranNash/Analisis-dengue/refs/heads/main/dengue_abierto.csv')

def conteo_genero(df):
    conteo = df.groupby('SEXO').size().reset_index(name = 'conteo')
    return conteo

genero = conteo_genero(df1)

print(genero)

#para test
def dimen(df):
    conteo = df.groupby('SEXO').size().reset_index(name = 'conteo')
    num = len(conteo)
    return num

numero = dimen(df1)
print(numero)

