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
