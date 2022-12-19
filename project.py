import pandas as pd

titanic_df = pd.read_csv('https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv')

titanic_df.info()

titanic_df.Age.hist()
