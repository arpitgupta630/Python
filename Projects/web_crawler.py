import requests
from bs4 import BeautifulSoup
import pprint

response = requests.get("https://news.ycombinator.com/news")

soup_obj = BeautifulSoup(response.text, "html.parser")

links = soup_obj.select(".titlelink")       # Grab all titlelink class
subtext = soup_obj.select(".subtext")           # Grab all score class

def sort_by_vote(resut_list):
    return sorted(resut_list, key=lambda key: key["Votes"], reverse=True)

def coustom_result(links, subtext):
    result = []
    for index, item in enumerate(links):
        
        title = item.getText()
        href = item.get("href")
        vote = subtext[index].select(".score")

        if len(vote) :
            points = int(vote[0].getText().replace(" points", ""))  
            if points > 99:
                result.append({"Title": title, "Votes": points, "Link": href})
        
    return sort_by_vote(result)

def web_crwaler(link, subtext):
    links = link
    subtext = subtext
    for i in range(2,11):
        new_response = requests.get("https://news.ycombinator.com/news?p=" + str(i))
        new_soup_obj = BeautifulSoup(new_response.text, "html.parser")
        new_links = soup_obj.select(".titlelink")
        new_subtext = soup_obj.select(".subtext")
        
        links = links + new_links
        subtext = subtext + new_subtext
    return coustom_result(links, subtext)


for top_news in web_crwaler(links, subtext):
    pprint.pprint(top_news)
    print('\n')
