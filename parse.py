from bs4 import BeautifulSoup
from pip._vendor import requests
import fake_useragent
url = "https://my-calend.ru/holidays"
def getInfo():
    string = ""
    user = fake_useragent.UserAgent().random
    header = {"user-agent":user}
    my_request = requests.get(url, headers = header).text
    soup = BeautifulSoup(my_request, 'html.parser')
    divs = soup.findAll('div', attrs={'class':'holidays main'})
    for div in divs:
        response = div.find('article', class_ = 'holidays-day')
    sequence = response.find('section').find('ul', class_ = 'holidays-items').findAll('li')
    for i in range(0,len(sequence) - 1):
        string  += sequence[i].text[1:-4] + '\n'

    return  string




getInfo()



