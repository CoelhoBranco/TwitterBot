import requests
from bs4 import BeautifulSoup

    
class TrendingTopics:
    
    def __init__(self) -> None:
        html_doc = requests.get('https://trends24.in/brazil/')
        html_doc = html_doc.text
        self.soup = BeautifulSoup(html_doc, 'html.parser')
        
    
    def handle_data(self):
        #tag_class = self.soup.find_all(['li', 'a', 'span'])
        tag_class = self.soup.find_all(['ol', 'li'])
        
        brute_data = []
        for tag in tag_class:
            brute_data.append((tag.a.text))
          
        clean_list = []
 
        for element in brute_data:
            if element not in clean_list:
                clean_list.append(element)
        
        return clean_list
        

    def top_10(self):
        return self.handle_data()[:10]
        
    
    def all_topics(self):
        return self.handle_data()
        
        
if __name__ == '__main__':
    trending = TrendingTopics()
    data = trending.top_10()
    print(data)

        
    