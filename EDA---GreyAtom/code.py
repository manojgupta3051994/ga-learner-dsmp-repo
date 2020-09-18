# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns





#Code starts here
data = pd.read_csv(path)

data['Rating'].plot.hist()

data = data[data['Rating'] <= 5]

data['Rating'].plot.hist()


#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()

percent_null = (total_null/data.isnull().count())

missing_data = pd.concat([total_null,percent_null],keys=['Total','Percent'],axis=1)

print(missing_data)

data.dropna(inplace=True)

total_null_1 = data.isnull().sum()

percent_null_1 = (total_null_1/data.isnull().count())


missing_data_1 = pd.concat([total_null_1,percent_null_1],keys=['Total','Percent'],axis=1)

print(missing_data_1)


# code ends here


# --------------

#Code starts here
sns.catplot(x="Category",y="Rating",data=data, kind="box",height=10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')
plt.show()


#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here



# --------------
#Code starts here
print(data['Price'].value_counts())

data['Price'] = data['Price'].str.replace('$','')
data['Price'] = data['Price'].astype(float)
sns.regplot(x='Price',y= 'Rating',data=data)
plt.title('Rating vs Price [RegPlot]')
plt.show()

#Code ends here


# --------------

#Code starts here
print(data['Genres'].unique())

data['Genres'] = data.Genres.str.split(';',expand=True)

gr_mean = data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print (gr_mean.describe())

gr_mean = gr_mean.sort_values(by='Rating')

print(gr_mean.head(1))
print(gr_mean.tail(1))

#Code ends here


# --------------

#Code starts here
print(data['Last Updated'])

data['Last Updated'] = pd.to_datetime(data['Last Updated'])

max_date = data['Last Updated'].max()

data['Last Updated Days'] = max_date - data['Last Updated']
data['Last Updated Days'] = data['Last Updated Days'].dt.days

sns.regplot(x="Last Updated Days", y="Rating", data=data)
plt.title('Rating vs Last Updated [RegPlot]')
plt.show()


#Code ends here


