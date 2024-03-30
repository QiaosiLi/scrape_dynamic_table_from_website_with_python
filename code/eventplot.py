import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

figure_folder = '/figure'
if not os.path.exists(figure_folder):
    os.makedirs(figure_folder)

csv_file = '/data/timetable_20240318.csv'
df = pd.read_csv(csv_file)
dep_time = pd.to_datetime(df['Departs'], format='%H:%M')
df['Departs2'] = dep_time.dt.hour.replace(0,24)+dep_time.dt.minute/60
df['Interval'] = df['Departs2'].diff()*60  # The time interval between two trains, calculated in mins.
departs = df.groupby('date')['Departs2'].apply(list)
interval = df.groupby('date')['Interval']
max_interval_depart = df.loc[interval.idxmax()-1, 'Departs']
print(max_interval_depart) # print the max interval of departure time of the day.

fig, ax = plt.subplots(figsize=(30, 6))
plt.eventplot(departs, linelengths=0.8)
ax.set_xlabel('Hour')
ax.set_ylabel('Day')
ax.set_title('The departure time of trains in each day', fontsize=12)
ax.set_xticks(np.arange(5.5, 25, 0.5))
ax.set_yticks(np.arange(0,7))
date_list = pd.to_datetime(departs.index.tolist())
day_of_week_list = date_list.strftime('%Y-%m-%d (%A)')
ax.set_yticklabels(day_of_week_list)
plt.savefig(os.path.join(figure_folder,'eventplot.jpg'), bbox_inches='tight', dpi=300)
plt.close()
print('figures are saved.')
