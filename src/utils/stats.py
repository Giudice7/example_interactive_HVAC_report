import pandas as pd


def calculate_top_coldest_days(df: pd.DataFrame, k: int = 5):
    """
    Calculate the top k coldest days in the dataset
    :param df: the pd.DataFrame with Datetime and OA_TEMP columns
    :param k: the number of top coldest days to calculate
    :return: pd.Dataframe with the top k coldest days
    """

    df['Datetime'] = pd.to_datetime(df['Datetime'])
    df_temp = df[['Datetime', 'OA_TEMP']].copy()

    # Resample the data to daily
    df_temp.set_index('Datetime', inplace=True)
    df_temp = df_temp.resample('D').mean().round(2)

    # Get the top k coldest days
    top_k_coldest_days = df_temp.nsmallest(k, 'OA_TEMP')
    top_k_coldest_days.columns = ['Outdoor Air Mean Temperature']

    return top_k_coldest_days
