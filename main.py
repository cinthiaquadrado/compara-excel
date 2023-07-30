import pandas as pd

model = 'model.xlsx'
new = 'new_data.xlsx'

def compara_excel(model_file, new_file):
    df_model = pd.read_excel(model_file)
    df_new = pd.read_excel(new_file)

    if set(df_model.columns) == set(df_new.columns):
        print("A estrutura dos arquivos é a mesma.")
        return
    elif set(df_model.columns) - set(df_new.columns):
        missing_columns = set(df_model.columns) - set(df_new.columns)
        print(f'As colunas {missing_columns} estão faltando no arquivo.')
    elif set(df_new.columns) - set(df_model.columns):
        additional_columns = set(df_new.columns) - set(df_model.columns)
        print(f'As colunas {additional_columns} foram adicionadas no novo arquivo.')

compara_excel(model, new)
