from pandas import DataFrame


def compute_death_rate(data: DataFrame) -> DataFrame:
    data['death_rate'] = data['Deaths'] / data['Active']
    return data
