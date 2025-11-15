import pandas as pd
import numpy as np
import joblib

# # Load test dataset
# test_file = 'TestDatasetExample.xls'
# df_test = pd.read_excel(test_file)
# s
# patient_ids = df_test['ID']
# #load the model
# final_model = joblib.load('rfs_model.joblib')
# X_test = df_test.drop(columns=['ID', 'pCR (outcome)', 'RelapseFreeSurvival (outcome)'], errors='ignore')

# rfs_pred = final_model.predict(X_test)

# output = pd.DataFrame({
#     'PatientID': patient_ids,
#     'RFS': np.round(rfs_pred, 2)
# })
# output.to_csv('RFSPrediction.csv', index=False)


#load the final model pipeline
final_model = joblib.load('rfs_model.joblib')

# Load the test data 
test_file = 'TestDatasetExample.xls' 
df_test = pd.read_excel(test_file)

patient_ids = df_test['ID']

df_test = df_test.replace(999, np.nan)

X_test = df_test.drop(columns=['ID', 'pCR (outcome)', 'RelapseFreeSurvival (outcome)'], errors='ignore')

#Prediction
rfs_pred = final_model.predict(X_test)

output = pd.DataFrame({
    'PatientID': patient_ids,
    'RFS': np.round(rfs_pred, 2)
})

output.to_csv('RFSPrediction.csv', index=False)
