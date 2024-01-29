import pandas as pd

def drop_missing_values(df, columns):

    return df.dropna(subset=columns)

def remove_percentage(df,column):
    df[column] = df[column].str.replace('%', '').astype(float)

def drop_columns(df, columns):

    columns_to_drop = [col for col in columns if col in df.columns]

    return df.drop(columns_to_drop, axis=1)

def fill_missing_values(df, column, method='mean'):

    if method == 'mean':
        fill_value = df[column].mean()
    elif method == 'median':
        fill_value = df[column].median()
    elif method == 'mode':
        fill_value = df[column].mode()[0]
    else:
        raise ValueError("Method must be 'mean', 'median', or 'mode'.")

    df[column] = df[column].fillna(fill_value)
    return df

def standardize_column_names(df):

    df.columns = df.columns.str.lower().str.replace(' ', '_')
    return df

def remove_duplicates(df):

    return df.drop_duplicates()

def standardize_column_names(df):

    df.columns = df.columns.str.strip().str.replace(' ', '_').str.lower()
    return df

def unique_values_for_categorical (df):

    categorical_columns = df.select_dtypes(include=['object', 'category']).columns

    unique_values = {}

    for column in categorical_columns:
        unique_values[column] = df[column].unique()
        print(f'{column} uniques: {unique_values[column]}')

if __name__ == "__main__":

    data = {'Name': ['Alice', 'Bob', None, 'David', 'Alice'],
            'Age': [25, 30, 35, 40, '25']}
    df = pd.DataFrame(data)

    df = drop_missing_values(df, ['Name'])
    df = fill_missing_values(df, 'Age', method='median')
    df = standardize_column_names(df)
    df = remove_duplicates(df)

    print(df)
