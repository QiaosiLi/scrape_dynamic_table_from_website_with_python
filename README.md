# Scraping dynamic table from the website with Python
## Motivation: 

I moved into a flat where I could always hear the rumble of trains, and then I realized that there is an underground railway just next to the flat. The rumbling sound is annoying and I wonder how often the trains pass by. Live timetables for specific train stations can be viewed on the ScotRail official website as shown below,

![Screen Recording 2024-03-16 at 2 13 11 PM (1)](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/2d017c07-2971-49c4-98ed-81dc976f0dd9)

## Methods:
In order to scrape the information of the live timetable, I wrote a Python code by using the Selenium library to open the website and scrape data every 10 min from 5:00 - 23:59, Monday to Sunday (code/scrape_timetable.py). Event plot (eventplot.py) and bar charts (code/barchat.py) are generated to visualize how many trains pass by per day.

## Results:
![eventplot](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/1e188c48-d620-4c3a-bdc8-2d3d301dc9b8)
![plot_3-18-2024_Monday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/6670d884-41ce-4e62-8bd3-e0a5518e4ecd)
![plot_3-19-2024_Tuesday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/73bead03-0336-4882-af30-7cc110570446)
![plot_3-20-2024_Wednesday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/aaf654bf-ac17-4eae-a665-2855745ea809)
![plot_3-21-2024_Thursday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/7081c619-f28a-4dab-b096-f322840d0c95)
![plot_3-22-2024_Friday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/48e0b94a-0a42-4b2c-989f-86bb0ef8eac8)
![plot_3-23-2024_Saturday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/3b863e53-f51e-419b-8c7d-51c63e5df56f)
![plot_3-24-2024_Sunday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/264ed4fb-633c-4f11-a657-7c5fe217cab3)

## Conclusion:
1. Using the Selenium library works well without being denied by the website.

2. There are so many trains passing by every day, so DO NOT stay at home all day! Getting some peace during 21:21-21:45 (24 min) and 22:51-23:20 (29 min). Hope to move out soon...

## Updates:
I moved out of this 'train flat' on 26th March 2025, after spending 790 days here—finally.

