import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

figure_folder = 'E:/QL_2022/pycharm_project/web_timetable/figure'
if not os.path.exists(figure_folder):
    os.makedirs(figure_folder)

# csv_file = '/Users/qiaosili/Pycharm/web_scraping/data/timetable.csv'
csv_file = 'E:/QL_2022/pycharm_project/web_timetable/data/timetable_20240318.csv'
df = pd.read_csv(csv_file)

df['Hour'] = pd.to_datetime(df['Departs'], format='%H:%M').dt.hour
df['Hour'] = df['Hour'].replace(0, 24)
hourly_frequency_per_day = df.groupby([df['date'], 'Hour']).size()
daily_sum = hourly_frequency_per_day.groupby(level=0).sum()
hourly_frequency_per_day = hourly_frequency_per_day.unstack()


for day, data in hourly_frequency_per_day.groupby(level=0):
    # Unstack the DataFrame to pivot the hour index to columns
    day_of_week = datetime.strptime(day,'%m/%d/%Y').strftime('%A')
    data = data.unstack().fillna(0)
    data = data.reset_index(level=1, drop=True)
    sum_value = daily_sum.loc[day]

    # Plot the figure for each day
    fig, ax = plt.subplots(figsize=(14, 8))
    data.plot(kind='bar', ax=ax, width=0.8)
    ax.set_xlabel('Hour')
    ax.set_ylabel('Frequency')
    ax.set_title(f'Hourly frequency of passing trains of {day}({day_of_week}), Total number of trains: {sum_value}')
    ax.grid(axis='y')
    plt.xticks(rotation=1)

    # Anotate number on bars
    for i, v in enumerate(data):
        ax.annotate(f'{v}', xy=(i, v), xytext=(0, 3), textcoords='offset points', ha='center', va='bottom', fontsize=10)
    plt.tight_layout()
    # plt.show()
    day_name = day.replace('/', '-')
    plt.savefig(os.path.join(figure_folder,f'plot_{day_name}_{day_of_week}.jpg'), bbox_inches='tight', dpi=300)
    plt.close()


print('figures are saved.')

