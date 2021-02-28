import pandas as pd

df = pd.read_csv('data/survey_results_public.csv')
schema_df = pd.read_csv('data/survey_results_schema.csv')

pd.set_option('display.max_columns', 61)
pd.set_option('display.max_rows', 61)

print(df.head())
