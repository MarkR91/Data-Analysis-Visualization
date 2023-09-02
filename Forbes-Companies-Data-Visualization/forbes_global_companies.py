import pandas as pd
import matplotlib.pyplot as plt

# Functions to be used to process the sales data stored as as alphanumeric strings in the sales columns.

def convertToB(x):
    x= x.str.extract('(\d+\.\d+|\d+)',expand=False)
    ix =pd.to_numeric(x)
    return ix/1000

def convertToNumeric(x):  
    x= x.str.extract('(\d+\.\d+|\d+)',expand=False)
    ix =pd.to_numeric(x)
    return ix

# Set the dimensions of the plot
plt.rcParams["figure.figsize"] = (16, 10)

# Read in n<=100 rows from the Forbes data set.
df = pd.read_csv('forbes_global_2022_companies.csv').head(100)

# Check for missing values
# print(df.isna().to_string())

# Check data types of columns in the dataframe created
print(df.info)

# Use the following to strip any problematic leading and trailing whitespaces that might cause key read errors for any column name.
df.columns = df.columns.str.strip()

# Standardize the sales data in the dataframe to Billions and with the float datatype. The Forbes data set is stored as alphanumeric strings and the sales column gives figures in both millions with 'M'and billions'B'.
# The following code is used to convert sales figures given in 'M' millions to billions and store it as a float. Similarly, sales figures recored as "$7.52 B" are converted to 7.52 for example.

df['sales'].mask(df['sales'].str.endswith("M"),convertToB,inplace=True)
df['sales'] = df['sales'].astype(str)

df['sales'].mask(df['sales'].str.endswith("B") ,convertToNumeric,inplace=True)
df['sales'] = df['sales'].astype(float)

# Do the barchart showing total sales for each company in the dataset.    
# Sort the values in descending order for first 10 companies.    
sales_stats = df.sort_values(by='sales',ascending=False).head(10) 
#print(sales_stats.to_string())

sales_stats.plot(kind='bar',y='sales', x='global company',rot=20, fontsize=6) #create bar chart
                                          
# Add title and axis labels 
plt.title('Sales by Company')
plt.ylabel('Sales (Billions 2022)')


# Show the plot of sales of the top 10 Global Companies
plt.show()

# Calculate the average profit
# average_profit = df['profit'].mean()

# Create a scatter plot of x verses y
# plt.scatter(df['x'],df['y'])

# Add axis labels and title
# plt.xlable()
# plt.ylabel()
# plt.title()
         
# Create a series of the countries in the dataframe and sort alphabetically. Also, add an index to series created.

# Get the number of countries 
country_counts = df["country"].value_counts() 

# Find the most common country making it into the Forbes listings.Sort in descending order.
most_popular_country = country_counts.sort_values(ascending=False).index[0]
print("most_popular_country =",most_popular_country)

# Find the least common country making it into the Forbes listings 
least_popular_country = country_counts.sort_values(ascending=True).index[0]
print("least_popular_country =",least_popular_country)

# Create a new data frame?

# Return the x row and y row in the Pandas DataFrame -> df.loc[[0, 1]]  

# Return the default number of rows with head() method.

# Run a correlation on this dataset?
