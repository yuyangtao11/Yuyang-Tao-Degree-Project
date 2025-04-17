import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.metrics import roc_auc_score

df = pd.read_csv("merged_with_LACE.csv")

df["lace_cut"] = pd.cut(df["LACE"],
                        bins=[-1, 4, 9, 100],
                        labels=["0-4", "5-9", ">=10"])

# Logistic Regression
model = sm.Logit.from_formula("readmitted ~ C(lace_cut, Treatment('0-4'))", data=df).fit(disp=0)

# p & coef
param_5_9 = model.params["C(lace_cut, Treatment('0-4'))[T.5-9]"]
param_10 = model.params["C(lace_cut, Treatment('0-4'))[T.>=10]"]

pval_5_9 = model.pvalues["C(lace_cut, Treatment('0-4'))[T.5-9]"]
pval_10 = model.pvalues["C(lace_cut, Treatment('0-4'))[T.>=10]"]

# CI
conf_int = model.conf_int()
conf_5_9 = conf_int.loc["C(lace_cut, Treatment('0-4'))[T.5-9]"]
conf_10 = conf_int.loc["C(lace_cut, Treatment('0-4'))[T.>=10]"]

# OR
or_5_9 = np.exp(param_5_9)
or_5_9_low, or_5_9_high = np.exp(conf_5_9[0]), np.exp(conf_5_9[1])

or_10 = np.exp(param_10)
or_10_low, or_10_high = np.exp(conf_10[0]), np.exp(conf_10[1])

print("\n Logistic Regression - LACE \n")
print("LACE index score      OR        95% CI (Lower, Upper)       p")
print("0-4            1.00")
print(f"5-9            {or_5_9:.2f}      ({or_5_9_low:.2f}, {or_5_9_high:.2f})    {pval_5_9:.4g}")
print(f">=10           {or_10:.2f}      ({or_10_low:.2f}, {or_10_high:.2f})    {pval_10:.4g}")

# ROC-AUC
df = pd.read_csv("merged_with_LACE.csv")
use_cols = ["readmitted", "LACE"]
df_sub = df[use_cols].copy()
df_sub = df_sub.replace([np.inf, -np.inf], np.nan)
df_sub = df_sub.dropna(axis=0, how='any')
df_sub["lace_cat"] = pd.cut(df_sub["LACE"], bins=[-1, 4, 9, float("inf")], labels=["0-4", "5-9", ">=10"])

# fit
model = sm.Logit.from_formula("readmitted ~ C(lace_cat, Treatment('0-4'))", data=df_sub).fit()
df_sub["pred_prob"] = model.predict(df_sub)
auc = roc_auc_score(df_sub["readmitted"], df_sub["pred_prob"])
print("ROC AUC =", auc)
