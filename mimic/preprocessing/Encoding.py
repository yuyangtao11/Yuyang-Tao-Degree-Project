import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("merged_with_LACE.csv")

categorical_cols = [
    "admission_type",
    "admission_location",
    "discharge_location",
    "insurance",
    "marital_status",
    "race",
    "gender"
]

for col in categorical_cols:
    if col in df.columns:
        df[col] = df[col].fillna("Missing")

# One-Hot encoding
# df_encoded = pd.get_dummies(
#     df,
#     columns=categorical_cols,
#     prefix=categorical_cols,
#     drop_first=False
# )
#
# df_encoded = df_encoded.replace({False: 0, True: 1})
# df_encoded.to_csv("One_hot_encode.csv", index=False)

# Label Encoding
for col in categorical_cols:
    if col in df.columns:
        le = LabelEncoder()
        # Forced conversion to string type, then label-encode
        df[col] = le.fit_transform(df[col].astype(str))


df.to_csv("label_encoded.csv", index=False)
