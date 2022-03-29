import os

from Bromo.bromo import Bromo
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

from scrapper import TrendingTopics

class TwitterBot:
    
    def __init__(self):
        '''
                    #options.add_argument('--headless')
                    options.add_argument('--no-sandbox')
                    #options.add_argument('--disable-gpu')
                    options.add_argument('--window-size=1280x1696')
                    options.add_argument('--hide-scrollbars')

                    options.add_argument('--enable-logging')
                    options.add_argument('--log-level=0')
                    options.add_argument('--v=99')
                    options.add_argument('--single-process')
                    options.add_argument('--data-path=/tmp/data-path')
                    options.add_argument('--ignore-certificate-errors')
        '''
        options = Options()
        #options.add_argument(f'user-data-dir={os.path.join(os.getcwd(),"modelos", userid, "wpp")}')
        options = webdriver.ChromeOptions()
        
    
        options.add_argument(f'user-data-dir={os.getcwd()}/ChromeProfile/Profile 1')
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        
        self.bromo = Bromo(self.driver)
        self.driver.get('')
            
    
    def get_top_10(self):
        trending = TrendingTopics()
        return trending.top_10()
            
    
    def send_tweet(self, tweet='testando'):
        tweet_click_btn = 'document.querySelector("#react-root > div > div > div.css-1dbjc4n.r-18u37iz.r-13qz1uu.r-417010 > header > div > div > div > div.css-1dbjc4n.r-1habvwh > div.css-1dbjc4n.r-1r5su4o.r-e7q0ms > a > div > span > div > div > span > span").click()'
        self.driver.execute_script(tweet_click_btn)
        self.bromo.write('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div', tweet)
        


if __name__ == '__main__':
    twitter = TwitterBot()
    twitter.send_tweet()


        