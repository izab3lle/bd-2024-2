import pandas as pd

# Boa prática: Definir o tipo do
# retorno da função ( func() -> tipoDeRetorno: )


def create_example() -> pd.DataFrame:
    """Creates a DataFrame table.
    
    Returns:
        pd.DataFrame: Names and scores table.
    """
    tabela = pd.DataFrame({
        'nome': ['Renata', 'Anderson', 'Paulo'],
        'nota1': [10, 5, 9],
        'nota2': [7, 3, 9],
    })
    
    return tabela