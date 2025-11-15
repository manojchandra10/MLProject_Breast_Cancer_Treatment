# Machine Learning Project for Breast Cancer Treatment Response Prediction

This is an Adacemic project, a part of COMP4139 Machine Learning Module, supervised by **Dr. Direnc Pekaslan** and **Dr. Shreyank N. Gowda**. The goal is to build machine learning models that can predict how breast cancer patients respond to chemotherapy using both **clinical data** and **MRI-based features**.

We’ll work on two main tasks:
1. **PCR Prediction (Classification)** – predicting whether a patient will achieve *pathological complete response* (PCR).
2. **RFS Prediction (Regression)** – estimating *relapse-free survival* (RFS) time after treatment.

The project will use Python and popular ML libraries like **Scikit-learn**, **Pandas**, **NumPy**, and others.

---

## Project Aim
To develop and evaluate machine learning models capable of predicting:
- **PCR (Pathological Complete Response):** a binary classification task.
- **RFS (Relapse-Free Survival):** a regression task estimating continuous survival time.

The models will be trained on clinical and MRI-derived features to help improve treatment planning and patient outcomes.

---

## Dataset
The dataset is based on the **I-SPY 2 TRIAL** and has been simplified for this assignment.

- **Training set:** `trainDataset.xls` (400 patients)
- **Test set:** hidden (provided later for evaluation)
- Each patient record includes:
  - **11 clinical features** (e.g., Age, ER, HER2, Tumour Stage, etc.)
  - **107 MRI-based features** extracted using **PyRadiomics**.
- Missing values are represented by `999`.

---

## Project File Structure
```
ML_Project_Breast_Cancer/
│
├── data/
│   ├── trainDataset.xls
│   └── testDatasetExample.xls
│
├── src/
│   ├── FinalTestPCR.py
│   ├── FinalTestRFS.py
│   ├── PCR.ipynb
│   └── RFS.ipynb
│
├── outputs/
│   ├── PCRPrediction.csv
│   └── RFSPrediction.csv
│
└── report.pdf
```

---

## Tools & Libraries
You can use any standard Python ML libraries, such as:
- **Scikit-learn** – model building and evaluation
- **Pandas** / **NumPy** – data handling and preprocessing
- **Matplotlib** / **Seaborn** – data visualization
- **TensorFlow** / **PyTorch** – for deep learning (if applicable)

Note: No AutoML or Large Language Model–based automation is allowed for model selection or optimization.
