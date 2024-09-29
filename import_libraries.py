# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load COVID-19 Data from a URL
url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
covid_data = pd.read_csv(url)

# Step 2: Display the first few rows of the data
print("First few rows of the COVID-19 dataset:")
print(covid_data.head())

# Step 3: Data Cleaning (optional - depending on your needs)
covid_data = covid_data.drop(['Province/State', 'Lat', 'Long'], axis=1)
covid_data.columns = covid_data.columns.str.replace(' ', '_').str.lower()

# Step 4: Summing cases across all countries over time
time_series = covid_data.iloc[:, 4:].sum(axis=0)

# Step 5: Plot total confirmed cases over time
plt.figure(figsize=(10, 6))
plt.plot(time_series.index, time_series.values)
plt.title('Total Confirmed COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
