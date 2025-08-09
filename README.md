# Yuyang-Tao-Degree-Project
Here is the code repo for the degree project: **Causal Reasoning for Predictive Health Modeling**

The project uses electronic health record (EHR) data to forecast 30‑day readmission and to uncover the patient factors that drive those outcomes. It combines high‑performing machine‑learning predictors with three state‑of‑the‑art causal discovery pipelines (Nonlinear‑NOTEARS, FCI + RCIT, and DECI) for patient specific intervention planning.

> **All code referenced in the thesis is located in the `mimic/` folder.**  
> **The CSV dataset files used in the code can be found in the [Release section](https://github.com/yuyangtao11/Yuyang-Tao-Degree-Project/releases/tag/Dataset).**

## Environment Setup

To ensure reproducibility, all dependencies from the development environments have been merged into a single Conda file: **`environment.yml`**.  

### 1) Create the environment
```bash
conda env create -f environment.yml
```

### 2) Activate the environment
```bash
conda activate degree-project
```
> The environment name `degree-project` is defined in the YAML file.

### Notes
- This environment covers the whole workflow:
  - **Preprocessing** (extraction, cleaning, encoding)
  - **Machine Learning** (XGBoost, Random Forest, LightGBM, CatBoost, TabPFNv2, Logistic Regression + SHAP)
  - **Causal Discovery** (DECI, FCI+RCIT, Nonlinear-NOTEARS)
- The YAML includes both **conda** and **pip** packages; Conda will orchestrate installs automatically.
- If you encounter conflicts, first update Conda:
```bash
conda update -n base -c defaults conda
```
- If you use Graphviz via `pydot/graphviz` and installed with `pip`, make sure a system Graphviz binary is available in `PATH`.
