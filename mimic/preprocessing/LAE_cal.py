import pandas as pd

# load
df = pd.read_csv('merged_with_readmission.csv', parse_dates=['admittime', 'dischtime'])
columns_to_drop = ['admit_provider_id', 'language', 'edregtime', 'edouttime', 'hospital_expire_flag']
df.drop(columns=columns_to_drop, inplace=True)

# L
df['admittime'] = pd.to_datetime(df['admittime'])
df['dischtime'] = pd.to_datetime(df['dischtime'])

# Calculate total stay duration
df['stay_hours'] = (df['dischtime'] - df['admittime']).dt.total_seconds() / 3600
df['natural_days'] = (df['dischtime'].dt.date - df['admittime'].dt.date).apply(lambda x: x.days + 1)

# If stay is less than 12 hours, count as 1 day; otherwise use natural day count
df['length_of_stay_days'] = df.apply(lambda row: 1 if row['stay_hours'] < 12 else row['natural_days'], axis=1)


# Apply LACE scoring rules for Length of Stay
def score_los(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    elif 4 <= x <= 6:
        return 4
    elif 7 <= x <= 13:
        return 5
    elif x >= 14:
        return 7
    else:
        return 0


df['Length'] = df['length_of_stay_days'].apply(score_los)
df.drop(columns=['stay_hours', 'natural_days', 'length_of_stay_days'], inplace=True)
cols = df.columns.tolist()
cols.insert(3, cols.pop(cols.index('Length')))
df = df[cols]

# A
df['admission_type'] = df['admission_type'].fillna('')
df['Acuity'] = df['admission_type'].apply(
    lambda x: 3 if 'EMER' in x or 'URGENT' in x else 0
)
cols = df.columns.tolist()
cols.insert(4, cols.pop(cols.index('Acuity')))
df = df[cols]

# E
df['is_emergency'] = df['admission_type'].apply(
    lambda x: 1 if 'EMER' in str(x).upper() or 'URGENT' in str(x).upper() else 0)
df['E'] = 0
df = df.sort_values(['subject_id', 'admittime'])
for subject_id, group in df.groupby('subject_id'):
    group = group.sort_values('admittime')
    for i in range(1, len(group)):
        curr_idx = group.index[i]
        curr_time = group.loc[curr_idx, 'admittime']
        past_6mo = group.iloc[:i]
        mask = (
                (past_6mo['admittime'] >= curr_time - pd.Timedelta(days=180)) &
                (past_6mo['is_emergency'] == 1)
        )
        e_val = min(mask.sum(), 4)
        df.loc[curr_idx, 'E'] = e_val

cols = df.columns.tolist()
cols.insert(5, cols.pop(cols.index('E')))
df = df[cols]
df.drop(columns=['is_emergency'], inplace=True)

# save
df.to_csv('merged_with_readmission_with_LACE.csv', index=False)
