from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())

webpage = "https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation"
driver.get(webpage)

target = driver.find_element_by_css_selector('div.lisingNews') # single
news = target.find_elements_by_css_selector('div.news_Itm')  # multi

# loop through all the news
data = []
for item in news:
    try:
        title = item.find_element_by_css_selector('h2.newsHdng').text
    except:
        title = ""
    try:
        posted_by = item.find_element_by_css_selector('span.posted-by').text
    except:
        posted_by = ""
    try:
        content = item.find_element_by_css_selector('p.newsCont').text
    except:
        content =  ""

    data.append({
        'title':title,
        'posted_by':posted_by,
        'content':content
    })
    # loop ends

if len(data) > 0:
    pd.DataFrame(data).to_csv('todays_headlines.csv')
else:
    print("NO news headlines found")
driver.close() 

