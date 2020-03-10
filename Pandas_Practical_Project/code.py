# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 
 



# code starts here
bank = pd.read_csv(path)
categorical_var = bank.select_dtypes(include = 'object')
print (categorical_var)
numerical_var = bank.select_dtypes(include = 'number')
print (numerical_var)


# code ends here


# --------------
# code starts here
banks = bank.drop(columns = 'Loan_ID')
print (banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)
banks = banks.fillna('bank_mode')
print(banks.isnull().sum())
#code ends here



# --------------
# Code starts here






avg_loan_amount = pd.pivot_table(data=banks , index = ['Gender','Married','Self_Employed'] , values = 'LoanAmount' , aggfunc = np.mean)

# code ends here



# --------------
# code starts here
a = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status'] == 'Y')]
loan_approved_se = a.count()[0]
b = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status'] == 'Y')]
loan_approved_nse = b.count()[0]
print (loan_approved_se)
print(loan_approved_nse)
percentage_se = loan_approved_se*100/614
percentage_nse = loan_approved_nse*100/614
print(round(percentage_se,2))
print(round(percentage_nse,2))
# code ends here


# --------------
# code starts here
loan_term = banks['Loan_Amount_Term'].apply(lambda x : x / 12)
#print (loan_term)
big_loan_term = loan_term[loan_term >= 25].count()
print (big_loan_term)


# code ends here


# --------------
# code starts here

loan_groupby = banks.groupby('Loan_Status')

loan_groupby = loan_groupby[['ApplicantIncome','Credit_History']]

mean_values = loan_groupby.mean()
# code ends here


