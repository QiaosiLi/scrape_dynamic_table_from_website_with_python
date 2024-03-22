# Scraping dynamic table from the website with Python
## Motivation: 

I moved into a flat where I could always hear the rumble of trains, and then I realized that there is an underground railway just next to the flat. The rumbling sound is annoying and I wonder how often the trains passe by. Live timetables for specific train stations can be viewed on the e ScotRail official website as shown below,

![Screen Recording 2024-03-16 at 2 13 11 PM (1)](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/2d017c07-2971-49c4-98ed-81dc976f0dd9)

## Methods:
In order to scrape the information of the live timetable, I wrote a Python code by using the Selenium library to open the website and scrape data every 10 min from 5:00 - 23:59, Monday to Sunday (code/scrape_timetable.py). Bar charts are generated to visualize how many trains pass each hour per day (code/figure.py)

## Results:

![plot_3-14-2024_Thursday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/e6816917-9dc6-4af3-a134-9dfaedcbd19f)
![plot_3-15-2024_Friday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/df5954bd-f20a-4c66-b993-1e64a030ee10)
![plot_3-16-2024_Saturday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/c204379b-aa50-4555-a8fd-b9cda2461ac5)
![plot_3-17-2024_Sunday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/f5240c34-cccf-4145-ac7c-fd5f41be2f16)
![plot_3-18-2024_Monday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/be2839c7-8eac-4a74-9390-a3ace68f8378)
![plot_3-19-2024_Tuesday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/1a7fd0e2-9be5-4586-9ecf-2cfc5c089170)
![plot_3-20-2024_Wednesday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/655e36da-0138-4cc2-9bef-b0b462720457)
![plot_3-21-2024_Thursday](https://github.com/QiaosiLi/scrape_dynamic_table_from_website_with_python/assets/140426435/b3318849-6dd6-49cd-8bb6-baf0095c5cd5)

## Conclusion:




