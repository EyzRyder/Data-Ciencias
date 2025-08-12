import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotext
import pycountry

def aula03(df_limpo):
    print(df_limpo.head())

    #df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribuição de senioridade")

    # Gráfico de distribuição de senioridade
    plt.figure(figsize=(6,4))
    plt.title("Distribuição de senioridade")
    df_limpo['senioridade'].value_counts().plot(kind='bar', title="Distribuição de senioridade")
    plt.xlabel("Senioridade")
    plt.ylabel("Contagem")
    plt.tight_layout()
    plt.show()
    plt.savefig("Gráfico de distribuição de senioridade.png")

    # Gráfico de salário médio por senioridade
    plt.figure(figsize=(8,5))
    sns.barplot(data=df_limpo, x='senioridade', y='usd')
    plt.title("Salário médio por senioridade")
    plt.xlabel("Senioridade")
    plt.ylabel("Salário médio anual (USD)")
    plt.show()
    plt.savefig("Gráfico de salário médio por senioridade.png")

    print()
    print(df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False))
    print()
    ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
    print(ordem)
    print()
    plt.figure(figsize=(8,5))
    sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)
    plt.title("Salário médio por senioridade")
    plt.xlabel("Senioridade")
    plt.ylabel("Salário médio anual (USD)")
    plt.show()
    plt.savefig("Gráfico de salário médio por senioridade em ordem.png")

    plt.figure(figsize=(10,5))
    sns.histplot(df_limpo['usd'], bins = 50, kde=True)
    plt.title("Distribuição dos salários anuais")
    plt.xlabel("Salário em USD")
    plt.ylabel("Frequência")
    plt.show()
    plt.savefig("Gráfico de Distribuição dos salários anuais.png")


    plt.figure(figsize=(8,5))
    sns.boxplot(x=df_limpo['usd'])
    plt.title("Boxplot Salário")
    plt.xlabel("Salário em USD")
    plt.show()
    plt.savefig("Gráfico Boxplot Salário.png")

    ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']

    plt.figure(figsize=(8,5))
    sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade)
    plt.title("Boxplot da distribuição por senioridade")
    plt.xlabel("Salário em USD")
    plt.show()
    plt.savefig("Gráfico Boxplot da distribuição por senioridade.png")

    ordem_senioridade = ['junior', 'pleno', 'senior', 'executivo']

    plt.figure(figsize=(8,5))
    sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
    plt.title("Boxplot da distribuição por senioridade")
    plt.xlabel("Salário em USD")
    plt.show()

    plt.savefig("Gráfico Boxplot da distribuição por senioridade 2.png")

    # prompt: Crie um gráfico de média salarial por senioridade em barras usando o plotly

    senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

    fig = px.bar(senioridade_media_salario,
                 x='senioridade',
                 y='usd',
                 title='Média Salarial por Senioridade',
                 labels={'senioridade': 'Nível de Senioridade', 'usd': 'Média Salarial Anual (USD)'})

    fig.show()

    remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
    remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

    fig = px.pie(remoto_contagem,
                 names='tipo_trabalho',
                 values='quantidade',
                 title='Proporção dos tipos de trabalho'

              )

    fig.show()


    remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
    remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

    fig = px.pie(remoto_contagem,
                 names='tipo_trabalho',
                 values='quantidade',
                 title='Proporção dos tipos de trabalho',
                 hole=0.5
              )

    fig.show()

    remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
    remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

    fig = px.pie(remoto_contagem,
                 names='tipo_trabalho',
                 values='quantidade',
                 title='Proporção dos tipos de trabalho',
                 hole=0.5
              )
    fig.update_traces(textinfo='percent+label')
    fig.show()
    print()
    print(df_limpo.head())
    print()
    # Criar nova coluna com código ISO-3
    df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

    # Calcular média salarial por país (ISO-3)
    df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
    media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

    # Gerar o mapa
    fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='usd',
                    color_continuous_scale='rdylgn',
                    title='Salário médio de Cientista de Dados por país',
                    labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'})

    fig.show()
    print()
    print(df_limpo.head())
    print()
    df_limpo.to_csv('dados-imersao-final.csv', index=False)
    return df_limpo

# Função para converter ISO-2 para ISO-3
def iso2_to_iso3(code):
    try:
        return pycountry.countries.get(alpha_2=code).alpha_3
    except:
        return None
