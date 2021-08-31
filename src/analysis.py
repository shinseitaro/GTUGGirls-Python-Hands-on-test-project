import pandas as pd

def to_datafrme(data):
    df = pd.DataFrame(data)
    df['post_time'] = pd.to_datetime(df['post_time'])
    return df


if __name__ == '__main__':

    pass