import pandas as pd
import matplotlib.pyplot as plt

csv_file = '/Users/qiaosili/Pycharm/web_scraping/data/timetable.csv'
df = pd.read_csv(csv_file)

# Convert 'Departs' column to datetime type
df['Departs'] = pd.to_datetime(df['Departs'], errors='coerce')

# Drop rows with missing datetime values (if any)
df.dropna(subset=['Departs'], inplace=True)

# Extract hour from 'Departs' column
df['Hour'] = df['Departs'].dt.hour

# Convert 'date' column to datetime type
df['date'] = pd.to_datetime(df['date'])

# Group by date and hour, and count frequency
hourly_frequency_per_day = df.groupby([df['date'].dt.date, 'Hour']).size()

# Unstack the DataFrame to pivot the hour index to columns
hourly_frequency_per_day = hourly_frequency_per_day.unstack()

# Plot the figure
hourly_frequency_per_day.plot(kind='bar', figsize=(14, 8), width=0.8)
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.title('Hourly Departure Frequency per Day')
plt.xticks(rotation=45)
plt.legend(title='Hour', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(axis='y')
plt.show()