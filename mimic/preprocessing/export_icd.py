import pandas as pd
from sqlalchemy import create_engine

# connect SQL
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5430/mimic')

icd = pd.read_sql('SELECT * FROM mimiciv_hosp.diagnoses_icd', engine)
icd.to_csv('diagnoses_icd.csv', index=False)