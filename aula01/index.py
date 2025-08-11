import pandas as pd
def aula01 ():
    df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
    #df is a data frame

    #df.head() prints the first 5, and the first paramter is to change how much is called, so head(10) calls 10 rows
    print(df.head(10))
    print(df.info())
    print(df.describe())
    print(df.shape) # ele vai retornar uma tupla (linhas , colunas)
    linhas, colunas = df.shape[0],df.shape[1]

    print(f"Esse arquivo tem {linhas} linhas e {colunas} colunas")
    print("Row: ",linhas)
    print("Cols: ",colunas)

    print(df.columns)

    # Dicionário de renomeação
    novos_nomes = {
        'work_year': 'ano',
        'experience_level': 'senioridade',
        'employment_type': 'contrato',
        'job_title': 'cargo',
        'salary': 'salario',
        'salary_currency': 'moeda',
        'salary_in_usd': 'usd',
        'employee_residence': 'residencia',
        'remote_ratio': 'remoto',
        'company_location': 'empresa',
        'company_size': 'tamanho_empresa'
    }

    # Aplicando renomeação
    df.rename(columns=novos_nomes, inplace=True)

    # Verificando resultado
    print(df.head())

    print(df["senioridade"].value_counts())
    print(df["contrato"].value_counts())
    print(df['remoto'].value_counts())
    print(df["tamanho_empresa"].value_counts())

    senioridade = {
        'SE': 'senior',
        'MI': 'pleno',
        'EN': 'junior',
        'EX': 'executivo'
    }
    df['senioridade'] = df['senioridade'].replace(senioridade)
    print(df['senioridade'].value_counts())

    contrato = {
        'FT': 'integral',
        'PT': 'parcial',
        'CT': 'contrato',
        'FL': 'freelancer'
    }
    df['contrato'] = df['contrato'].replace(contrato)
    print(df['contrato'].value_counts())

    tamanho_empresa = {
        'L': 'grande',
        'S': 'pequena',
        'M':	'media'

    }
    df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)
    print(df['tamanho_empresa'].value_counts())




    mapa_trabalho = {
        0: 'presencial',
        100: 'remoto',
        50: 'hibrido'
    }

    df['remoto'] = df['remoto'].replace(mapa_trabalho)
    print(df['remoto'].value_counts())

    print(df.head())

    print(df.describe(include="object"))
    return df

def dadosAula01():
    df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")
    # Dicionário de renomeação
    novos_nomes = {
        'work_year': 'ano',
        'experience_level': 'senioridade',
        'employment_type': 'contrato',
        'job_title': 'cargo',
        'salary': 'salario',
        'salary_currency': 'moeda',
        'salary_in_usd': 'usd',
        'employee_residence': 'residencia',
        'remote_ratio': 'remoto',
        'company_location': 'empresa',
        'company_size': 'tamanho_empresa'
    }

    # Aplicando renomeação
    df.rename(columns=novos_nomes, inplace=True)

    senioridade = {
        'SE': 'senior',
        'MI': 'pleno',
        'EN': 'junior',
        'EX': 'executivo'
    }
    df['senioridade'] = df['senioridade'].replace(senioridade)

    contrato = {
        'FT': 'integral',
        'PT': 'parcial',
        'CT': 'contrato',
        'FL': 'freelancer'
    }
    df['contrato'] = df['contrato'].replace(contrato)

    tamanho_empresa = {
        'L': 'grande',
        'S': 'pequena',
        'M':	'media'

    }
    df['tamanho_empresa'] = df['tamanho_empresa'].replace(tamanho_empresa)

    mapa_trabalho = {
        0: 'presencial',
        100: 'remoto',
        50: 'hibrido'
    }

    df['remoto'] = df['remoto'].replace(mapa_trabalho)
    return df
