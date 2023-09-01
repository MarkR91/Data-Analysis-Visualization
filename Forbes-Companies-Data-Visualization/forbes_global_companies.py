import pandas as pd
import matplotlib.pyplot as plt


# Set the area of the plot
plt.rcParams["figure.figsize"] = (16, 10)

# Read in n<=100 rows from the Forbes data set.
df = pd.read_csv('forbes_global_2022_companies.csv').head(100)


# Check for missing values
# print(df.isna().to_string())


# Use the following to strip problematic leading and trailing whitespaces that might cause key read errors from each column name.
df.columns = df.columns.str.strip()

# Extract the sales figures from strings of columns: sales
df['sales'] = df['sales'].str.extract('(\d+)',expand=False)
df['sales']=  pd.to_numeric(df['sales'])


# Do a barchart showing total sales for each company in the dataset.
         
sales_stats = df.sort_values(by='sales',ascending=False).head(10) #sort values for first 10 companies
print(sales_stats.to_string())


sales_stats.plot(kind='bar',y='sales', x='global company',rot=20, fontsize=6) #create bar chart
                                          

# Add axis labels and title
plt.xlabel('Company')
plt.ylabel('Sales (Billions 2022)')
plt.title('Sales by Company')

# Show the plot of Sales of the top 10 Global Companies
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
