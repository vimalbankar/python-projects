import pandas as pd #import pandas for data manipulation
import matplotlib.pyplot as plt #import matplotlib for data visualization
import seaborn as sns#import seaborn for advanced data visualization

df = pd.read_csv("C:/Users/hp/Downloads/HR-Employee-Attrition.csv")# Load dataset
print("\nFirst 5 Rows of Dataset:")# Display first 5 rows
print(df.head())# Display dataset 
print("\nDataset Information:")#print dataset info
print(df.info())#info function for information about dataset

#Data Cleaning
print("\nChecking Missing Values:")# print missing values
print(df.isnull().sum())# No missing values found
df.drop( #Drop irrelevant columns
    ['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'],# columns to drop
    axis=1,# axis=1 for columns
    inplace=True #inplace=True to modify original dataframe
)
print(df.shape) # print shape after dropping columns
print(df.dtypes)# print data types of columns

#Separate categorical and numerical columns

categorical_cols = df.select_dtypes(include='object').columns #select categorical columns of object (string) type
numerical_cols = df.select_dtypes(exclude='object').columns #select numerical columns excluding object type

print("\nCategorical Columns:") # print categorical columns
print(categorical_cols)

print("\nNumerical Columns:")# print numerical columns
print(numerical_cols)
#Encode binary categorical columns (text → numbers)

df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})# Encode 'Attrition' column,map() used to replace values
df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})# Encode 'OverTime' column
df['Gender'] = df['Gender'].map({'Male': 1, 'Female': 0})# Encode gender column

# Verify changes
print(df[['Attrition', 'OverTime', 'Gender']].head())# print first 5 rows of encoded columns
print("\nUpdated data types:")# print data types of encoded columns
print(df.dtypes[['Attrition', 'OverTime', 'Gender']])# print data types of updated encoded columns

#Check unique values in multi-category columns

multi_cat_cols = [ #list of multi-category columns
    'BusinessTravel',# column names
    'Department',
    'EducationField',
    'JobRole',
    'MaritalStatus'
]
for col in multi_cat_cols:# iterate through multi-category columns ,multi_cat_cols is a list
    print(f"\nUnique values in {col}:")# print unique values
    print(df[col].unique())# print unique values of the column,unique() function used to get unique values
#Check value counts for multi-category columns
for col in multi_cat_cols:
    print(f"\nValue counts for {col}:")
    print(df[col].value_counts())# print value counts of the column,value_counts() function used to get counts of unique values
#pandas:1.Average Monthly Income by Department
avg_income_dept = df.groupby('Department')['MonthlyIncome'].mean()# group by department and calculate mean monthly income
print(avg_income_dept)

# pandas:2.Job Role with Highest Average Income
avg_income_role = df.groupby('JobRole')['MonthlyIncome'].mean().sort_values(ascending=False)# group by job role and calculate mean monthly income, sort in descending order
print(avg_income_role)
#pandas:3 Average Job Satisfaction by Department
dept_satisfaction = df.groupby('Department')['JobSatisfaction'].mean().sort_values(ascending=False)# group by department and calculate mean job satisfaction, sort in descending order
print(dept_satisfaction)
#pandas:4.Attrition Rate (%) by Department
attrition_rate = df.groupby('Department')['Attrition'].mean() * 100# group by department and calculate mean attrition rate, multiply by 100 to get percentage
print(attrition_rate)
#pandas:5.Average Work-Life Balance by Job Role
wlb_role = df.groupby('JobRole')['WorkLifeBalance'].mean().sort_values(ascending=False)# group by job role and calculate mean work-life balance, sort in descending order
print(wlb_role)
#pandas:6.Employees with More Than 3 Companies
job_hoppers = df[df['NumCompaniesWorked'] > 3].shape[0]# filter employees with more than 3 previous companies and count them,shape[0] gives the number of rows
print("Employees with more than 3 previous companies:", job_hoppers)

#seaborn:1.How does monthly income vary across departments and genders?
plt.figure(figsize=(9, 5))# set figure size,9x5 inches

sns.boxplot(# create box plot because it shows distribution
    x='Department',
    y='MonthlyIncome',
    hue='Gender',# hue for gender separation
    data=df
)

plt.title('Monthly Income Distribution by Department and Gender')
plt.xlabel('Department')
plt.ylabel('Monthly Income')

plt.tight_layout()# adjust layout to prevent overlap
plt.show()# display plot
#seaborn:2.How does job satisfaction differ across job levels?
plt.figure(figsize=(8, 5))

sns.violinplot(# create violin plot to show distribution and density
    x='JobLevel',
    y='JobSatisfaction',
    data=df,
    inner='quartile',# show quartiles inside the violin plot 
    color='lightgreen'
)

plt.title('Job Satisfaction Distribution Across Job Levels')
plt.xlabel('Job Level')
plt.ylabel('Job Satisfaction')

plt.tight_layout()
plt.show()
#seaborn:3.What is the relationship between age and monthly income?
plt.figure(figsize=(8, 5))

sns.scatterplot( # create scatter plot to show relationship and correlation
    x='Age',
    y='MonthlyIncome',
    hue='JobLevel',# hue for job level separation
    data=df
)

plt.title('Age vs Monthly Income by Job Level')
plt.xlabel('Age')
plt.ylabel('Monthly Income')

plt.tight_layout()
plt.show()
#seaborn:4.How are work-life balance and job satisfaction related?
plt.figure(figsize=(8, 5))

corr_data = df[['WorkLifeBalance', 'JobSatisfaction', 'EnvironmentSatisfaction']].corr() # calculate correlation between satisfaction factors 

sns.heatmap(# create heatmap to visualize correlation
    corr_data,
    annot=True,# annotate cells with correlation values and True to show values
    cmap='coolwarm' # color map for better visualization
)

plt.title('Correlation Between Satisfaction Factors')

plt.tight_layout()
plt.show()
# matplotlib
# 1. Attrition vs Department(bar plot)
plt.figure(figsize=(8, 5))

sns.countplot( # create count plot to show counts of attrition by department 
    x='Department',
    hue='Attrition', # hue for attrition separation
    data=df
)
plt.title('Employee Attrition by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.legend(title='Attrition', labels=['No', 'Yes']) # legend for attrition labels and title
plt.tight_layout()
plt.show()
#2.Attrition vs Job Role(bar plot)
plt.figure(figsize=(10, 6))

sns.countplot( # create count plot to show counts of attrition by job role
    y='JobRole', # y-axis used because many job roles
    hue='Attrition',
    data=df
)
plt.title('Employee Attrition by Job Role')
plt.xlabel('Number of Employees')
plt.ylabel('Job Role')
plt.legend(title='Attrition', labels=['No', 'Yes'])

plt.tight_layout()
plt.show()

#3.Attrition vs Monthly Income (Matplotlib Histogram)
plt.figure(figsize=(8, 5))

plt.hist( # create histogram to show distribution of monthly income by attrition status
    df[df['Attrition'] == 0]['MonthlyIncome'], # select monthly income where attrition is 0 and no attrition
    bins=20,# number of bins,bins=20 for better granularity,means 20 intervals
    alpha=0.7,# transparency level, alpha=0.7 for better visibility meaning 70% opaque,opaque means not see-through
    label='No Attrition'
)
plt.hist( # create histogram for attrition = 1, meaning attrition happened
    df[df['Attrition'] == 1]['MonthlyIncome'],
    bins=20,
    alpha=0.7,
    label='Attrition'
)
plt.title('Monthly Income Distribution by Attrition')
plt.xlabel('Monthly Income')
plt.ylabel('Number of Employees')
plt.legend()
plt.tight_layout()
plt.show()
#4. Attrition vs OverTime
plt.figure(figsize=(6, 4))

sns.countplot(
    x='OverTime',
    hue='Attrition',
    data=df
)

plt.title('Employee Attrition by OverTime')
plt.xlabel('OverTime (0 = No, 1 = Yes)')
plt.ylabel('Number of Employees')
plt.legend(title='Attrition', labels=['No', 'Yes'])
plt.tight_layout()
plt.show()
#5.Attrition vs WorkLifeBalance
plt.figure(figsize=(7, 5))

sns.countplot(
    x='WorkLifeBalance',
    hue='Attrition',
    data=df
)

plt.title('Employee Attrition by Work-Life Balance')
plt.xlabel('Work-Life Balance (1=Poor, 4=Excellent)')
plt.ylabel('Number of Employees')
plt.legend(title='Attrition', labels=['No', 'Yes'])# legend for attrition labels

plt.tight_layout()
plt.show()
#6. Monthly Income vs Job Level (Box Plot)
plt.figure(figsize=(8, 5))

sns.boxplot(# create box plot to show distribution of monthly income across job levels
    x='JobLevel',
    y='MonthlyIncome',
    data=df,
    color='skyblue'
)

plt.title('Monthly Income Distribution Across Job Levels')
plt.xlabel('Job Level')
plt.ylabel('Monthly Income')

plt.tight_layout()
plt.show()
#seaborn:5.How does distance from home affect monthly income and job level?
sns.jointplot( # create joint plot to show relationship between distance from home and monthly income
    x='DistanceFromHome',
    y='MonthlyIncome',
    data=df,
    kind='scatter',# scatter plot to show relationship
    color='purple'# color of points
)

plt.suptitle('Distance from Home vs Monthly Income', y=1.02)# adjust y for title position y meaning 1.02 is slightly above the plot
plt.show()

