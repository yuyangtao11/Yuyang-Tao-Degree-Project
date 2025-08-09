This folder holds every script and notebook referenced in the thesis.  
All experiments follow a three‑step workflow:  
1) Data preparation  
2) Machine learning prediction  
3) Causal discovery  

The CSV dataset files used in the code can be found in the [Release section](https://github.com/yuyangtao11/Yuyang-Tao-Degree-Project/releases/tag/Dataset).  
## Preprocessing

The `preprocessing` folder contains all scripts and notebooks used to extract, clean, and prepare the dataset before running machine learning and causal discovery experiments.

### Workflow
1. **Merge_Pat_Adm.py**  
   Extracts relevant patient and admission information from the downloaded MIMIC-IV database, and stores the result in `merged_with_readmission.csv`.

2. **LAE_cal.py**  
   Calculates **Length**, **Acuity**, and **Emergency visits** from the LACE index, saving the results to `merged_with_readmission_with_LACE.csv`.

3. **C_cal.py**  
   Calculates **Comorbidity** from the LACE index, producing `merged_with_LACE.csv`.

4. **copecat.ipynb**  
   Uses the CopeCat pipeline to extract patient data, merges it with previously extracted data, and outputs `after_cop.csv`.

5. **preprocessing.ipynb**  
   Performs further preprocessing, including:
   - Variable name mapping  
   - Removing outliers  
   - Dropping variables with excessive missing values  
   - Encoding variables  

   Produces:
   - `encoded_clean_data.csv` – cleaned and encoded dataset  
   - `encoded_clean_data2.csv` and `encoded_clean_data3.csv` – i.i.d. processed and feature-selected datasets for use in later ML and causal discovery stages.

6. **Visualization.ipynb**, **eda.ipynb**, **LA_age_check.ipynb**  
   Conduct exploratory data analysis and visualization, focusing on variables such as **age**, **LACE score**, and **gender**.  
   Additional variables are also analyzed to ensure only valid and relevant features are used in subsequent experiments.

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
- **Age groups**  
- **Gender**  

This allows comparison of causal structures across demographic subgroups, revealing potential differences in variable interactions for different patient populations.
