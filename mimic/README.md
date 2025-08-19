This folder holds every script and notebook referenced in the thesis.  
All experiments follow a three‑step workflow:  
1) Data preparation  
2) Machine learning prediction  
3) Causal discovery  

## Preprocessing

The `preprocessing` folder contains all scripts and notebooks used to extract, clean, and prepare the dataset before running machine learning and causal discovery experiments.

### Workflow
1. **Import MIMIC-IV data into PostgreSQL**  
   Before running the scripts, the raw MIMIC-IV tables are first imported into a local PostgreSQL database. This enables direct access to the data through Python (via the `sqlalchemy` library) and allows efficient querying.

2. **Merge_Pat_Adm.py**  
   Extracts patient and admission information from PostgreSQL and stores `merged_with_readmission.csv`.  
   → Base cohort file with identifiers, timestamps, demographics, and a 30-day readmission/death label; all later steps build on this table.

3. **LAE_cal.py**  
   Calculates **Length**, **Acuity**, and **Emergency visits** (L, A, E from the LACE index), saving `merged_with_readmission_with_LACE.csv`.  
   → Adds clinical risk components to the base cohort for downstream modeling.

4. **C_cal.py**  
   Calculates **Comorbidity** (C from the LACE index), producing `merged_with_LACE.csv`.  
   → Provides the full LACE score per admission for risk stratification and analysis.

5. **copecat.ipynb**  
   Uses the CopeCat pipeline to extract additional patient variables, merges with prior data, and outputs `after_cop.csv`.  
   → Enriches features beyond LACE to support broader experiments.

6. **preprocessing.ipynb**  
   Performs further preprocessing, including:  
   - Variable name mapping  
   - Removing outliers  
   - Dropping variables with excessive missing values  
   - Encoding variables  

   Produces:  
   - `encoded_clean_data.csv` – cleaned and encoded dataset ready for modeling  
   - `encoded_clean_data2.csv` – additionally processed to approximate **independent and identically distributed (IID)** conditions  
   - `encoded_clean_data3.csv` – IID-processed with **feature selection** for ML and causal discovery  
   → Final inputs used across prediction and causal analyses.

7. **Visualization.ipynb**, **eda.ipynb**, **LA_age_check.ipynb**  
   Conduct exploratory analysis and visualization (e.g., age, LACE, gender), and sanity-check variable usefulness.  
   → Validates the preprocessing pipeline and guides feature choices for later stages.

## Machine Learning

The `machine learning` folder contains scripts and notebooks implementing multiple predictive models for hospital readmission, along with feature importance analysis.

### Workflow
1. **ml_output.ipynb**  
   Implements six different machine learning algorithms to predict hospital readmission:
   - **XGBoost**  
   - **Random Forest**  
   - **LightGBM**  
   - **CatBoost**  
   - **TabPFNv2**  
   - **Logistic Regression**  

   Each algorithm is trained and evaluated under various **feature set combinations**, enabling performance comparison across different input configurations.  
   The resulting outputs represent predictive performance under multiple experimental cases.

2. **Feature Importance Analysis**  
   Uses the **SHAP (SHapley Additive exPlanations)** method to quantify the contribution of each feature to the model predictions.  
   This provides interpretable insights into which features are most influential for readmission prediction across models.

## Causal Discovery

The `Causal Discovery` folder contains scripts and notebooks for inferring causal relationships among clinical variables using multiple causal discovery algorithms.

### Workflow
1. **deci.ipynb**  
   Applies **DECI (Differentiable Causal Discovery with Interventions)** to learn causal structures from the dataset, producing directed acyclic graphs (DAGs) that represent the inferred causal relationships.

2. **fci_test.ipynb** and **fci_seg.ipynb**  
   Implement the **Fast Causal Inference (FCI)** combined with the **Randomized Conditional Independence Test (RCIT)** as the conditional independence testing method to handle potential latent confounders and infer Partial Ancestral Graphs (PAGs).  

3. **notears.ipynb** and **notears_seg.ipynb**  
   Implement **Nonlinear-NOTEARS**, a gradient-based causal structure learning method, to estimate DAGs under nonlinear relationships.

### Feature Subset & Stratified Analysis
For each algorithm, causal discovery is performed under four different feature configurations:
- All available features  
- Top 20 features ranked by feature importance  
- Top 10 features ranked by feature importance  
- Top 5 features ranked by feature importance  

Additionally, **stratified analyses** are conducted by splitting the dataset based on:
- Age groups  
- Gender  

This allows comparison of causal structures across demographic subgroups, revealing potential differences in variable interactions for different patient populations.
