import pandas as pd

#Criação da tabela
tabela = pd.DataFrame({
    'Nome': ['Renata', 'Anderson', 'Paulo'],
    'Nota1': [10, 5, 9],
    'Nota2': [7, 3, 9],
})

# Selecionar colunas ou mudar ordem
tabela[['Nota2', 'Nome', 'Nota1']]

#Filtrar tabelas
tabela.query('Nota1 > 7')
tabela.query('Nome == "Renata"')    # '[...] "String" ' ou "[...] 'String' "
tabela.query('Nome in ("Renata", "Paulo")')

tabela \
    .query('Nota1 > 7')
    
(
    tabela
        .query('Nota1 > 7')
)


# Criar colunas
tabela \
    .assign(
        # "lambda x" renomeia a tabela para melhorar a notação
        Media = lambda x: (x['Nota1'] + x['Nota2'])/2
    )
    