import pandas as pd
from sqlalchemy import create_engine
from datetime import timedelta

# connect PostgreSQL
engine = create_engine('postgresql://postgres:123456@127.0.0.1:5430/mimic')

patients = pd.read_sql('SELECT * FROM mimiciv_hosp.patients', engine)
admissions = pd.read_sql('SELECT * FROM mimiciv_hosp.admissions', engine)

# combine
merged = pd.merge(admissions, patients, on='subject_id', how='left')

merged['admittime'] = pd.to_datetime(merged['admittime'])
merged['dischtime'] = pd.to_datetime(merged['dischtime'])

# readmission or not
merged = merged.sort_values(['subject_id', 'admittime'])
merged['readmitted'] = 0

for subject_id, group in merged.groupby('subject_id'):
    group = group.sort_values('admittime')
    disch_times = group['dischtime'].values
    admit_times = group['admittime'].values
    hadm_ids = group['hadm_id'].values

    for i in range(len(group) - 1):
        if pd.notnull(disch_times[i]) and pd.notnull(admit_times[i+1]):
            gap = admit_times[i+1] - disch_times[i]
            gap_days = gap / pd.Timedelta(days=1) 
            if 0 < gap_days <= 30:
                merged.loc[merged['hadm_id'] == hadm_ids[i], 'readmitted'] = 1

cols = merged.columns.tolist()
cols.insert(1, cols.pop(cols.index('hadm_id')))
cols.insert(2, cols.pop(cols.index('readmitted')))
merged = merged[cols]
merged.loc[merged['discharge_location'] == 'DIED', 'readmitted'] = 1
merged['dod'] = pd.to_datetime(merged['dod'], errors='coerce')
merged['dischtime'] = pd.to_datetime(merged['dischtime'], errors='coerce')
death_within_30_days = (merged['dod'].notna()) & ((merged['dod'] - merged['dischtime']) <= timedelta(days=30))
merged.loc[death_within_30_days, 'readmitted'] = 1

# save
merged.to_csv('merged_with_readmission.csv', index=False)
