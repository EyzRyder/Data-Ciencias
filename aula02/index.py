import pandas as pd
import numpy as np

def aula02(df):
    print(df.isnull())
    print()
    print(df.isnull().sum())
    print()
    print(df["ano"].unique())
    print()

    #Exibindo quais linhas estão com os anos nulos:
    print()
    print(df[df.isnull().any(axis=1)])
    print()

    # 1. Preenchimento com Valores Derivados (Imputation)
    # Para salario: Usar a mediana ou média do salário da mesma categoria, senioridade e país.

    # 2. Remover Linhas com Dados Faltantes
    # Caso a quantidade de dados nulos seja muito pequena (como neste caso, apenas 5 linhas), você pode simplesmente removê-las.

    # 3. Inferência e Preenchimento com Regras de Negócio
    # Preencher com base em regras claras.
    df_salarios = pd.DataFrame({
        'nome':['Amanda','Beatriz','Celia','Day','Valkiria'],
        'salario':[4000,np.nan,5000,np.nan,100000]
    })
    df_salarios['salario_media']=df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
    df_salarios['salario_mediana']=df_salarios['salario'].fillna(df_salarios['salario'].median())
    print()
    print(df_salarios)
    print()

    df_temperaturas = pd.DataFrame({
        'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
        'temperatura': [30, np.nan, np.nan, 28, 27]
    })

    df_temperaturas['preenchido_ffill'] = df_temperaturas['temperatura'].ffill()

    print()
    print(df_temperaturas)
    print()



    df_temperaturas = pd.DataFrame({
        'dia': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex'],
        'temperatura': [30, np.nan, np.nan, 28, 27]
    })

    df_temperaturas['preenchido_bfill'] = df_temperaturas['temperatura'].bfill()

    print()
    print(df_temperaturas)
    print()

    df_cidades = pd.DataFrame({
        'nome':['Amanda','Beatriz','Celia','Day','Valkiria'],
        'cidade': ['São Paulo', np.nan, 'Curitiba', np.nan, 'Salvador']
    })

    df_cidades['cidade_corrigida'] = df_cidades['cidade'].fillna('Não informado')

    print()
    print(df_cidades)
    print()

    df_limpo = df.dropna()
    #Obs: também dá para especificar a coluna, com dropna(subset=['nome da coluna'])
    print()
    print(df_limpo.isnull().sum())
    print()
    print(df_limpo.head())
    print()
    print(df_limpo.info())
    print()
    df_limpo = df_limpo.assign(ano=df_limpo['ano'].astype('Int64'))
    print()
    print(df_limpo.head())
    print()
    print(df_limpo.info())
    df_limpo.to_csv('dados-imersao.csv', index=False)






def dadosAula01():
    print()
