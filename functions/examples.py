import pandas as pd

# Boa prática: Definir o tipo do
# retorno da função ( func() -> tipoDeRetorno: )


def create_example() -> pd.DataFrame:
    """Creates a DataFrame table.
    
    Returns:
        pd.DataFrame: Names and scores table.
    """
    tabela = pd.DataFrame({
        'Nome': ['Renata', 'Anderson', 'Paulo'],
        'Nota1': [10, 5, 9],
        'Nota2': [7, 3, 9],
    })
    
    return tabela