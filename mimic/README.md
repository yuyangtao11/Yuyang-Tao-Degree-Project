This folder holds every script and notebook referenced in the thesis.  
All experiments follow a three‑step workflow:  
1) data preparation; 2) machine learning prediction; 3) causal discovery.

| Sub‑folder | Contents | Thesis sections |
|------------|----------|-----------------|
| **preprocessing** | • Python scripts to extract MIMIC‑IV tables<br>• Feature engineering for *physical status*, LACE, length‑of‑stay buckets, etc.<br>• Train/validation/test split creators and basic visualisations | §4.1 Exploratory Data Analysis |
| **machine learning** | • Training pipelines for Random Forest, XGBoost, LightGBM, CatBoost, TabPFNv2, and logistic regression<br>• YAML configs for Cases 1‑4, plus the 10‑trial light tuning used in §4.2<br>• SHAP and performance‑metric notebooks that generate Table 4.1 and Figures 4.7‑4.10 | §4.2 Model Performance<br>§4.4 ML vs. Causal Comparison |
| **Causal Discovery** | • Implementations / wrappers for Nonlinear‑NOTEARS, FCI + RCIT, and DECI<br>• Edge‑weight extraction, PAG visualisation, and inclusion‑probability plotting<br>• Scripts that reproduce Figures 4.14‑4.18 and the qualitative analyses in §4.3 | §4.3 Causal Analysis |
