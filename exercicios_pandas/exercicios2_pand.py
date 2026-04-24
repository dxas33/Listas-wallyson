#exercicios pandas,iloc,loc, etc...
#----------------------------------ねこ------------------------------------------
import pandas as pd
'''
conteudo = """jogo,genero,nota,preco,ano,plataforma
The Witcher 3,RPG,93,79.90,2015,PC
Celeste,Plataforma,91,36.99,2018,Multi
Hades,Roguelike,93,46.99,2020,Multi
Stardew Valley,Simulação,89,24.99,2016,Multi
Hollow Knight,Metroidvania,90,27.99,2017,Multi
Elden Ring,RPG,96,199.90,2022,Multi
Undertale,RPG,92,21.99,2015,PC
Cuphead,Plataforma,86,37.99,2017,Multi
Dead Cells,Roguelike,89,49.90,2018,Multi
Terraria,Sandbox,83,17.99,2011,PC
Minecraft,Sandbox,93,119.90,2011,Multi
Disco Elysium,RPG,97,69.90,2019,PC
Portal 2,Puzzle,95,19.99,2011,PC
Ori and the Blind Forest,Metroidvania,88,39.99,2015,Multi
Shovel Knight,Plataforma,90,54.90,2014,Multi"""
 
with open('jogos.csv', 'w', encoding='utf-8') as f:
    f.write(conteudo)
 
print("Arquivo jogos.csv criado!")
'''
import pandas as pd
 
df = pd.read_csv('jogos.csv')
#print(df)

# EXERCICIO 1

# A) há 15 jogos no total
#Dimensões: (linhas, colunas)
#print(df.shape)  # (15, 6)
 
#----------------------------------ねこ------------------------------------------

#B float64,int64 e str
# Informações sobre tipos e valores nulos
#print(df.info())

#----------------------------------ねこ------------------------------------------

#C) o preço medio é 56,6
# Estatísticas das colunas numéricas
# print(df.describe())

#----------------------------------ねこ------------------------------------------

#D)
# Linhas 0 a 2, colunas específicas
#print(df.loc[0:2, ['jogo', 'preco']])


# EXERCICIO 2 

df['genero'].value_counts()           # Minha previsão: quantos generos diferentes tem (7)
df['nota'].max()                       # Minha previsão: nota maxima entre os jogos (97)
df['preco'].min()                      # Minha previsão: preço minimo que existem entre os jogos (17.99)
df.loc[5, 'jogo']                      # Minha previsão: localiza o jogo na quinta posição ( Elden Ring )
df.iloc[0:3, 1:3]                      # Minha previsão: imprime as 3 primeiras linhas e colunas
df[['jogo', 'ano']].tail(3)            # Minha previsão: imprime o jogo e o ano dos 3 ultimos jogos (portal 2, ori e shovel knight(
df.describe().loc['mean']              # Minha previsão: descreve a media de preço dos jogos

