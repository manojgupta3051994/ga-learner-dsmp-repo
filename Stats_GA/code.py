# --------------
#Header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#path of the data file- path

#Code starts here 
data = pd.read_csv(path)
data['Gender'].replace('-','Agender',inplace=True)
gender_count = data['Gender'].value_counts()
gender_count.plot(kind='bar')



# --------------
#Code starts here
alignment = data['Alignment'].value_counts()
alignment.plot(kind='pie')
plt.title('Character Alignment')


# --------------
#Code starts here
sc_df = data[['Strength','Combat']]
sc_covariance = sc_df.Strength.cov(sc_df.Combat)
print (sc_covariance)
sc_strength = sc_df['Strength'].std()
sc_combat = sc_df['Combat'].std()
x = sc_strength*sc_combat
sc_pearson = sc_covariance/x
print (round(sc_pearson,2))
ic_df = data[['Intelligence','Combat']]
ic_covariance = ic_df.Intelligence.cov(ic_df.Combat)
print (ic_covariance)
ic_intelligence = ic_df['Intelligence'].std()
ic_combat = ic_df['Combat'].std()
y = ic_intelligence*ic_combat
ic_pearson = ic_covariance/y
print (round(ic_pearson,2))



# --------------
#Code starts here
total_high = data['Total'].quantile(q=0.99)
super_best = data[data['Total']>total_high]
super_best_names = []
super_best_names.append(super_best['Name'])
print (super_best_names)



# --------------
#Code starts here
fig,(ax_1,ax_2,ax_3) = plt.subplots(1,3)
ax_1.boxplot(data['Intelligence'])
ax_1.set_title('Intelligence')
ax_2.boxplot(data['Speed'])
ax_2.set_title('Speed')
ax_3.boxplot(data['Power'])
ax_3.set_title('Power')


