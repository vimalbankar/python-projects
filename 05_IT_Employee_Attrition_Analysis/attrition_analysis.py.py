import pandas as pd              # Used only to load CSV file
import numpy as np               # Used for numerical/statistical operations
import statistics as stats       # Used for classical statistics concepts

# Load the cleaned HR dataset
df = pd.read_csv("C:/Users/hp/Downloads/HR-Employee-Attrition.csv")  # Reads employee data

# Convert required columns to NumPy arrays (DO THIS ONCE)
income = np.array(df['MonthlyIncome'])        # Monthly salary values
age = np.array(df['Age'])                     # Employee age values
experience = np.array(df['TotalWorkingYears'])# Total experience values

#1.What is the mean, median, and standard deviation of employee monthly income?
mean_income =np.mean(income)        # Calculates average salary of employees
median_income = np.median(income)    # Finds middle salary value
std_income = np.std(income)          # Measures salary spread from the mean

print("Mean Monthly Income:", mean_income)      # Prints average income
print("Median Monthly Income:", median_income)  # Prints median income
print("Standard Deviation of Income:", std_income)  # Prints income variability
#2.What are the minimum income, maximum income, quartiles, and Interquartile Range (IQR) of monthly income?
min_income = np.min(income)              # Finds the lowest monthly salary
max_income = np.max(income)              # Finds the highest monthly salary

q1 = np.percentile(income, 25)           # Calculates 25th percentile (Q1)
q2 = np.percentile(income, 50)           # Calculates 50th percentile (Median)
q3 = np.percentile(income, 75)           # Calculates 75th percentile (Q3)

iqr = q3 - q1                             # Calculates Interquartile Range (Q3 − Q1)

print("Minimum Monthly Income:", min_income)   # Prints minimum income
print("Maximum Monthly Income:", max_income)   # Prints maximum income
print("First Quartile (Q1):", q1)               # Prints Q1 value
print("Median (Q2):", q2)                       # Prints median value
print("Third Quartile (Q3):", q3)               # Prints Q3 value
print("Interquartile Range (IQR):", iqr)        # Prints IQR

#3.Is the monthly income distribution skewed? If yes, is it positively or negatively skewed?
# Reuse previously calculated statistics
mean_income =np.mean(income)        # Calculates average salary of employees
median_income = np.median(income)       # Calculates middle income value
std_income = np.std(income)             # Calculates spread of income values

# Calculate skewness using Pearson’s formula
skewness = (mean_income - median_income) / std_income  # Measures distribution asymmetry

print("Mean Income:", mean_income)       # Prints mean income
print("Median Income:", median_income)   # Prints median income
print("Standard Deviation:", std_income) # Prints income variability
print("Skewness of Income:", skewness)   # Prints skewness value


#4.What is the covariance between employee experience and monthly income?
cov_matrix = np.cov(experience, income)    # Calculates covariance matrix for experience & income
cov_exp_income = cov_matrix[0, 1]          # Extracts covariance value between experience and income

print("Covariance Matrix:\n", cov_matrix)  # Prints full covariance matrix
print("Covariance between Experience and Income:", cov_exp_income)  # Prints required covariance
#5.What is the correlation between employee age and monthly income?
corr_matrix = np.corrcoef(age, income)   # Calculates correlation matrix between age and income
age_income_corr = corr_matrix[0, 1]      # Extracts correlation value between age and income

print("Correlation Matrix:\n", corr_matrix)  # Prints full correlation matrix
print("Correlation between Age and Income:", age_income_corr)  # Prints required correlation

#6.What proportion of employees earn more than one standard deviation above the mean monthly income?
mean_income = np.mean(income)              # Calculates average monthly income
std_income = np.std(income)                # Calculates standard deviation of income

high_income_threshold = mean_income + std_income  # Defines high-income cutoff (Mean + 1 SD)

high_income_count = np.sum(income > high_income_threshold)  # Counts employees above cutoff
total_employees = len(income)              # Counts total number of employees

high_income_probability = high_income_count / total_employees  # Calculates probability

print("Mean Income:", mean_income)                          # Prints mean income
print("Standard Deviation:", std_income)                    # Prints income spread
print("High Income Threshold:", high_income_threshold)      # Prints cutoff value
print("High Income Employee Count:", high_income_count)     # Prints number of high earners
print("Probability of High Income Employees:", high_income_probability)  # Prints probability

#7.How are employees distributed across income quartiles?
q1 = np.percentile(income, 25)        # Calculates first quartile (25%)
q2 = np.percentile(income, 50)        # Calculates second quartile (median)
q3 = np.percentile(income, 75)        # Calculates third quartile (75%)

q1_count = np.sum(income <= q1)                       # Counts employees in Q1
q2_count = np.sum((income > q1) & (income <= q2))     # Counts employees in Q2
q3_count = np.sum((income > q2) & (income <= q3))     # Counts employees in Q3
q4_count = np.sum(income > q3)                        # Counts employees in Q4

print("Employees in Q1 (Lowest Income Group):", q1_count)
print("Employees in Q2 (Lower-Middle Income Group):", q2_count)
print("Employees in Q3 (Upper-Middle Income Group):", q3_count)
print("Employees in Q4 (Highest Income Group):", q4_count)

#8.Does monthly income approximately follow a normal distribution (Empirical Rule check-68–95–99.7 Rule)?
mean_income = np.mean(income)           # Calculates average monthly income
std_income = np.std(income)             # Calculates standard deviation of income

lower_bound = mean_income - std_income  # Defines lower bound (Mean - 1 Std)
upper_bound = mean_income + std_income  # Defines upper bound (Mean + 1 Std)

within_one_std = np.sum((income >= lower_bound) & (income <= upper_bound))  # Counts incomes within range
total_employees = len(income)           # Counts total employees

percentage_within_one_std = (within_one_std / total_employees) * 100  # Converts count to percentage

print("Mean Income:", mean_income)                         # Prints mean income
print("Standard Deviation:", std_income)                   # Prints standard deviation
print("Lower Bound:", lower_bound)                          # Prints lower bound
print("Upper Bound:", upper_bound)                          # Prints upper bound
print("Employees within 1 Std Dev:", within_one_std)        # Prints count within range
print("Percentage within 1 Std Dev:", percentage_within_one_std)  # Prints percentage

#9.What is the most common (mode) employee age, and what does it tell us about the workforce?
mode_age = stats.mode(df['Age'])    # Finds the most frequently occurring age

print("Mode of Employee Age:", mode_age)  # Prints the most common employee age

#.10.What is the coefficient of variation (CV) of monthly income, and what does it indicate about salary inequality?
mean_income = stats.mean(df['MonthlyIncome'])   # Calculates average monthly income
std_income = stats.stdev(df['MonthlyIncome'])   # Calculates standard deviation of income

cv_income = (std_income / mean_income) * 100    # Calculates coefficient of variation in percentage

print("Mean Monthly Income:", mean_income)       # Prints mean income
print("Standard Deviation of Income:", std_income)  # Prints income spread
print("Coefficient of Variation (%):", cv_income)   # Prints relative variability

#.11.What are the quartiles (Q1, Q2, Q3) of monthly income using the statistics module, and what do they indicate?
quartiles = stats.quantiles(df['MonthlyIncome'], n=4, method='inclusive')  # Divides income into 4 equal parts

q1 = quartiles[0]   # First quartile (25% of employees earn below this)
q2 = quartiles[1]   # Second quartile (median income)
q3 = quartiles[2]   # Third quartile (75% of employees earn below this)

print("First Quartile (Q1):", q1)      # Prints lower income boundary
print("Second Quartile (Median / Q2):", q2)  # Prints median income
print("Third Quartile (Q3):", q3)      # Prints upper-middle income boundary

#12.Is the monthly income distribution positively skewed, negatively skewed, or symmetric (using mean–median logic)?
mean_income = stats.mean(df['MonthlyIncome'])     # Calculates average income
median_income = stats.median(df['MonthlyIncome']) # Calculates middle income value

print("Mean Monthly Income:", mean_income)        # Prints mean income
print("Median Monthly Income:", median_income)    # Prints median income

if mean_income > median_income:                   # Checks if mean is greater than median
    print("Income distribution is Positively Skewed")
elif mean_income < median_income:                 # Checks if mean is less than median
    print("Income distribution is Negatively Skewed")
else:                                             # Checks if mean equals median
    print("Income distribution is Symmetric")

#.13.What is the probability that an employee earns more than the median monthly income?
median_income = stats.median(df['MonthlyIncome'])   # Calculates median monthly income
total_employees = len(df['MonthlyIncome'])          # Counts total number of employees

above_median_count = sum(df['MonthlyIncome'] > median_income)  # Counts employees earning above median

probability_above_median = above_median_count / total_employees  # Calculates probability

print("Median Monthly Income:", median_income)       # Prints median income
print("Employees earning above median:", above_median_count)  # Prints count above median
print("Probability of earning above median:", probability_above_median)  # Prints probability

#14.Hypothesis Testing: Is the average monthly income greater than ₹50,000?
hypothesized_mean = 50000                         # Sets benchmark salary for testing
sample_mean = stats.mean(df['MonthlyIncome'])    # Calculates sample mean income
sample_std = stats.stdev(df['MonthlyIncome'])    # Calculates sample standard deviation
n = len(df['MonthlyIncome'])                     # Calculates sample size

standard_error = sample_std / (n ** 0.5)         # Calculates standard error of the mean
z_score = (sample_mean - hypothesized_mean) / standard_error  # Calculates Z-score

print("Sample Mean Income:", sample_mean)         # Prints sample mean
print("Hypothesized Mean:", hypothesized_mean)    # Prints benchmark mean
print("Standard Error:", standard_error)          # Prints standard error
print("Z-score:", z_score)                        # Prints Z-score

if z_score > 1.645:                               # Critical value for 5% significance (right-tailed)
    print("Reject H0: Average income is significantly greater than 50,000")
else:
    print("Fail to Reject H0: Not enough evidence that income is greater than 50,000")

#15.Is salary variability different between junior-level and senior-level employees?
junior_income = df[df['JobLevel'] <= 2]['MonthlyIncome']   # Selects income of junior employees
senior_income = df[df['JobLevel'] >= 4]['MonthlyIncome']   # Selects income of senior employees

junior_std = stats.stdev(junior_income)   # Calculates salary variability for junior employees
senior_std = stats.stdev(senior_income)   # Calculates salary variability for senior employees

print("Standard Deviation (Junior Employees):", junior_std)  # Prints junior salary spread
print("Standard Deviation (Senior Employees):", senior_std)  # Prints senior salary spread

#.16.Does employee experience significantly influence monthly income? (Final statistical inference)
# Calculate covariance between experience and income
cov_matrix = np.cov(experience, income)           # Creates covariance matrix
cov_exp_income = cov_matrix[0, 1]                 # Extracts covariance value

# Calculate correlation between experience and income
corr_matrix = np.corrcoef(experience, income)     # Creates correlation matrix
corr_exp_income = corr_matrix[0, 1]               # Extracts correlation value

print("Covariance (Experience vs Income):", cov_exp_income)   # Prints covariance
print("Correlation (Experience vs Income):", corr_exp_income) # Prints correlation

# Final inference based on statistical results
if cov_exp_income > 0 and corr_exp_income > 0:
    print("Inference: Employee experience has a positive influence on monthly income.")
else:
    print("Inference: Employee experience does not show a strong positive influence on income.")

