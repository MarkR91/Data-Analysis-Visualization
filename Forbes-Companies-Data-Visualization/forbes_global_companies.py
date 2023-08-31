import pandas as pd
import matplotlib.pyplot as plt


# Change the style of plots
# plt.rcParams["figure.figsize"] = (10, 6)
# plt.rcParams["font.size"] = ?
# plt.rcParams["axes.grid"] = True


# Read in Forbes data set (n<=100)
df = pd.read_csv('') #rank , global company, country ,sales 	,profit 	,assets	,market value


# Check for missing values
print(df.isna().to_string())
         
# Use dropna() if need be

# Do a barchart showing total sales for each company in the dataset.
         
rev_stats = df['sales'].sort_values('',ascending=False)  #sort values

rev_stats[''].plot(kind='bar',rot=0) #create bar chart
                                          

# Add axis labels and title
plt.xlabel('Company')
plt.ylabel('Sales')
plt.title('Sales by Company')

# Calculate the average profit
average_profit = df['Profit'].mean()

# Create a scatter plot of x verses y
# plt.scatter(df['x'],df['y'])

# Add axis labels and title
plt.xlable()
plt.ylabel()
plt.title()
         
# Create a series of the countries in the dataframe and sort alphabetically
# Also, add an index to series created.

# Get the number of countries 

country_counts = df["country"].value_counts() 

# Find the most common country making it into the Forbes listings 

most_popular_country = country_counts.sort_values(ascending=False).index[0]


# Create a new data frame?

# Return the x row and y row in the Pandas DataFrame -> df.loc[[0, 1]]  

# Return the default number of rows with head() method.

# Run a correlation on this dataset?


