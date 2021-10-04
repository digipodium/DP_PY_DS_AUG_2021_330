from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def init(start_url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(start_url)
    return driver

def load_next_page(driver):
    try:
        link = driver.find_element_by_css_selector('a.next').get_attribute('href')
        driver.get(link)
        return True
    except:
        print("no link found")
        return False

def extract_news(driver):
    target = driver.find_element_by_css_selector('div.lisingNews') 
    news = target.find_elements_by_css_selector('div.news_Itm')
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

def save_to_file(filename='data.csv'):
    pd.DataFrame(data).to_csv(filename)


if __name__ == "__main__":
    url = 'https://www.ndtv.com/latest#pfrom=home-ndtv_mainnavgation'
    driver = init(url)

    data = [] # blank list to hold all news
    while True:
        extract_news(driver)
        if not load_next_page(driver):
            break
    save_to_file('headlines.csv')
    driver.close()


